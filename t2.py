# Use words.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)

for lines in fh:
        stripp=lines.strip()
        print(stripp.upper())

