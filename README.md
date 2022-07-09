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

```python
print(Fibonacci(lim))
```

## All functions in Python by default return …?

In python function's return type by default is class nonetype it can be verfied by using type() function.

```bash
<class 'NoneType'>
```

## What are keyword arguments and when should we use them?

Keyword arguments are the arguments we write the argument preceded by an "=" sign then the parameters this increases code readability and due to keyword arguments position is no longer an issue as shown below.

```python
def sum(a, b):
    print(a+b)

sum (b = 10 , a = 5)
```

## How can we make a parameter of a function optional?

We can make a prameter of a function optional by assigning some default value to it as shown below.

```python
def sum(a, b=10):
    return a+b

print(sum(a=10))
```

## What happens when we prefix a parameter with an asterisk (\*)?

so we use this (\*) operator mostly for multiplication but mostly you will see these in functions basicly they are unpacking lists they are used for arbitrary number of positional arguments as shown below.

```python
def add(*args):
  return sum(args)

print(add(5, 10, 20, 6))
```

## What about two asterisks (\*\*)?

Same as single asterisks they are used for arbitrary number of keyword arguments and they are also used for unpacking dictionaries as shown below.

```python
def food(**kwargs):
  for items in kwargs:
    print(f"{kwargs[items]} is a {items}")


dict = {'fruit' : 'cherry', 'vegetable' : 'potato', 'boy' : 'srikrishna'}
food(**dict)
```

## Write a function

That prints all the prime numbers between 0 and limit where the limit is a parameter.

```python
#Prime number
def prime(lim):
    primelist = []
    for num in range(1,lim):
        if num>1:
            for i in range(2,num):
                if(num % i ==0):
                    break
            else:
                primelist.append(num)

    return primelist

lim = int(input("To how many number you want to generate prime number list: "))
print(prime(lim))
```

## Data types and Manipulation:

We will keep track of when our friend’s birthdays are, and be able to find that information based on their name. Create a dictionary (in your file) of names and birthdays. When you run your program it should ask the user to enter a name and return the birthday of that person back to them. The interaction should look something like this:

```bash
>>> Welcome to the birthday dictionary. We know the birthdays of:
Albert Einstein
Benjamin Franklin
Ada Lovelace
>>> Who`s birthday do you want to look up?
Benjamin Franklin
>>> Benjamin Franklin`s birthday is 01/17/1706.

```
```python
# Question 1
import json
birthdays = {"People": {
    "Albert Einstein": "March 14, 1879",
    "Benjamin Franklin": "January 17, 1706",
    "Ada Lovelace": "December 10, 1815",
    "Ben": "March 8, 2020"
}
}
print("Welcome to the birthday dictionary we know the birthdays of: ")
for key in birthdays["People"]:
    print(key)
person = str(input("Who's birthday do you want to look up?\n"))
print(person+"'s birthday is "+birthdays["People"].get(person))
```
Modify your program from Question 1 of this section to load the birthday dictionary from a JSON file on disk, rather than having the dictionary defined in the program. Finally, ask the user for another scientist’s name and birthday to add to the dictionary, and update the JSON file you have on disk with the scientist’s name. If you run the program multiple times and keep adding new names, your JSON file should keep getting bigger and bigger.

```python
# Question 2
import json
birthdays = dict()
with open("birthdays.json", "r") as file:
    birthdays = json.load(file)
    file.close()
print("Add a birthday in dictionary.")
key = input("Add a person: ")
birthday = input("Add birthday: ")
birthdays["People"][key]=birthday
with open("birthdays.json" , "w") as outfile:
    json.dump(birthdays,outfile,indent=4)
    outfile.close()
```
```json
{
    "People": {
        "Albert Einstein": "March 14, 1879",
        "Benjamin Franklin": "January 17, 1706",
        "Ada Lovelace": "December 10, 1815",
        "Jane Foster": "July 27, 2022",
        "Abdulrehman ajmal": "March 8, 2020"
    }
}
```

We saved information about famous scientists’ names and birthdays to disk. Now we load that JSON file from disk, extract the months of all the birthdays, and count how many scientists have a birthday in each month. (Hint: Use counter from the collections module.)
Your program should output something like: 
```bash
{"May": 3,"November": 2,"December": 1}
```
```python
# Question 3
import json
from collections import Counter
birthdays = dict()
months = []
with open("birthdays.json", "r") as file:
    birthdays = json.load(file)
    file.close()
for key in birthdays["People"]:
   birthday = birthdays["People"].get(key)
   month = birthday.split()
   months.append(month[0])

print(Counter(months))
```
```bash
Counter({'March': 2, 'January': 1, 'December': 1, 'July': 1})
```
## You have a list:

a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]. Write one line of Python that takes this list a and makes a new list that has only the even elements of this list in it.

```python
print("Even :",list(filter(lambda num: num % 2 == 0, numbers)))
```

```bash
Even: [4, 16, 36, 64, 100]
```
