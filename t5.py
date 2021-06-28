fname = input("Enter file name: ")
if len(fname) < 1:
    fname = "mbox-short.txt"

fh = open(fname)
count = 0
for line in fh:
    if not line.startswith("From"):
        continue
    else :
        if line.startswith("From:"):
            
            print((line.strip().split(":")[1].rstrip()).split(" ")[1])
            count = count + 1
            #lstt = list()
            #lstt.append(line.split(":")[1])
            #print(lstt)
            #text=line
            #pos=text.find(":")
            #lngth=len(text)
            #untrimmrd=text[pos+1:29]
            #fltNumVal=float(untrimmrd.strip())
            #total = total + fltNumVal
        else :
            continue

print("There were", count, "lines in the file with From as the first word")

