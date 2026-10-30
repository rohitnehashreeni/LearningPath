

# variables

test_name= 'login works'
expected = 5
actual = 2+3
passed = actual == expected

print(f"{test_name} : {passed}")
print(type(passed))
print(type(test_name))
print(type(expected))
print(type(actual))

# practice ex 1
first_name = 'John'
city = 'New York'

print(f" I am {first_name} and I live in {city}.")

# practice ex 2 String methods
text = "  Python is fun  "

print(text)
print(text.strip())
print(text.lstrip())
print(text.rstrip())

print(text.upper())
print(text.lower())

# practice ex 3 int operators
a = 3
b = 5

print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a % b)
print(a ** b) 
print(a // b) 

#practice ex 4 
string = "49"
number = int(string)
expected = number + 10

print(expected)
print(49 + 10)