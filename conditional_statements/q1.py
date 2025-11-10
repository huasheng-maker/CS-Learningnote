#兔子五分钟内每分钟走y步，然后休息5分钟，乌龟每分钟走x步，不休息
#俩人何时第一次相遇
def race(x,y):
    #兔子必须走快但不能走得太快
    assert y>x and y<=2*x
    tortoise,hare,minute=0,0,0
    while minute==0 or tortoise-hare: #只要非0就会一直执行下去
        tortoise+=x
        if minute%10<5:
            hare+=y
        minute+=1
    return minute


