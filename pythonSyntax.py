"""
Basic Python Syntax
----------------------------
This file is a guided template for learning Python basics.
Students should fork and clone this repository from Greg's repo.
Explanations and examples will be added by Greg.
"""

# ==========================================================
# 1. PRINTING AND COMMENTS
# ----------------------------------------------------------
# - Print statements
# - Single-line comments
# - Multi-line comments (docstrings)
# ==========================================================

print("Hello, COP 4814!")  # This is a single-line comment
"""
This is a multi-line comment (docstring).
It can also serve as documentation.
"""

# ==========================================================
# 2. VARIABLES AND DATA TYPES
# ----------------------------------------------------------
# - Strings
# - Integers, floats
# - Booleans
# - Type checking with type()
# ==========================================================

name = "Gregory"        # string
age = 42                # integer
height = 1.78           # float
is_professor = True     # boolean

print(name, age, height, is_professor)
print(type(age))  # <class 'int'>

# ==========================================================
# 3. BASIC OPERATORS
# ----------------------------------------------------------
# - Arithmetic (+, -, *, /, //, %, **)
# - Comparison (==, !=, >, <, >=, <=)
# - Logical (and, or, not)
# ==========================================================

a = 10
b = 3
print(a + b)   # addition → 13
print(a / b)   # division → 3.333...
print(a // b)  # floor division → 3
print(a % b)   # modulus → 1
print(a ** b)  # exponentiation → 1000

print(a > b)   # True
print(a == 10 and b == 3)  # True

# ==========================================================
# 4. STRING OPERATIONS
# ----------------------------------------------------------
# - Concatenation
# - f-strings
# - Common methods (.upper(), .lower(), .strip(), etc.)
# ==========================================================

greeting = "hello"
print(greeting.upper())         # HELLO
print(greeting.capitalize())    # Hello
print(f"My name is {name} and I am {age} years old.")  # f-string

messy_string = "   data science   \n"
print(f"Original: '{messy_string}'")
print(f"Using strip(): '{messy_string.strip()}'")   # removes spaces + newline
print(f"Using lstrip(): '{messy_string.lstrip()}'") # removes only from the left
print(f"Using rstrip(): '{messy_string.rstrip()}'") # removes only from the right

# Example 1: Remove specific characters like punctuation
text = "???Hello World!!!???"
print(text.strip("?"))      # "Hello World!!!"
print(text.strip("?!"))     # "Hello World"

# Example 2: Remove dots and commas
messy = ",,,Python is fun..."
print(messy.strip(",."))    # "Python is fun"

# Example 3: Remove multiple characters including whitespace
mixed = " \t\n***Data Science***\n\t "
print(mixed.strip(" \n\t*"))  # "Data Science"

# Example 4: Only from left or right
sample = "###example###"
print(sample.lstrip("#"))   # "example###"
print(sample.rstrip("#"))   # "###example"


# ==========================================================
# 5. LISTS
# ----------------------------------------------------------
# - Creating lists
# - Indexing and slicing
# - Adding/removing elements
# - Useful methods (.append(), .remove(), .sort(), etc.)
# ==========================================================

fruits = ["apple", "banana", "cherry"]
print(fruits[0])       # apple
print(fruits[-1])      # cherry
fruits.append("mango") # add element
fruits.extend(["strawberry", "grapefruit"])
fruits.insert(1,"kiwi")
fruits.remove("banana")
firstFruit=fruits.pop(0)
print(fruits, firstFruit)
fruits[2]="passio fruit"
fruits.reverse()
fruits.sort()
fruits.sort(reverse=True)

# ==========================================================
# 6. TUPLES AND SETS
# ----------------------------------------------------------
# - Tuples: immutable sequences
# - Sets: unique collections
# ==========================================================

colors = ("red", "green", "blue")
print(colors[0])   # red

# Tuples cannot be modified
try:
    colors[0] = "yellow"
except TypeError as e:
    print("Error:", e)

# But you can create a new tuple from an old one
new_colors = colors + ("yellow",)
print(new_colors)  # ('red', 'green', 'blue', 'yellow')

numbers = {1, 2, 2, 3, 4}  # set → removes duplicates
print(numbers)  # {1, 2, 3, 4}

# ==========================================================
# 7. DICTIONARIES
# ----------------------------------------------------------
# - Key-value pairs
# - Accessing and modifying values
# - Common methods (.keys(), .values(), .items())
# ==========================================================

student = {"name": "Alice", "age": 20, "major": "CS"}
print(student["name"])       # Alice
student["age"] = 21          # update value
print(student.keys())        # dict_keys(['name', 'age', 'major'])


# ==========================================================
# 8. CONDITIONALS
# ----------------------------------------------------------
# - if, elif, else
# - Nested conditionals
# ==========================================================

grade = 85
if grade >= 90:
    print("A")
elif grade >= 80:
    print("B")
else:
    print("C")

# ==========================================================
# 9. LOOPS
# ----------------------------------------------------------
# - for loops
# - while loops
# - break and continue
# ==========================================================

for fruit in fruits:
    print("I like", fruit)

count = 0
while count < 3:
    print("count =", count)
    count += 1

# ==========================================================
# 10. FUNCTIONS
# ----------------------------------------------------------
# - Defining functions
# - Parameters and return values
# - Default arguments
# ==========================================================

def square(x):
    return x * x

print(square(5))  # 25

def greet(name="student"):
    return f"Hello, {name}!"

print(greet())         # Hello, student!
print(greet("Greg"))   # Hello, Greg!

# ==========================================================
# 11. IMPORTING MODULES
# ----------------------------------------------------------
# - Importing built-in modules (e.g., math, random)
# - Using functions from modules
# ==========================================================

import math
print(math.sqrt(16))  # 4.0

import random
print(random.choice(fruits))  # random fruit


# ==========================================================
# 12. ERROR HANDLING (OPTIONAL)
# ----------------------------------------------------------
# - try, except
# - Handling different exception types
# ==========================================================

try:
    print(10 / 0)
except ZeroDivisionError:
    print("You cannot divide by zero!")

