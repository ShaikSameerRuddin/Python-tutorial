a = 10
b = 10
print(a + b)
print(id(a))


a : int = 10
b : int = 10
print(a+b)
print(id(b))


c = a
print(id(c))

c = a + b
print(id(c))

# re assigning variable 
age = 25

age = 30

age = age + 10

print(age)

# creating multiple variables in one line

name , age, job =  "sameer ruddin", 25, "do nothing"

print(name)
print(age)
print(job)

# assign single value to multiple variables  

num = age = value = 23

print(num)
print(age)
print(value)

# Rules for variables 
# A variable name must start with a letter or the underscore character
# A variable name cannot start with a number or any special character like $, (, * % etc.
# A variable name can only contain alpha-numeric characters and underscores (A-z, 0-9, and _ )
# Python variable names are case-sensitive which means Name and NAME are two different variables in Python.
# Python reserved keywords cannot be used naming the variable

# Naming conventions
# Camel case − First letter is a lowercase, but first letter of each subsequent word is in uppercase. For example: kmPerHour, pricePerLitre

# Pascal case − First letter of each word is in uppercase. For example: KmPerHour, PricePerLitre

# Snake case − Use single underscore (_) character to separate words. For example: km_per_hour, price_per_litre


# Note
# 1. Always create meaningful variables names
# 2. Recommended to use lowercase letter
# 3. Separate multiple words by underscore.
# 4. Avoid funny and meaningless variables names.
# 5. class name should start with uppercase letters


# Delete variables

a = 10

print(a)

del a
print(a)  # NameError: name 'a' is not defined


# Variable annotations
name: str = "sameer ruddin"