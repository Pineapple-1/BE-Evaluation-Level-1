# BE - Evaluation: Level 1 😭
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

## Control Flow

### What is the difference between 10 / 3 and 10 // 3?

10/3 is called divison and 10//3 is called floor divission. "//" this operator neglects the values after the decimal point.

```bash
Result of 10/3: 3.3333333333333335
Result of 10//3: 3
```

### What is the result of 10 \*\* 3?

Double asterisks (\*\*) operator is used for taking exponent also known as power.

```bash
Result : 1000
```

### Given (x = 1), what will be the value of after we run (x += 2)?

x = 1 after the operation 2 will be added into x which will give the output as shown.

```bash
Value : 3
```

### How can we round a number?

By using a built in function called Round() it takes 2 parameters number to round off and number of digits to round off.

```bash
Rounded value : 3.56
```

### What is the result of float(1)?

```bash
float(1) : 1.0
```

### What is the result of bool(“False”)?

```bash
bool(“False”) : True
```

### What are the falsy values in Python?

- The number zero (0)
- An empty string ''
- False
- None
- An empty list []
- An empty tuple ()
- An empty dictionary {}

### What is the result of 10 == “10”?

```bash
(10 == "10") : False
```

### What is the result of “bag” > “apple”?

```bash
("bag" > "apple") : True
```

### What is the result of not(True or False)?

```bash
not(True or False) : False
```

### Under what circumstances does the expression 18 <= age < 65 evaluate to True?

This expression will always return true value if the value of age is greater than or equal 18 and smaller than 65.

### What does range(1, 10, 2) return?

```bash
<class 'range'>, range(1, 10, 2)
```

### Name 3 iterable objects in Python.

- Lists
- Tuples
- Dictionaries
- Sets

## OOP
A very common use case for inheritance is the creation of a custom exception hierarchy. Because we use the class of an exception to determine whether it should be caught by a particular except block, it is useful for us to define custom classes for exceptions that we want to raise in our code. Using inheritance in our classes is useful because if a except block catches a particular exception class, it will also catch its child classes (because a child class is its parent class). That means that we can efficiently write except blocks that handle groups of related exceptions, just by arranging them in a logical hierarchy. Our exception classes should inherit from Python’s built-in exception classes. They often won’t need to contain any additional attributes or methods.
Write a simple program that loops over a list of user data (tuples containing a username, email, and age) and adds each user to a directory if the user is at least 16 years old. You do not need to store the age. Write a simple exception hierarchy that defines a different exception for each of these error conditions:
- the username is not unique
- the age is not a positive integer
- the user is under 16
- the email address is not valid (a simple check for a username, the @ symbol and a domain name is sufficient).

