def print_if(s:list,f):
    """
    打印列表s中经过f运算后返回真值的每个元素
    >>> print_if([3, 4, 5, 6], lambda x: x > 4)
    5
    6
    >>> result = print_if([3, 4, 5, 6], lambda x: x % 2 == 0)
    4
    6
    >>> print(result)
    None
    """
    for x in s:
        if f(x):
            print(x)    
    return None

