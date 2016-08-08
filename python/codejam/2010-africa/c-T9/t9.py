# Africa 2010
# Problem C - T9 Spelling
# Jon Hanson

# Declare Variables
ifile = 'input.txt'
ofile = 'output.txt'
caselist = []
outlist = []

leadletter = ['a','d','g','j','m','p','t','w']

# Read Input File
with open(ifile,"r") as f:
    cases = int(f.readline())
    for n in range(0,cases):
        caselist.append( f.readline() )


# Do Operation
for n in range(0,cases):
    buf = caselist[n]
    outstr = ''
    prev = ''
    val = 0
    qty = 0
    for i in range(0,len(buf)):
        ch = buf[i]
        for n in range(2,10):
            if ord(ch) > ord(leadletter[n-2]):
                val = n
                qty = ord(ch) - ord(leadletter[n-2])
        if val == prev:
            outstr += ' '
        for j in range(1,qty):
            outstr += str(val)
        prev = val
    outlist.append( outstr+'\n' )



# Write Output File
with open(ofile,"w") as f:
    for n in range(0,cases):
        result = 'Case #' + str(n+1) + ': ' + outlist[n]
        f.write(result)
