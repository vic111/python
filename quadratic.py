import math

def qua(a,b,c):
    b=b/a
    c=c/a
    a=1
    i1=(b/2)        #合并后B值
    i2=(b/2)**2     #C位置的数据
    i3=c-i2     #D 位置的数据
    l1=+math.sqrt(i3)+i1
    l2=-math.sqrt(i3)+i1
    return l1,l2

