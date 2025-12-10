s="senthil"
sum=1
for x in s:
    if x in "aeiouAEIOU":
        print(sum,end="")
        sum+=1
    else:
        print(x,end="")    
          