a=12345
# str=str(a)[::-1]
# print(str)
 
c=list(map(int,str(a)))
b=int("".join(map(str,c)))
c=int(str(a))

print(type(c),c)


