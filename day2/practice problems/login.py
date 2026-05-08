user="admin"
passwd = "admin@123"
username=input("Enter Your Username")
password=input("Enter your password")
if username==user and password==passwd:
    print("Welcome to your account")
elif username==user and password!=passwd:
    print("Invalid Password")
elif username!=user and password==passwd:
    print("User does not exist")
else:
    print("Invalid Creds")