def fbi(n):
    """Compute the nth fibonacci number"""
    pre,curr=1,0
    k=0
    while k<n:
        pre,curr=curr,pre+curr
        k=k+1
    return curr