first_name = "jetson"
last_name = "cyrus"
mine = "Surprise"
age = 19
height = 169.5
print("Hai ", first_name)
print("My name is " + first_name + " " + last_name)
print(height)
print(type(height))
print(len(first_name))
print(first_name.capitalize())
print(first_name.upper())
print(first_name.lower())
print(first_name.isalpha())
print(first_name.isdigit())
print(first_name.replace("o", "a"))
print(first_name)
print(first_name.count("e"))
print(first_name.count("z"))

# getting input
name = input("whats ur name? ")
age = input("whats ur age? ")
age = int(age)
age = age + 1
print(age)

import math

pi = 3.14
print(round(pi))
print(math.pi)
print(math.ceil(pi))
print(math.floor(pi))
print(abs(pi))
print(pow(pi, 2))
print(math.sqrt(pi))

# slicing
name = "Jetson Cyrus"
first = name[0]
second = name[1]
last = name[-1]
last_prev = name[-2]
something = name[0:]
but = name[-1:]
print(first + " " + second + " " + last + " " + last_prev + " " + last)
print(something)
print(but)
all = name[::2]
print(all)
reversed_name = name[::-1]
print(reversed_name)
print(name[slice(2, 6)])


# if loop
age = int(input("Enter age: "))

if age < 18:
    print("Under age")
elif age == 18:
    print("YOU are NOT fall in any clause")
else:
    print("accepted")

if 18 < age < 58:  # wow
    print("you are eligible")
else:
    print("You are not accepted")

# while loop
i = 0
while i < 10:
    print(i)
    i += 1
# for loop
for i in range(10):  # prints 0 -> 9 last will be excepted
    print(i)

for i in range(1, 10):
    print(i)

# sleep ,..,.,
import time

for i in range(10, 0, -1):
    print(i, end=" ")
    time.sleep(1)


# printing pattern
import time

col = 3
row = 3

for i in range(row):
    for j in range(col):
        print("$", end="")
        time.sleep(1)
    print()


# list in python
food = ["pizza", "rice", "idly", "parotta", "sappathi"]
print(food)
print(food[0])
print(food[-1])
print(food[::-1])       # reverse
food.append("kothuparotta")
food.remove("pizza")
food.pop()
#food.remove(2)       # -- error --
print(food)
food.insert(2, "pizza")
print(food)
food.clear()
print(food)
