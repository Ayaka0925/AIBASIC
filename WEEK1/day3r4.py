fib = [0,1]
i=0
n=int(input('n:'))
while i<=n:
    num = fib[i+1] + fib[i]
    fib.append(num)
    i+=1
    print(num)