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
