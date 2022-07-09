# BE - Evaluation: Level 1

## Assignment

Write a program that asks the user how many Fibonacci numbers to generate and then generates them. Take this opportunity to think about how you can use functions. Make sure to ask the user to enter the number of numbers in the sequence to generate. (Hint: The Fibonacci sequence is a sequence of numbers where the next number in the sequence is the sum of the previous two numbers in the sequence. The sequence looks like this: 1, 1, 2, 3, 5, 8, 13, …)

```python
#Fibnacci series 
def Fibonacci(lim):
    fib_series = [1]
    for x in range(0,lim):
        fib_series.append(fib_series[x-1]+fib_series[x])
    return fib_series

lim = int(input("How many fibnacci numbers you wanna generate: "))
print(Fibonacci(lim))
```
## What is the difference between a parameter and an argument?
when the function is declared like the variables are know argument as shown below.
```python
def Fibonacci(lim):
```
where as when the function is called we pass variables like shown below it is called as parameters.
``` python 
print(Fibonacci(lim))
```

## All functions in Python by default return …?
In python function's return type by default is class nonetype it can be verfied by using type() function.
```bash
<class 'NoneType'>
```
## What are keyword arguments and when should we use them?
Keyword arguments are the arguments we write the argument preceded by an "=" sign then the parameters this increases code readability and due to keyword arguments position is no longer an issue as shown below.

``` python
def sum(a, b):
    print(a+b)

sum (b = 10 , a = 5) 
```
## How can we make a parameter of a function optional?
We can make a prameter of a function optional by assigning some default value to it as shown below.

``` python
def sum(a, b=10):
    return a+b

print(sum(a=10))
```

## What happens when we prefix a parameter with an asterisk (*)?

so we use this (*) operator mostly for multiplication but mostly you will see these in functions basicly they are unpacking lists they are used for arbitrary number of positional arguments as shown below.

``` python
def add(*args):
  return sum(args)
  
print(add(5, 10, 20, 6))
```
## What about two asterisks (**)?

Same as single asterisks they are used for arbitrary number of keyword arguments and they are also used for unpacking dictionaries as shown below.

``` python
def food(**kwargs):
  for items in kwargs:
    print(f"{kwargs[items]} is a {items}")
      
      
dict = {'fruit' : 'cherry', 'vegetable' : 'potato', 'boy' : 'srikrishna'}
food(**dict)
```
## Write a function 
That prints all the prime numbers between 0 and limit where the limit is a parameter.
``` python
#Prime number
def prime(lim):
    primelist = []
    for num in range(1,lim):
        if num>1:
            for i in range(2,num):
                if(num%i ==0):
                    break
            else:
                primelist.append(num)

    return primelist 

lim = int(input("To how many number you want to generate prime number list: "))
print(prime(lim))
```


