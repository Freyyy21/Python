#Int
#Int, or integer, is a whole number, positive or negative, without decimals, of unlimited length.
#Example
x = 1
y = 1321321321
z = -1

print(type(x))
print(type(y))
print(type(z))

#Float
#Float, or "floating point number" is a number, positive or negative, containing one or more decimals.
#Example
x = 1.10
y = 1.0
z = -23.45

print(type(x))
print(type(y))
print(type(z))

#Complex
#Complex numbers are written with a "j" as the imaginary part:
x = 3+5j
y = 5j
z = -5j

print(type(x))
print(type(y))
print(type(z))

#Type Conversion
x = 12
y = 10.2
z = 1j

a = float(x)
b = int(y)
c = complex(x)

print(a)
print(b)
print(c)

print(type(a))
print(type(b))
print(type(c))

#Random Number
#Python does not have a random() function to make a random number, but Python has a built-in module called random that can be used to make random numbers:
import random

print(random.randrange(1,10))
