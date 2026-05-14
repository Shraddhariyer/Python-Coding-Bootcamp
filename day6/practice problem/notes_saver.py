#input notes from user and save it in a file
note=input("Enter your notes to save permanently:\n")

#write function
with open("user_notes.txt","a") as file:
    file.write(f"{note}\n")

#read function
print("YOUR SAVED NOTE:\n")
with open("user_notes.txt","r") as file:
    print(file.read())