Raise these exceptions in your program where appropriate. Whenever an exception occurs, your program should move on to the next set of data in the list. Print a different error message for each different kind of exception.
Think about where else it would be a good idea to use a custom class, and what kind of collection type would be most appropriate for your directory.
You can consider an email address to be valid if it contains one @ symbol and has a non-empty username and domain name – you don’t need to check for valid characters. You can assume that age is already an integer value.
```python
class CustomException(Exception):
    """Custom Execption Class"""
    pass
class NotUniqueUsername(CustomException):
    """Raise if the exeption occurs when username is not unique"""
    pass
class NegetiveAgeInteger(CustomException):
    """Raise if age is assigned negetive value"""
    pass
class UnderAge(CustomException):
    """Raised when Age is less than 16 years """
    pass
class EmailNotValid(CustomException):
    """Raised when Email is not valid"""
    pass
data = [("Joe", "Joe@Joe.com", 17), ("Adam", "adam@adam.com", 17)]
directory = dict()
for name, email, age in data:
    try:
        if name in directory:
            raise NotUniqueUsername()
        if age < 0:
            raise NegetiveAgeInteger()
        if age < 16:
            raise UnderAge()
        if not ("@" in email):
            raise EmailNotValid()
    except NotUniqueUsername:
        print("Error: "+name+" username not unique.")
    except NegetiveAgeInteger:
        print("Error: Age can not be negetive.")
    except UnderAge:
        print("Error: User "+name+" is underage.")
    except EmailNotValid:
        print("Error: Email is not valid.")
    else:
        directory["Username"] = (name, email)
```
Write an “abstract” class, Box, and use it to define some methods which any box object should have: add, for adding any number of items to the box, empty, for taking all the items out of the box and returning them as a list, and count, for counting the items which are currently in the box. Write a simple Item the class which has a name attribute and a value attribute – you can assume that all the items you will use will be Item objects. Now write two subclasses of Box which use different underlying collections to store items: ListBox should use a list, and DictBox should use a dict.
```python
class Box:
    def add(self, *items):
        print("Add")

    def empty(self):
        print("Empty")

    def count(self):
        print("Count")

class Item:

    def __init__(self, name, value):
        self.name = name
        self.value = value

class Listbox(Box):
    def __init__(self):
        self.items = []

    def add(self, *args):
        self.items.extend(args)

    def empty(self):
        out = self.items
        self.items = []
        return out

    def count(self):
        return len(self.items)

class Dictbox(Box):
    def __init__(self):
        self.items = {}

    def add(self, *args):
        self.items.update(dict((i.name, i) for i in args))

    def empty(self):
        itemsList = self.items.values()
        self.items = {}
        return itemsList

    def count(self):
        return len(self.items)
```
Extending question 2 of this section, Write a function, repack_boxes, which takes any number of boxes as parameters, gathers up all the items they contain, and redistributes them as evenly as possible over all the boxes. Order is unimportant. There are multiple ways of doing this. Test your code a ListBox with 20 items, a ListBox with 9 items and a DictBox with 5 items. You should end up with two boxes with 11 items each, and one box with 12 items.
```python
def repack(*boxes):
    items = []
    print("repacking...")

    for box in boxes:
        items.extend(box.empty())
    
    print("Total Items: ",len(items))
    while items:
        for box in boxes:
            if len(items)> 0:
                box.add(items.pop())
```
```bash
repacking...
Total Items: 34
First Box Item Count: 12
Second Box Item Count: 11
Third Box Item Count: 11
```

## Docker
### Compare different kinds of docker image families. Alpine, Slim, Stretch, Buster, Jessie, Bullseye. What does this mean? How are they different? What advantage do they provide over the others?
Stretch buster jessie bullseye are code names for the version of debian releases bullseye is the currently stable build stretch, buseter and jessie are considred as obsolete. Choose one of these images if your code is compatible with a specific version of the Debian operating system. Older versions of Debian when starting a new project are rarely used.

Slim image is the paired down version of the fullimage this installs the minimal packges needed to run the project. This version saves the space.

Alpine image is the most smallest images. It is best to use apline images if there is a constraint on container space. These are the most varients of images due to their small size but now teams are moving away because of compatibility issues and it is much harder to debug. Alpine images have a disadvantage over some libraires it is not compatible with image as it uses the slimer varients of libraires.
## Difference between Entrypoint and CMD directive in a Dockerfile?
There can only be one CMD instruction in a Dockerfile. If you list more than one CMD then only the last CMD will take effect. The main purpose of a CMD is to provide defaults for an executing container which can be overriden. Entrypoint can not be overriden once specified in the docker file.

## Explain this command written inside a Dockerfile:RUN mkdir /app/django/helloworld
This command is making a folder in the specified path which is named as helloworld.
## Explain the concept of layering in Docker images/containers?

Basically, a layer, or image layer is a change on an image, or an intermediate image. Every command you specify (FROM, RUN, COPY, etc.) in your Dockerfile causes the previous image to change, which creates a new layer. You can think of it as staging changes when you're using git: You add a file's change, then another one, then another one.