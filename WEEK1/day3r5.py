x=0

while x<30:
    x+=1
    if x%3==0:
        print('Fizz')
    elif x%5==0:
        print('Bazz')
    elif x%3==0 and x%5==0:
        print('FizzBazz')
    else:
        print(x)


