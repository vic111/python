def fact (x):
    return fact_add(x,1)


def fact_add (x,y):
    if (x==1):
        return y
    return fact_add (x-1,y*x)
