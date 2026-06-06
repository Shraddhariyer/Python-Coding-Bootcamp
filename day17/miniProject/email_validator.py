#To validate the email given by user

def validate_email(email):
    if "@" not in email:
        return False
    
    if "." not in email:
        return False
    
    username,domain=email.split("@")
    #test@gmail.com

    if username=="":
        return False
    
    if domain=="":
        return False
    
    if domain.startswith("."):
        return False
    

    return True


if __name__=="__main__":
    email=input("Enter email:")
    if validate_email(email):
        print("Valid")
    else:
        print("Invalid")
