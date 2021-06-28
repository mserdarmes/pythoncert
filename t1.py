text = "X-DSPAM-Confidence:    0.8475"

pos=text.find(":")
lngth=len(text)
print(pos)
print(lngth)
untrimmrd=text[pos+1:29]

print(float(untrimmrd.strip()))
