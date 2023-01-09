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

text = "hello"
letter = "l"

frecuency = int((text.count(letter)/len(text)) * 100)
