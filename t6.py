name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name)

counts = dict()
for line in handle:
    if not line.startswith("From:"):
        continue
    else :
        if line.startswith("From"):
            emailAddr=(line.strip().split(":")[1].rstrip()).split(" ")[1]
            #print(emailAddr)
            counts[emailAddr] = counts.get(emailAddr,0) + 1
#print(counts)

bigcount=None
bigword=None
#print(counts.items())
for word,count in counts.items():
    if bigcount is None or count > bigcount : 
        bigword = word
        bigcount = count
print(bigword,bigcount)

