'''1) Escribe un programa muestre por pantalla “Hello World”.'''

'''print('Hello World')'''

'''2) Escribe un programa que escriba en la pantalla el resultado de sumar 3 + 5.'''

'''print(3+5)'''

'''3) Escribe un programa que pida el nombre del usuario y escriba un texto que
diga “Hola nombreUsuario”'''

'''user = input('Ingrese su nombre de usuario: ')
print('Hola', user)'''

'''4) Escribe un programa que pida un número, pida otro número y escriba el
resultado de sumar estos dos números.'''

'''num1 = int(input('Ingrese un numero: '))
num2 = int(input('Ingrese un otro numero: '))
print(num1 + num2)'''


'''5) Escribe un programa que pida dos números y escriba en la pantalla cual es el
mayor.'''

'''num1 = int(input('ingrese un numero: '))
num2 = int(input('ingrese un otro numero: '))
if num1 > num2:
    print(num1)
else:
    print(num2)'''

'''6) Escribe un programa que pida 3 números y escriba en la pantalla el mayor de
los tres.'''
'''num1 = int(input('insert the first number'))
num2 = int(input('insert the second number'))
num3 = int(input('insert the third number'))

if num1 > num2 and num1 > num3:
    print(num1)
elif num2 > num1 and num2 > num3:
    print(num2)
else:
    print(num3)'''


'''7) Escribe un programa que pida un número y diga si es divisible por 2'''

'''num = int(input('insert a number'))
if num % 2 == 0:
    print('is divisible by two')
else:
    print('is not divisible by two')'''


'''8) Escribe un programa que pida un número y nos diga si es divisible por 2, 3, 5 o
7 (sólo hay que comprobar si lo es por uno de los cuatro)'''

num = int(input('insert a number'))
if num % 2 == 0 or num % 3 == 0 or num % 5 == 0 or num % 2 == 7:
    print('is divisible')

'''9) Añadir al ejercicio anterior que nos diga por cuál de los cuatro es divisible (hay
que decir todos por los que es divisible)'''
num = int(input('insert a number'))



'''10) Escribir un programa que escriba en pantalla los divisores de un número dado'''

'''11) Escribir un programa que nos diga si un número dado es primo (no es divisible
por ninguno otro número que no sea él mismo o la unidad)'''

'''12) Pide una nota (número). Muestra la calificación según la nota:
 0-3: Muy deficiente
 3-5: Insuficiente
 5-6: Suficiente
 6-7: Bien
 7-9: Notable
 9-10: Sobresaliente'''

'''13) Realiza un programa que escriba una pirámide del 1 al 30 de la siguiente
forma:
1
22
333
4444'''
'''14) Haz un programa que escriba una pirámide inversa de los números del 1 al
número que indique el usuario de la siguiente forma (suponiendo que indica 6):
666666
55555
4444
333
22
1'''
'''15) Crear un programa que escriba los números del 1 al 500, y que indique cuales
son múltiplos de 4 y de 9 y que cada 5 líneas muestre una línea horizontal. Por
ejemplo:
1
2
3
4 (Múltiplo de 4)
5
------------------------------------------------------------
6
7
8 (Múltiplo de 4)
9 (Múltiplo de 9)
10'''