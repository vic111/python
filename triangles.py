#杨辉三角i

def yanghui ():
    l=[0,]
    while (True):
        yield l
        l=[1,]+[l[i]+l[i+1] for i in range(len(l)-1)]+[1,]
n = 0
for t in yanghui():
     print(t)
     n = n + 1
     if n == 10:
         break
