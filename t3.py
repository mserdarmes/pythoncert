# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)
total  = 0.0
avrg = 0.0
counter = 0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:"):
        continue
    else :
        counter = counter + 1
        text=line
        pos=text.find(":")
        lngth=len(text)
        #print(pos)
        #print(lngth)
        untrimmrd=text[pos+1:29]
        fltNumVal=float(untrimmrd.strip())
        total = total + fltNumVal
        #print(total)
        #print(fltNumVal)
        #print(counter)
avrg = total / counter
print("Average spam confidence: " + str(avrg))
#print("Done")
