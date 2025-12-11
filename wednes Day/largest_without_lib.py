a=[2,54,65,87,45,34,23,12]
lar=a[0]
count=0
for x in a:
    if x >lar:
        lar=x
        count+=1
print(lar)  
print("number of times largest updated :",count)      