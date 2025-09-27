def fizzbuzz(n):
    assert n>0 and n%1==0, "n must be a positive integer"
    i=1
    while i<=n:
        if i%3!=0 and i%5!=0:
            print(i)
        if i%3==0 and i%5!=0:
            print("Fizz")
        if i%5==0 and i%3!=0:
            print("Buzz")
        if i%3==0 and i%5==0:
            print("FizzBuzz")
        i+=1
    return None