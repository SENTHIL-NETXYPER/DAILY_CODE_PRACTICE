a=123456
b=str(a)
c=[]
for i in b:
    c.append(int(i))
e=sorted(c)  
e=int("".join(map(str,e)))  
d=sorted(c,reverse=True)
d=int("".join(map(str,d)))
print(d-e)














