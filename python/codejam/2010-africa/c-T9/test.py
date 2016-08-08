testlist = ['a','d','g','j','m','p','t','w']
ichar = 'h'

def myprint(mystr):
    print(mystr,end='')

myprint(ichar + '\t' + str(ord(ichar)))

myprint('\n\n')

for n in range(2,10):
    ll = testlist[9-n]
    print(ll + '\t' + str(ord(ll)))

myprint('\n\n')

for n in range(2,10):
    ll = testlist[9-n]
    if ord(ichar) > ord(ll):
        val = (9-n)+2
        qty = ord(ichar) - ord(ll) + 1
        myprint(str(val)+'\t'+str(qty))
        break

myprint('\n\n')

for i in range(0,qty):
    myprint(str(val))

print()
