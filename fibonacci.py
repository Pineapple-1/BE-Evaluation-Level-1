#Fibnacci series 
def Fibonacci(lim):
    fib_series = [1]
    for x in range(0,lim):
        fib_series.append(fib_series[x-1]+fib_series[x])
        return fib_series

lim = int(input("How many fibnacci numbers you wanna generate: "))
print(type(Fibonacci(lim)))