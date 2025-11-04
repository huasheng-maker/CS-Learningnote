
def search(f):
    """找出能够使得f(x)为真的x"""
    x = 0
    while not f(x):
        x += 1
    return x


def square(x):
    return x * x

def positive(x):
    return max(0,square(x)-100)

# 求反函数的一般策略，即能将y映射回x
def inverse(f):
    """Return g(y) such that g(f(x))->x"""
    return lambda y:search(lambda x:f(x)==y)
