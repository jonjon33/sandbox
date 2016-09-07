# Quals 2009
# Problem B: Watersheds
# Jon Hanson

#
# Declare Variables
#
ifile = 'input.txt'
ofile = 'output.txt'
caselist = []

#
#
#
class CaseMap(object):
    def __init__(self,height,width,alts):
        self.h = height
        self.w = width
        self.imap = alts

    def printCase(self):
        print(str(self.imap))


#
# read input file
#
with open(ifile,'r') as f:
    cases = int(f.readline())
    for n in range(0,cases):
        dim = list(map(int,f.readline().split(' ')))
        inlist = []
        for row in range(0,dim[0]):
            inlist.append(list(map(int,f.readline().split(' '))))
        case = CaseMap(dim[0],dim[1],inlist)
        caselist.append(case)

#
# conduct algorithm
#
for n in range(0,cases):
    case = caselist[n]
    case.printCase()


#
# write output file
#
with open(ofile,'w') as f:
    for n in range(0,cases):
        case = caselist[n]
        casestr = 'Case #' + str(n+1) + ': '

        casestr += '\n'

        f.write(casestr)
