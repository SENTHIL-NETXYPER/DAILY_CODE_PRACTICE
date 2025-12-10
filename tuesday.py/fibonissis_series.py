a=5
fib=[0,1]
for i in range(2,a):
    fib.append(fib[i-1]+fib[i-2])
print(fib)