# Quals 2009
# Problem A - Alien Language
# Jon Hanson

# Declare Variables
ifile = 'input.txt'
ofile = 'outfile.txt'
wordlist = []
caselist = []
outlist = []

def listout(istr):
    # # #
    # Need 2D list, 1D for letters and 1D for options

    for i in range(0,len(istr)-1):
        ch = istr[i]
        if ch == '(':
            mult = True
        else if ch == ')':
            mult = False




# Read Input File
with open(ifile,'r') as f:
    ivals = []

    strbuf = f.readline()
    ivals = map(int,strbuf.split(' '))
    letters = ivals[0]
    words = ivals[1]
    cases = ivals[2]
    for n in range(0,words):
        wordlist.append( f.readline() )
    for n in range(0,cases):
        caselist.append( f.readline() )

# Do Operation
for n in range(0,cases):
    matchlist = []
    matchlist = listout( caselist[n] )
    outlist.append( str(len(matchlist)) )

# Write Output File
with open(ofile,'w') as f:
    for n in range(0,cases):
        result = 'Case #' + str(n+1) + ': ' + outlist[n]
        f.write( result )
