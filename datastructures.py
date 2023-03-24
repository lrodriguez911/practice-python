import math
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

""" data = [[23, 11, 5, 14], 
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
    print(int((result / total)* 100 )) """

#elegants houses
""" prices = [125000, 78000, 110000, 65000, 300000, 250000, 210000, 150000, 165000, 140000, 125000, 85000, 90000, 128000, 230000, 225000, 100000, 300000] """
#tu código va aquí
""" print(sum(prices) / len(prices))
result = [i for i in prices if i > (sum(prices) / len(prices))]
print(len(result)) """
#exercises list methods
""" x = [8, 5, 42, 11, 20, 4]
x.sort()
print(max(x)-min(x)+x[2]) """


#pest control
""" c = 10
N = 12
print([N*2**i for i in range(12)])
 """


# using dictionaries

""" nums = {
    1: "one",
    2: "two",
    3: "three"
}
print(1 in nums)
print('two' in nums)
print('two' not in nums) """


""" pairs = {
    1: "apple",
    "orange": [2,3,4],
    True: False,
    12 : "True"
}

print(pairs.get(1))
print(pairs.get("orange"))

print(pairs.get(7,42))
print(pairs.get(12345, "not found")) """

#Exercises Fuzzy Search

""" contacts = {
    "David": ["123-321-88","david@test.com"],
    "James": ["241-873-093","james@test.com"],
    "Bob": ["987-004-322","bob@test.com"],
    "Amy": ["340-999-213","a@test.com"]
}

contact = input()
if contact in contacts:
    print(contacts.get(contact)[1])
else:
    print("Not found") """


#tuples
""" words = ("spam", "eggs", "sausages")
print(words[0]) """

#diferents data structures
#list 
# list = ["one", "two"]
# dictionary
# dict =  {1: "one", 2: "two"}
#tuple
#tup = ("one", "two")

""" dict = {
    ("David", 42): "red",
    ("Bob", 24): "green"
}

print(dict[("David", 42)])
print(dict[("Bob", 24)]) """

#tuple unpacking

""" numbers = (1,2,3)
a, b, c = numbers
print(a)
print(b)
print(c) """


#Exercises Mapping
""" points = [
    (12, 55),
    (880, 123),
    (64, 64),
    (190, 1024),
    (77, 33),
    (42, 11),
    (0, 90)
]
list = []
for i in points:
    x, y = i
    list.append(math.sqrt(pow(x, 2)+ pow(y, 2)))

list.sort()
print(list[0])

print(list) """

""" a,b,c,d, *e,f,g = range(20)

print(len(e)) """

#Sets

""" num_set = {1, 2, 3, 4, 5}
print(3 in num_set) 

letters = {"a", "b", "c", "d"}
if "e" not in letters:
    print(1)
else:
    print(2) """


""" nums = {1,2,1,3,1,4,5,6}
print(nums)
nums.add(-7)
nums.remove(3)
print(nums) """

""" first = {1,2,3,4,5,6}
second = {4,5,6,7,8,9}

print(first | second)
print(first & second)
print(first - second)
print(second - first)
print(first ^ second)
 """

#exewrcises words in common
""" s1 = "this is some text"
s2 = "I would like this tea some cookies"

set1 = set(s1.split())
set2 = set(s2.split())
print(len(set1 & set2)) """


# Stack

""" class Stack:
    def __init__(self):
        self.items = []  
  
    def is_empty(self):
        return self.items == []
  
    def push(self, item):
        self.items.insert(0, item)
    
    def pop(self):
        return self.items.pop(0)
    
    def print_stack(self):
        print(self.items)
    
s = Stack()
s.push('a')
s.push('b')
s.push('c')
s.print_stack()

s.pop()
s.print_stack() """

#exercise with stack
#come back

class Browser:
    def __init__(self):
      self.links = []  
  
    def is_empty(self):
      return self.links == []
  
    def push(self, link):
      self.links.insert(0, link)
    def pop(self):
      return self.links.pop(0)
    
  
x = Browser()
x.push('about:blank')
x.push('www.sololearn.com')
x.push('www.sololearn.com/courses/')
x.push('www.sololearn.com/courses/python/')

while not x.is_empty():
    print(x.pop())


#Queue

class Queue:
    def __init__(self):
      self.items = []

    def is_empty(self):
      return self.items == []
    
    def enqueue(self, item):
       self.items.insert(0, item)

    def dequeue(self):
       return self.items.pop()
    
    def print_queue(self):
       print(self.items)
   

#Linked List

class Node:
    def __init__(self, data, next):
       self.data = data
       self.next = next

class LinkedList:
    def __init__(self):
       self.head = None
    
    def add_at_front(self, data):
        self.head = Node(data, self.head)
    
    def add_at_end(self, data):
        if not self.head:
            self.head = Node(data, None)
            return
        curr = self.head
        while curr.next:
            curr = curr.next
        curr.next = Node(data, None)
    
    def get_last_node(self):
        n = self.head
        while (n.next != None):
            n = n.next
        return n.data

    def is_empty(self):
        return self.head == None
    
    def print_list(self):
        n = self.head
        while n != None:
            print(n.data, end=" => ")
            n = n.next
        print()

s = LinkedList()
s.add_at_front(5)
s.add_at_end(8)
s.add_at_front(9)

s.print_list()
print(s.get_last_node())

            
# Exercises Name that tune

class Track:
    def __init__(self, title, next):
        self.title = title
        self.next = next

class Player:
    def __init__(self):
        self.head = None

    def add(self, title):
        if not self.head:
            self.head = Track(title, None)
            return
        curr = self.head
        while curr.next:
            curr = curr.next
        curr.next = Track(title, None)


p = Player()
""" while True:
    x = input()
    if x == 'end':
        break
    p.add(x) """

p.add("bib")
p.add("myg")
p.add("lc")
p.add("believe")
#your code goes here
#your code goes here
""" while n != None: """
print(p.head.next.next.next.title)

n = p.head
while n != None:
    print(n.title)
    n = n.next
    
    
# Graph

class Graph():
    def __init__(self, size) -> None:
        self.adj = [ [0] * size for i in range(size)]
        self.size = size
    
    def add_edge(self, orig, dest):
        if orig > self.size or dest > self.size or orig < 0 or dest < 0:
            print("Invalid Edge")
        else:
            self.adj[orig-1][dest-1] = 1
            self.adj[dest-1][orig-1] = 1
    
    def remove_edge(self, orig, dest):
        if orig > self.size or dest > self.size or orig < 0 or dest < 0:
            print("Invalid Edge")
        else:
            self.adj[orig-1][dest-1] = 0
            self.adj[dest-1][orig-1] = 0
    
    def display(self):
        for row in self.adj:
            print()
            for val in row:
                print(f'{val: <4}', end="")
        
G = Graph(4)
G.add_edge(1, 1)
G.add_edge(1, 2)
G.add_edge(1, 3)
G.add_edge(2, 2)
G.add_edge(3, 3)
G.add_edge(4, 4)
G.display()

# Exercises Lets Connect