try:

    a=int(input())
    b=int(input())
    c=(a+b)
    print(c)
except Exception as a:

    print("your worng da")    
except SyntaxError:
    print("am not the kinf")    
finally:
    print("am god3")