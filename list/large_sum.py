def sum_list(s):
    if s==[]:
        return 0
    else:
        return s[0]+sum_list(s[1:])

def large_sum(s, n):
    """返回一个子列表，该子列表所有元素和小于或等于n，且最大限度地接近于n
    
    >>> large([4,2,5,6,7],3)
    [2]
    >>> large([4,2,5,6,7],8)
    [2,6]
    >>> large([4,2,5,6,7],19)
    [4,2,6,7]
    >>> large([4,2,5,6,7],20)
    [2,5,6,7]

    """
    if s == []:
        return []
    elif s[0]>n:
        return large_sum(s[1:],n)
    else:
        first=s[0]
        with_s0=[first]+large_sum(s[1:],n-first)
        without_s0=large_sum(s[1:],n)
        if sum_list(with_s0)>sum_list(without_s0):
            return with_s0
        else:
            return without_s0
