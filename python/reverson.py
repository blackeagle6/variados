
p_phrase = "was it a car or a cat I saw"
r_phrase= ''
print(p_phrase)
L1=[]
L2=[]
for x in p_phrase:
    L1.append(x)
p_phrase=L1
for x in p_phrase[::-1]:
    L2.append(x)
for x in L2:
    r_phrase+=x
print(r_phrase)




'''r_phrase=[]
for x in p_phrase[::-1]:
    r_phrase.append(x)
    if x == ' ':
        x=x.replace(' ','')
print(*r_phrase)
print(p_phrase)'''

