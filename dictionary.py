#Question 1
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

#Question 2

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

#Question 3
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

