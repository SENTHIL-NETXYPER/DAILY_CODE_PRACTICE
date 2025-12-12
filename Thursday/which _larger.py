a=[11,2,3,4,45,678,3,345,4567,4,3,3,4,33,4,34]
# a=1,2,3,4,5,6,7
# b=list(map(int,str(a)))


maxy=a[0]
for i in a:
    if i>maxy:
        maxy=i
print(maxy)           
print(max(a))