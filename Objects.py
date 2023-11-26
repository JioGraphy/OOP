# Every value in Python is an Object, and every Object is created by some class

text = "String"
number = 1
l = []
set = {"A", 1}
dict = {"A":1}

# Built-in class attribute / magic method / dunder
print(f" {text} is a {text.__class__}")
print(f" {number} is a {number.__class__}")
print(f" {set} is a {set.__class__}")
print(f" {dict} is a {dict.__class__}")

s = str("hello")
i = int(2)

print("hello".__class__)


def func():
    print("Hi")

n = None

# function is an object of a function class
print(func.__class__)

# every class is also an object from another class
# metaclasses
print(n.__class__.__class__)

