from ast import operator
from re import X


print(1 + 2)

print(3 * 6)

print(input('Ingrese un numero ') + input('ingrese otro numero '))

""" operators in place """
x = 3
x +=4
print(x)

"""Boolean y comparadores"""
if x > 1:
    print('x es mayor q uno')

"""ejercicio de practica"""

purity = float(input())

if purity >= 91.7:
    print('Accepted')
 

"""declaracion else"""

if x > 10:
    print('x es mayor q cinco')
else:
    print('x no es mayor q cinco')


num = 3
if num == 1:
    print('One')
else:
    if num == 2:
        print('Two')
    else:
        if num == 3:
            print('Three')
        else:
            print('Something else')


"""declaracion elif forma simple de hacer if else"""


if num == 1:
    print("One")
elif num == 2:
    print("Two")
elif num == 3: 
    print("Three")
else: 
    print("Something else")


year = 2000
if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print("Leap year")
        else:print("Not a leap year")
    else:print("Leap year")
else:print("Not a leap year")
    
    
""" bolean logic operator """

""" operator and """
print(1 > 0 and 2 > 1)

""" operator or """
print(1 > 0 or 1 > 2)

""" operator not  """
print(not 1 > 0)
