stopwords = ['to', 'a', 'for', 'by', 'an', 'am', 'the', 'so', 'it', 'and', "The"]
org = "The organization for health, safety, and education"
acro = []
org = org.split()
for o in org:
    for x in stopwords:
        if o == x:
            org.remove(o)
print(org)
for y in org:
    for a in y:
        a=a.upper()
        acro.append(a)
        break
acro="".join(acro)
print(acro)