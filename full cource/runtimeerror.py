try:
    a=input()
    b=input()
    c=int(input())
    d=a*c
    print(a/c)
except TypeError as a:
    print("it ik",a)
except ValueError as v:
    print("it is value error",v)
except Exception as e:
    print("it sbeen exception",e)
    
finally 
