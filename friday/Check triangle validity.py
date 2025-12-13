a=[60,50,60]
sum=0
for i in a:
    sum+=i
if sum == 180:
    print(sum,"valid triangle") 
elif sum < 180:
    print(sum, "invalid trinagele")      