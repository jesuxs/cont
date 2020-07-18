a=[]
for m in range(1,11):
    m=m**3
    a.append(m)
b= a[-3:]
print(b)
print(a[3:8])
print(a)

b=[m**3 for m in range(1,11)]
print(b)