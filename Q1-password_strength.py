def check_password_strength(password):
    # Checking minimum password string length
    if len(password) < 8:
        return False

    #Defining flags to false
    has_upper = False
    has_lower = False
    has_digit = False
    has_special = False

    #Allowed special characters
    special_characters = "!@#$%^&*(),.?\":{}|<>"

    for char in password:
        #checking password has uppercase
        if char.isupper():
            has_upper = True
        #checking password has lowercase
        elif char.islower():
            has_lower = True
        #checking password has numbers
        elif char.isdigit():
            has_digit = True
        #checking password has special characters
        elif char in special_characters:
            has_special = True

    #If all conditions true then return True
    if has_upper and has_lower and has_digit and has_special:
        return True
    else:
        return False

if __name__ == "__main__":
    user_password = input("Enter your password: ")#collecting information from user

    if check_password_strength(user_password):#check the return value true by calling check_password_strength function with the input string
        print("Password is strong.")
    else:
        print("Password is weak. It must be at least eight characters long & include upperCase, lowerCase, a digit, and a special character.")