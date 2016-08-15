# Quals 2009
# Problem A - Alien Language
# Jon Hanson


#
# Declare Global Variables
#
ifile = 'input.txt'
ofile = 'outfile.txt'
wordlist = []
caselist = []
outlist = []
SO_FAR_SO_GOOD = 1
NO_GOOD = 0

#
# parsecase()
#  arg: string
#  ret: list
# desc: parses case statements into list of potential letters
#   ex: case = (ab)b(bc)
#       output = ['ab','b','bc']
#
def parsecase( casestr ):
    retlist = []        # output list of letter possibilities
    buf = ''            # string buffer, holds temp items for retlist
    multi = False       # status flag: is this a multi char read state?

    for i in range(0,len(casestr)): # for each char in input string
        ch = casestr[i]             # ch is char buf

        if ch == '(':               # if open paren
            multi = True            # set multi flag
        elif ch == ')':             # else if close paren
            multi = False               # clear multi flag
        elif ch >= 'a' and ch <= 'z':   # else if letter
            buf += ch                   # append it to string buffer

        if multi == False and buf != '':    # if mutli clear and buf populated
            retlist.append( buf )           # append the buf to retlist
            buf = ''                        # clear the string buf

    return retlist


#
# findmatches()
#  arg: list
#  ret: int
# desc: takes parsed list and finds all matching words in word list
#   ex: wordlist = ['abc','bbb','cba']
#       retlist = ['ab','b','bc']
#       output = 2
#
def findmatches( parsedlist ):
    matches = 0

    for word in wordlist:
        wordstatus = SO_FAR_SO_GOOD

        for n in range(0,letters):
            letterstatus = NO_GOOD
            buf = parsedlist[n]

            for i in range(0,len(buf)):
                if buf[i] == word[n]:
                    letterstatus = SO_FAR_SO_GOOD

            if letterstatus == NO_GOOD:
                wordstatus = NO_GOOD
                break

        if wordstatus == SO_FAR_SO_GOOD:
            matches += 1

    return matches


#
# Read Input File
#
with open(ifile,'r') as f:
    ivals = []

    strbuf = f.readline()
    ivals = list(map(int,strbuf.split(' ')))
    letters = ivals[0]
    words = ivals[1]
    cases = ivals[2]
    for n in range(0,words):
        wordlist.append( f.readline() )
    for n in range(0,cases):
        caselist.append( f.readline() )

#
# Do Operation
#
for n in range(0,cases):
    parsedcase = parsecase(caselist[n])
    outlist.append(str( findmatches(parsedcase) ))

#
# Write Output File
#
with open(ofile,'w') as f:
    for n in range(0,cases):
        result = 'Case #' + str(n+1) + ': ' + outlist[n] +'\n'
        f.write( result )
        print(result,end='')
