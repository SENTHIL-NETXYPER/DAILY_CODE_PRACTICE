a = [5, 2, 2, 4]
b = 2

c = sorted(a)
d = c[:b]
e = c[-b:]
f = sum(d)
g = sum(e)
ans = abs(g - f)
print(ans)

