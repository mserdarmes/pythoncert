fname = input("Enter file name: ")
fh = open(fname)
lst = list()
for line in fh:
    lnlist = list()
    lnlist = (line.rstrip()).split()
    #print (lnlist)
    #print(range(len(lnlist)))
    for i in range(len(lnlist)):
           #print (lnlist[i])
            if lnlist[i] not in lst :
                lst.append(lnlist[i])
                #print(lst)
    #print(line.rstrip())
lst.sort()
print(lst)
