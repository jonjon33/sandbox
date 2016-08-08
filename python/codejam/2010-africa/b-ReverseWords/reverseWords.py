# Africa 2010
# Problem B - Reverse Words
# Jon Hanson

# Declare Variables
ifile = 'B-large-practice.in'
ofile = 'B-large-practice.out'
linelist = []
newlinelist = []

# Read Input File
with open(ifile,'r') as f:
    lines = int(f.readline())
    for n in range(0,lines):
        linelist.append( f.readline() )

# Do Operation
for n in range(0,lines):
    buf1 = linelist[n].split()
    buf2 = []
    for i in range(len(buf1),0,-1):
        buf2.append( buf1[i-1] )
    newlinelist.append( ' '.join(buf2) )

# Write Output File
with open(ofile,'w') as f:
    for n in range(0,lines):
        result = 'Case #'+str(n+1)+': '+str(newlinelist[n])+'\n'
        f.write(result)
