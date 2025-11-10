def is_Prime(n):
    '''
    判断一个数n是否是质数。
    当n<2时，直接返回False;
    当n>=2时，使用while循环遍历2到根号n的所有整数是否能整除n，
    如果是，返回False。如果不是，返回True。

    Args：
        n：要判断的整数n。

    returns：
        bool：布尔值，是质数返回True，否则返回False。
    '''
    assert n >= 0, "Input must be a non-negative integer"
    if n<2 :
        return False
    i=2
    while i*i<=n:
        if n%i==0:
            return False
        i+=1
    return True
