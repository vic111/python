def my_abs(x):
    if not isinstance (x,(int ,float)):
        raise TypeError ('bad operand tper')
    if x >= 0:
        return x
    else:
        return -x
