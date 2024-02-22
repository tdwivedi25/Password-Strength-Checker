import re

password = input("Enter your password: ")

def password_check(password):
    #Checking if password has at least 8 characters
    if len(password) < 8:
        return False
    
    #Checking if password contains at least 1 uppercase letter
    if not re.search(r'[A-Z]', password):
        return False
    
    #Checking if password contains at least 1 lowercase letter
    if not re.search(r'[a-z]', password):
        return False
    
    #Check if password contains at least 1 digit
    if not re.search(r'\d', password):
        return False
    
    #Check if the password contains at least 1 special character
    if not re.search(r'[!@#$%^&*(),.?"/~<>|]', password):
        return False
    
    else:
        return True

validity = password_check(password)

if validity:
    print("Valid Password")

else:
    print("Password does not meet the requirements")