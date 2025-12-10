a=[2,4,3,2,3,4,5,6,7,8,8,8,6]
sum=1
odd=0
for i in a:
    if i%2==0:
        sum+=i
    else:
        odd+=i  
print(sum)
print(odd)