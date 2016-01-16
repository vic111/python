def fib (max):
    n=0
    l=[1,1]
    while (n<max):
        i=len(l)
        l=l+[l[i-1]+l[i-2]]
        n=n+1
    print (l)
