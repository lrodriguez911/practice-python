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


""" def print_whit_exclamation(word=str(input())):
        print(word + '!')
    
print_whit_exclamation('fizz')
print_whit_exclamation('buzz')
print_whit_exclamation()
    
def print_sum_twice(x=int(input('insert first number to sum ')),y=int(input('insert second number to sum '))):
    print(x + y)
    
print_sum_twice()
 """
""" feet to inches converter """
""" feet = int(input())

def convert(feet):
    print(feet * 12)

convert(feet)
 """

""" def function to multiply 2 arguments """

""" def print_mult(x, y):
    print(x * y)

print_mult(2, 4) """

""" fucntions to calculate a max number of twice """

""" def max(x , y):
    if x >= y:
        return x
    else:
        return y

print(max(4, 8))

z = max(5,9)
print(z) """

""" def shortest_string(x, y):
    if len(x) <= len(y):
        return x
    else:
        return y """

""" print(shortest_string('hola', 'buenos dias')) """

""" def add_numbers(x, y ):
    total = x + y
    return total
   

print(add_numbers(4, 4)) """


""" counter how many letters have a text """

""" def letter_count(text, letter):
    #tu código va aquí
    count =0
    for i in text:
        if i == letter:
            count += 1
    return count
text = input()
letter = input()

print(letter_count(text, letter))
 """


""" practing whit dicconarys it's like object in jscript """

""" ages = {
    "Lucas" : 30,
    "FLor" : 29,
    "Exe": 31
}
print(ages.str) """


""" exercises car selling """


""" car = {
    'brand' : 'BMW',
    'year' : 2018,
    'color': 'red',
    'mileage' : 15000
}
print(car[input()]) """


""" nums = {
    1: "one",
    2: "two",
    3: "three",
}
print(1 in nums)
print("three" in nums)
print(4 not in nums)


pairs = {1: "apple",
  "orange": [2, 3, 4], 
  True: False, 
  12: "True",
}

print(pairs.get("orange"))
print(pairs.get(7, 42))
print(pairs.get(12, "not found")) """

""" add exercises about economic liberty in diferents countries """
""" data = {
    'Singapore': 1,
    'Ireland': 6,
    'United Kingdom': 7,
    'Germany': 27,
    'Armenia': 34,
    'United States': 17,
    'Canada': 9,
    'Italy': 74
}
print(data.get(input(), "Not found")) """


""" tuples in python  """

""" words = ('spam', 'eggs', 'sausages')

print(words[0])

words[1] = 'jam' """

""" my_tuple = 'one', 'two', 'three'

print(my_tuple[0]) """


""" contacts = [
    ('James', 42),
    ('Amy', 24),
    ('John', 31),
    ('Amanda', 63),
    ('Bob', 18)
]

def find(str):
    for i in contacts:
        if i[0] == str:
            return print("{name} is {age}".format(name=i[0], age = i[1]))
    return print("Not Found")
           

find('Amanda')
 """

""" unpaking tuples and assing """


""" numbers = (1, 2, 3)
a, b, c = numbers
print(a)
print(b)
print(c) """


""" using asterisk to take all values  """
""" a, b, *c, d = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(a)
print(b)
print(c)
print(d) """


""" add exercises whit tuples """

""" def calc(x):
    tup = (x*4, x*x)
    return tup
    

side = int(input())
p, a = calc(side)

print("Perimeter: " + str(p))
print("Area: " + str(a)) """

""" exercises whit sets """

""" num_set = {1, 2, 3, 4, 5}

print(3 in num_set) """

""" working whit sets """

""" nums = {1, 2, 1, 3, 1, 4, 5, 6}
print(nums) """

""" use add to add a element in set """
""" nums.add(-7) """

""" use remove to remove a element in set """
""" nums.remove(3)
print(nums) """

""" combine sets whit maths operators """
""" first = {1, 2, 3, 4, 5, 6}
second = {4, 5, 6, 7, 8, 9} """

""" El operador unión  | combina dos conjuntos para formar uno nuevo que contenga elementos en cualquiera de ellos.
El operador intersección & obtiene elementos sólo en ambos.
El operador diferencia - obtiene elementos en el primer conjunto pero no en el segundo.
El operador diferencia simétrica  ^ obtiene elementos en cualquiera de los dos conjuntos, pero no en ambos. """
""" print(first | second)
print(first & second)
print(first - second)
print(second - first)
print(first ^ second) """


""" exercises whit sets """

""" skills = {'Python', 'HTML', 'SQL', 'C++', 'Java', 'Scala'}
job_skills = {'HTML', 'CSS', 'JS', 'C#', 'NodeJS'}

def coincid(set1, set2):
    return print(list(set1 & set2)[len(list(set1 & set2)) - 1])

coincid(skills, job_skills) """

""" start whit list comprhesion """

""" cubes = [i**3 for i in range(5)]

print(cubes)

evens = [i**2 for i in range(20) if i**2 % 2 == 0]

print(evens) """

""" create a list of multiples of 3 from 0 to 20 """

""" multiples3 = [i for i in range(20) if i %3 == 0]

print(multiples3) """

""" exercises counter of letter using dictionaries """

'''text = input()
dict = {}
#tu código va aquí
for i in text:
    if i not in dict:
        dict[i] = 1
    else:
        dict[i] += 1     
print(dict) '''

'''-----------------------------------------'''


'''functional programing in python'''

'''def apply_twice(func, arg):
    return func(func(arg))

def add_five(x):
    return x + 5

print(apply_twice(add_five, 10))'''


#lambdas

def my_func(f, arg):
    return f(arg)

my_func(lambda x: 2*x*x, 5)

#name function
def polynomial(x):
    return x**x + 5*x + 4
print(polynomial(-4))

#lambda
print((lambda x: x**2 + 5*x +4) (-4))

#solving a wrongs lambda
price = int(input())
perc = int(input())

res = (lambda x,y:x*(y / 100))(price, perc)

print(res)


#functional programing: map and filter

def add_five(x):
    return x + 5

nums = [11, 22, 33, 44, 55]
result = list(map(add_five, nums))
print(result)

#exercises code coach map

salaries = [2000, 1800, 3100, 4400, 1500]
bonus = int(input())

print(list(map(lambda x: x + bonus, salaries )))

#filter

nums = [11, 22, 33, 44, 55]
res = list(filter(lambda x: x%2==0, nums))
print(res)

#generators

def countdown():
    i=5
    while i > 0:
        yield i
        i -= 1

for i in countdown():
    print(i)


#Decorators
""" def decor(func):
    def wrap():
        print("============")
        func()
        print("============")
    return wrap

def print_text():
    print("Hello world!")

decorated = decor(print_text)
decorated() """

""" def decor(func):
    def wrap():
        print("============")
        func()
        print("============")
    return wrap

@decor
def print_text():
    print("Hello world!")

print_text(); """


