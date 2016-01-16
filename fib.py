#斐波拉契数列

def fib (max):
    n,a,b=0,1,1
    while (n<max):
        yield b
        a,b=b,a+b
        n=n+1
    return 'ok'
