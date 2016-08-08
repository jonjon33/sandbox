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
with open(ifile,"r") as f:              # Open ifile as f
    cases = int(f.readline())           # Get num of cases from 1st line
    for n in range(0,cases):            # For each case:
        caselist.append( f.readline() ) # Append a line to the caselist


# Do Operation
for n in range(0,cases):    # For each case:
    buf = caselist[n]           # Take the case string
    outstr = ''                 # Prep an output str
    prev = 0                    # Previous t9 key 'value'
    val = 0                     # Current t9 key 'value'
    qty = 0                     # Current t9 key 'quantity'
    for i in range(0,len(buf)-1):   # For each char in the case string:
        ch = buf[i]                     # Take a char
        if ch == ' ':                   # if it's space
            val = 0                     # t9 val is 0
            qty = 1                     # qty is 1
        else:                       # otherwise
            for n in range(2,10):       # For each possible t9 value:
                if ord(ch) >= ord(leadletter[9-n]):           # if char > ll
                    val = (9-n)+2                            # take that ll val
                    qty = ord(ch) - ord(leadletter[9-n]) + 1 # eval qty of val
                    break                                    # break the for
            if val == prev:             # If val didn't change:
                outstr += ' '               # Add a space to output string
        for j in range(0,qty):      # Iterate qty times:
            outstr += str(val)          # Add val to output string
        prev = val                  # Set prev to val
    outlist.append( outstr+'\n' )   # Append case output str to an output list



# Write Output File
with open(ofile,"w") as f:
    for n in range(0,cases):
        result = 'Case #' + str(n+1) + ': ' + outlist[n]
        f.write(result)
