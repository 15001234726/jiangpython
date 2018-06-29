
# 次方
def myAbs(x):
    if not isinstance(x,(int,float)):
        raise TypeError("lalala")
    if x >0:
        return x
    else:
        return -x


def power(x,n = 2):
    s = 1
    while n > 0:
        n=n-1
        s=s*x
    return s