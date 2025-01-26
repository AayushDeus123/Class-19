#Importing Math along with some functions
import math
a = int(input('Enter the angle to find its Trigonometric values : '))

s = math.sin(a)
c = math.cos(a)
t = math.tan(a)

print('\nThe Sine of' ,a, 'is' ,s)
print('The Cosine of' ,a, 'is' ,c)
print('The Tangent of' ,a, 'is' ,t)

b = float(input('\nEnter a decimal number to Round it : '))

c = math.ceil(b)
f = math.floor(b)

print('The round of' ,b, 'to its uppermost value is' ,c)
print('The round of' ,b, 'to its lowermost value is' ,f)

d = int(input('\nEnter a number to find its factorial : '))
g = math.factorial(d)
print('The factorial of' ,d, 'is' ,g)