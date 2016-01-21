L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]

def swap1(b):
    for a in b:
        a=a[::-1]
        yield a

def swap2(t):
    x=swap1(t)
    o=[]
    for z in x:
        o.append(z)
    return o
l=list(sorted(swap2(L),reverse=True))
l=dict(swap2(l))
print (l)

        

