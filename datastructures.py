#exercise how many vowels
""" word = str("hellou")
vowels = ["a","e","i","o", "u"]
length = len([i for i in word if i in vowels])
print(length)  """

#exercise align them
""" str = "data"
i = 1
for l in str:
    print(l * i) 
    i+=1 """

#Exercise Guide to edition
""" str1 = "kilograms"
str2 = "kg"

str3 = "I weigh 80 kilograms. He weighs 65 kilograms"

print(str3.count("kilograms"))
print(str3.replace(str1, str2)) """

#Test Module 1
#Frecuency of letters

""" text = "hello"
letter = "l"

frecuency = int((text.count(letter)/len(text)) * 100)
 """

 #operartions whit lists
""" words = ["spam","egg","spam","sausage"]
print("spam" in words)
print("egg" in words)
print("tomato" in words) """

""" name = input()
contacts = ["Lucas", "Flor", "Naza"]
if name in contacts:
    print("Found")
else:
    print("Not found") """

#using a loop to traverse list

""" x = [2,4,6,8]

for n in x:
    print(n) """

#list exercises the apple of my eyes

#color orders in brown, blue, green and black

data = [[23, 11, 5, 14], 
[8, 32, 20, 5]]

color = 'blue'
total = sum(data[0]) + sum(data[1])

result = 0
if color == 'brown':
    result = data[0][0] + data[1][0]
    print(int((result / total)* 100 ))
elif color == 'blue':
    result = data[0][1] + data[1][1]
    print(int((result / total)* 100 ))
elif color == 'green':
    result = data[0][2] + data[1][2]
    print(int((result / total)* 100 ))
else:
    result = data[0][3] + data[1][3]
    print(int((result / total)* 100 ))

