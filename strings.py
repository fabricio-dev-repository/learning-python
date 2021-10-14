print('hello')
print("world")
print('this is also a string')
print("I'm going on a run")
print("hello world 1")
print("hello world 2")
# Scape sequence - Special commands
print('hello \n world')
print('hello \nworld')
# lengh function
print(len("I am"))
# Indexing
mystring = "Hello World"
print(mystring)
print(mystring[0])
print(mystring[9])
print(mystring[8])
# Reverse indexing
print(mystring[-2])
print(mystring[-3])
# Slicing
mystring = "abcdefghijk"
print(mystring)
print(mystring[2])
print(mystring[2:])
print(mystring[:3])
print(mystring[3:6])
print(mystring[1:3])
print(mystring[::2])
print(mystring[2:7:2])
print(mystring[::-1])  # reverse string easy way
# Immutability
name = "Sam"
# name[0] = 'P' result in error
last_letters = name[1:]
print(last_letters)
print('P' + last_letters)
x = "Hello World"
x = x + " it's beautiful outside"
print(x)
letter = 'z'
letter = letter * 10
print(letter)
print(2+3)
print('2'+'3')
# Built-in string methods
x = "Hello World"
print(x.upper())
print(x.lower())
print(x.split())
x = "Hi this is a string"
print(x.split())
print(x.split('i'))
