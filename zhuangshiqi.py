def log (text):
    print (1)
    def aaa (func):
        print (2)
        def bbb (*args,**kw):
            print (text,(func.__name__))
            return func(*args,**kw)
        print (3)
        return bbb
    print (4)
    return aaa

@log('111')
def now ():
    print ('0122')


now()

