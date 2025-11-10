def unique_digits(n):
    """
    
    Return the number of unique digits in positive integer n.

    >>> unique_digits(8675309) # All are unique
    7
    >>> unique_digits(13173131) # 1, 3, and 7
    3
    >>> unique_digits(101) # 0 and 1
    2
    """
    "*** YOUR CODE HERE ***"
    unique=set()
    for digit in str(n):
        unique.add(digit)
    return len(unique)
    

def has_digit(n, k):
    """
    k为0-9这10个整数中的任意一个整数，
    逐个遍历n的数字，如果存在与k相等整数，返回True；否则返回False；
    Returns whether k is a digit in n.

    >>> has_digit(10, 1)
    True
    >>> has_digit(12, 7)
    False
    """
    "*** YOUR CODE HERE ***"
    assert k >= 0 and k < 10
    while n//10!=0 :
        if n%10==k :
            return True
        n=n//10
    return False