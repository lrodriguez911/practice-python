from ast import operator
from re import X


""" print(1 + 2)

print(3 * 6)

print(input('Ingrese un numero ') + input('ingrese otro numero '))
 """
""" operators in place """
""" x = 3
x +=4
print(x) """

"""Boolean y comparadores"""
""" if x > 1:
    print('x es mayor q uno')
 """
"""ejercicio de practica"""

""" purity = float(input())

if purity >= 91.7:
    print('Accepted') """
 

"""declaracion else"""

""" if x > 10:
    print('x es mayor q cinco')
else:
    print('x no es mayor q cinco') """


""" num = 3
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
 """

"""declaracion elif forma simple de hacer if else"""


""" if num == 1:
    print("One")
elif num == 2:
    print("Two")
elif num == 3: 
    print("Three")
else: 
    print("Something else") """


""" year = 2000
if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print("Leap year")
        else:print("Not a leap year")
    else:print("Leap year")
else:print("Not a leap year")
     """
    
""" bolean logic operator """

""" operator and """
""" print(1 > 0 and 2 > 1) """

""" operator or """
""" print(1 > 0 or 1 > 2)
 """
""" operator not  """
""" print(not 1 > 0) """


""" bucles  """

""" while """

""" x = 1 
while x <= 5:
    print(x)
    x+=1
print("While finished") """


""" whilw and if else """

""" x = 1
while x < 10:
    if x % 2 == 0:
        print(str(x) + " is Even")
    else:
        print(str(x) + " is odd")
    x+=1 """


""" exercises bucle while """
""" #tu código va aqui
points = 100
i = 0
while i < 4:
    x = input()
    if x == 'hit':
        points += 10
    if x == 'miss':
        points -= 20
    i+=1
    
print(points) """


""" exercises system of entries """

""" i = 0
price = 0
while i <= 4:
    i+= 1
    if int(input('ingrese la edad del pasajero ')) <= 3:
        continue
    price+=100
print(price) """


""" calc of IMC """

weight = int(input('enter your weight '))
height = float(input('enter your height '))
imc = float(weight / (height ** 2))
if imc >= 0 and imc <= 18.4:
    print('Underweight')
elif imc >= 18.5 and imc <= 24.9:
    print('Normal')
elif imc >= 25 and imc <= 29.9:
    print('Overweight')
else:print('Obesity')
