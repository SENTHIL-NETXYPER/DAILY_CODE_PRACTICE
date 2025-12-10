a=11
fab=[0,1]
for i in range(2,a):
    fab.append(fab[-1]+fab[-2])
print(fab)