
stopwords = ['to', 'a', 'for', 'by', 'an', 'am', 'the', 'so', 'it', 'and', 'The']
sent = "The water earth and air are vital"
acro = []
z=None
a=1
sent = sent.split()
for o in sent:
    for x in stopwords:
        if o == x:
            sent.remove(o)    
for y in sent:
    z=y[0:2].strip()
    z=z.upper()
    if a < len(sent):
        acro.append(z+". ")
        a += 1
    else:
        acro.append(z)
acro="".join(acro)
print(acro)
print(a)
print(len(sent))