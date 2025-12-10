a="apple banana apple"
b="apple"
count=0
c=a.split()
for i in c:
    if i==b:
        count+=1
print(count)        