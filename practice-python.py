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



""" weight = int(input())
height = float(input())
imc = float(weight  / height ** 2)

if imc <= 18.4:
    print('Underweight')
elif imc >= 18.5 and imc <= 24.9:
    print('Normal')
elif imc >= 25 and imc <= 29.9:
    print('Overweight')
elif imc >= 30:
    print('Obesity') """


""" lists """

""" m = [0,1,2,3,4]
print(m[0]) """

""" exercises where is mi site """
""" seats = [
['a', 'b', 'c'],
['d', 'e', 'f'],
['g', 'h', 'i'],
['j', 'k', 'l']
]



row = int(input())
column = int(input())
print(seats[row][column]) """


""" using operator 'in' in lists """

""" words = ["spam", "egg", "spam", "sausage"]
print("spam" in words) 
print("egg" in words)
print("tomato" in words)
print("to" in "to") """

""" for word in words:
    print(word) """

""" str = "testing for loops"
count = 0

for x in str:
   if(x == 't'):
    count += 1

print(count) """


""" exercises cart shop discount using for """

""" cart = [15, 42, 120, 9, 5, 380]

discount = int(input())
total = 0
for i in cart:
    total += i-(i*(discount/100))

print(total) """


""" using range  """

""" print(list(range(5))) """

""" for i in list(range(4)):
    print(i)
for i in range(4):
    print(i) """


""" slice a list """
""" squares = [1,2,3,4,5,6,7,8,9,10]
print(squares[2:4])
 """
""" no put last character in slicer go to ends list"""
""" print(squares[0:])  """

""" the slice begin in start """
""" print(squares[:4]) """

""" using a interval putting a third character """

""" print(squares[1:5:2]) """

""" using a negative numbers in slicer """
""" print(squares[0:-2])
 """
""" reverse a str unsing slicer third parametrer number negative """

""" str = str(input())

print(str[::-1]) """

""" calculate the factorial of number """
""" using a formula to calculate the factorial """
""" N = int(input()) """
""" print(int((((N+1)-N)+ N)/2 * N))"""


""" another method to calculate the factorial """
""" T = 0
for i in range(N):
    T += i + 1
    i + 1
print(T) """



""" functions """


""" examples about functions """

""" print("Hello world!")
range(2, 20)
str(12)
range(10, 20, 3) """

""" know length of lists using function len"""
""" str = "hello"
nums = [1,2,3,4,5,6,7]
print(len(nums))
print(len(str)) """

""" append add a element in the final of list """
""" nums = [0,1,2,3,4,5,6,7,8,9,10] """
""" nums.append(5) """
"""print(nums) """

""" insert use to add in list using a index in anywhere of list"""
""" nums.insert(0,0) """
""" print(nums) """


"using index to find first time appear a element"

""" letters = ['a','b','c','d'] """
""" print(letters.index('b'))
print(nums.index(1)) """


""" using diferents funcitons: max, min, count, remove, reverse """

""" max(list): Devuelve el valor máximo.

min(list): Devuelve el valor mínimo.

list.count(item): Devuelve un recuento de cuántas veces aparece un elemento en una lista.

list.remove(item): Elimina un elemento de una lista.

list.reverse(): Invierte los elementos de una lista. """

""" nums = [0,1,2,3,4,5,6,7,8,9,10]

print(max(nums))

print(min(nums))

print(nums.count(1))

nums.remove(1).remove(2)

print(nums)

nums.reverse()
print(nums)
letters.reverse()
print(letters) """

""" exercises list's functions """

""" nums = [0,1,2,3,4,5,6,7,8,9,10]
total = 0
nums.remove(min(nums))
nums.remove(max(nums))

for i in nums:
    total += i

print(total) """


""" format of strings """

""" nums = [1,2,3,4]
msg = "Numbers: {0} {1} {2}". format(nums[0], nums[1], nums[2])
print(msg)

print("{0}{1}{0}".format("abra","cad")) """

""" a='{x} {y}'.format(x=12, y=13)
print(a) """

""" print(','.join(['a','b','c']))

print('abcd'.split())

print('azc'.replace('z', 'b'))

print('abc'.startswith('a'))

print('abc'.endswith('c'))

print('upper'.upper())

print('lower'.lower()) """


""" exercises screaming test """

""" msg = str(input())
print(msg.lower()) """

""" using decalration def to declare a function """

""" def myfunc():
    print("hi")
    print("hello")
    print("Good bye")

myfunc()
    

def hello():
    print("hello {a}".format(a=str(input())))
    
    
hello() """
    

def print_whit_exclamation(word=str(input())):
        print(word + '!')
    
print_whit_exclamation('fizz')
print_whit_exclamation('buzz')
print_whit_exclamation()
    
def print_sum_twice(x=int(input('insert first number to sum ')),y=int(input('insert second number to sum '))):
    print(x + y)
    
print_sum_twice()

""" feet to inches converter """
feet = int(input())

def convert(feet):
    print(feet * 12)

convert(feet)


""" def function to multiply 2 arguments """

def print_mult(x, y):
    print(x * y)
    
print_mult(2, 4)