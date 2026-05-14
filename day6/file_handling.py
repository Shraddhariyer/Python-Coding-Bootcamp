#creating and opening file
file=open("notes.txt","w")
file.write("Hello, Welcome to Python Coding Bootcamp. ")
file.close()

#reading & writing mode
file=open("notes.txt","r")
data=file.read()
print(data)
file.close()

#appending mode
file=open("notes.txt","a")
file.write("This is Day 6")
file.close()

#write + read()
file=open("notes.txt","r+")
print(file.read)
file.write("\nToday we are learning Strings and File handling..")
file.close()


#with open()
with open("demo.txt","w") as file:
    file.write("Hello this is a demo file. This file closes authomatically once code is executed.")
    file.write("\nHello Everyone.")

#reading function
#readline
with open("demo.txt","r") as file:
    line1=file.readline()
    print(line1)
    line2=file.readline()
    print(line2)

#readlines
with open("demo.txt","r") as file:
    lines=file.readlines()
    print(lines)

#writelines
list=["Apple","Banana","Grapes"]
with open("fruits.txt","w") as file:
    line=file.writelines(list)
    print(line)