

# import math
# a=int(input("enter a number:    "))
# print(math.factorial(a))


a=int(input("enter a number:    "))
count=1
for i in range(1,a+1):
    count*=i
print(count)