#creating a string
word="Hello"
print(word)
#indexing
print(word[0])
print(word[-1])
print(word[2])
print(word[3])
print(word[-1])
#slicing
a="Welcome to Python Bootcamp"
print(a[0:7])
print(a[8:10])
print(a[:7])
print(a[11:])
print(a[::3])#steps in slicing
print(a[::-1])

#looping
for char in a:
    print(char)

#length of string
print(len(a))

#Concatenate
print(word+", "+a)

#string repeat
print(word*3)

#upper() and lower ()
print(word.upper())
print(word.lower())

#strip
b="       Rahul    "
print(b)
print(b.strip())

#split
c=a.split()
print(c)

#replace
sentence=a.replace("Python","Coding")
print(sentence)
print(a)

#count
x=sentence.count("o")
print(x)

#startwith() endwith()
y=sentence.endswith("p")
print(y)

#function chaining
p="   Rahul   "
q=p.strip().upper()
print(q)

#f-string  
name=input("Enter your name:")
age=int(input("Enter your age:"))
print("My name is{name} ",name,"and I'm ",age,"year old.")
print(f"My name is {name} and I'm {age+5} year old.")