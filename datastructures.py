#exercise how many vowels
word = str("hellou")
vowels = ["a","e","i","o", "u"]
length = len([i for i in word if i in vowels])
print(length) 
