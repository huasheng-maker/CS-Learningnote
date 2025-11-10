def repeating(t, n):
    """Return whether t digits repeat to form positive integer n.

    >>> repeating(1, 6161)
    False
    >>> repeating(2, 6161)  # repeats 61 (2 digits)
    True
    >>> repeating(3, 6161)
    False
    >>> repeating(4, 6161)  # repeats 6161 (4 digits)
    True
    >>> repeating(5, 6161)  # there are only 4 digits
    False
    """
    if pow(10, t-1) > n:  # make sure n has at least t digits
        return False
    #like t=2
    end =n%pow(10,t) 
    #maximum t:pow(10,t-1)<n & pow(10,t)>n
    rest = n
    while rest:
        if rest % pow(10, t) != end:
           return False
        rest=rest//pow(10,t)
    return True