# Qualification Round 2009
# Problem C: Welcome to Codejam
# Jon Hanson

#
# declare variables
#
ifile = 'input.txt'
ofile = 'output.txt'
caselist = []
targetstr = 'welcome to codejam'

#
#
#
class TargetTracer(object):
    def __init__(self,instr):
        self.instr = instr
        self.hits = 0

    def solve(self):
        

#
# read input file
#
with open(ifile,'r') as f:
    cases = int( f.readline() )
    for n in range(0,cases):
        caselist.append( f.readline() )

#
# do stuff
#
for n in range(0,cases):
    case = caselist[n]


#
# write output file
#
with open(ofile,'w') as f:
    for n in range(0,cases):
        case = caselist[n]

        outstr = 'Case #' + str(n+1) + ': '
        outstr += str(case)
        outstr += '\n'

        f.write(outstr)
