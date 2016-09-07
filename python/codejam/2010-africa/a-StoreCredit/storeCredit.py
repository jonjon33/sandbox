# Africa 2010
# Problem A: Store Credit
# Jon Hanson

#
# Declare Variables
#
ifile = 'input.txt'     # simple input
ofile = 'output.txt'    # simple output
#ifile = 'A-large-practice.in'   # official input
#ofile = 'A-large-practice.out'  # official output
caselist = []           # list containing cases

#
# Problem State (Case) Class
#
class CredCase(object):
    def __init__(self,credit,itemCount,items):  # Initialize:
        self.credit = int(credit)                   # credit amount
        self.itemCount = int(itemCount)             # item count
        self.items = list(map(int,items.split()))   # item values list
        self.cost = -1                              # total cost
        self.solution = []                          # output list

    def trySolution(self,indices):
        cost = self.items[indices[0]] + self.items[indices[1]]
        if (cost <= self.credit) and (cost > self.cost):
            self.cost = cost
            self.solution = [x+1 for x in indices]

#
# Read Input File
#
with open(ifile) as f:
    cases = int(f.readline())
    for n in range(0,cases):
        case =  CredCase(f.readline(),f.readline(),f.readline())
        caselist.append(case)

#
# Conduct Algorithm
#
for n in range(0,cases):
    case = caselist[n]

    for i in range(0,case.itemCount):
        for j in range( (i+1) , case.itemCount ):
            case.trySolution( [i,j] )
            if case.credit == case.cost:
                break
        if case.credit == case.cost:
            break

#
# Write Output File
#
with open(ofile,'w') as f:
    for n in range(0,cases):
        case = caselist[n]

        casestr = 'Case #'+str(n+1)+': '
        casestr = casestr+str(case.solution[0])+' '+str(case.solution[1])+'\n'

        checkstr = 'Check: Credit='+str(case.credit)
        checkstr += ' Cost='+str(case.cost)
        checkstr += ' Item'+str(case.solution[0])+'='
        checkstr += str(case.items[case.solution[0]-1])
        checkstr += ' Item'+str(case.solution[1])+'='
        checkstr += str(case.items[case.solution[1]-1])+'\n'

        f.write(casestr)
        #f.write(checkstr)
