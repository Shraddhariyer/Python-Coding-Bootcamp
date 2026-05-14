#to make a journal where user can store data, append it, read it and save it


#write function
def write_journal():
    print("NEW JOURNAL ENTRY:\n")
    title=input("Enter title:")
    data=input("Enter today's content:")
    with open(journal_file,"a") as file:
        file.write("Title:"+title+"\n")
        file.write(data+"\n")
    print("Content added successfully!")

#read function
def read_journal():
    print("YOUR CONTENT:\n")
    with open(journal_file,"r") as file:
        content=file.read()
        print(content)
    
#search by keyword
def search_keyword():
    print("Search by keyword")
    keyword=input("Enter a keyword:").lower()
    with open(journal_file,"r") as file:
        content=file.read()
    if keyword in content.lower():
        print("Keyword Found!")
    else:
        print("Keyword not found!!")

#main function
journal_file="day6\\files\\journal.txt"
while True:
    print("\nYOUR JOURNAL\n")
    print("Choose the operation you want to perform:")
    print("1. Write Journal")
    print("2. Read Journal")
    print("3. Search Keyword in Journal")
    print("4. Exit")
    choice=int(input("Enter your Choice[1-4]:"))
    if choice==1:
        write_journal()
    elif choice==2:
        read_journal()
    elif choice==3:
        search_keyword()
    elif choice==4:
        print("Exiting")
        break
    else:
        print("Invalid choice")
    