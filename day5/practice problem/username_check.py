#to check if usernames exists or not
username={"rahul","Rishi"}
user=input("Enter a username:")
if user in username:
    print("Username exists, cannot created this username")
else:
    print("Username created")
    username.add(user)
print(username)
