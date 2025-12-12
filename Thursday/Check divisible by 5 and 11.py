a=int(input("Enter first number: "))
for  i in range(1, a+1):
    if i%5==0 and i%11==0:
         print(i)
         print("divisible by 5 and 11")