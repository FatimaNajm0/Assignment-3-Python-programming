# Prompt the user to enter a password
password = input("Please enter your password: ")

# Initialize boolean flags for each criterion
# We start by assuming all conditions are False
is_long_enough = False
has_uppercase = False
has_lowercase = False
has_digit = False

# 1. Check if the password is at least 8 characters long
if len(password) >= 8:
    is_long_enough = True

# 2 & 3. Loop through each character in the password to check for types
for char in password:
    if char.isupper():
        has_uppercase = True
    elif char.islower():
        has_lowercase = True
    elif char.isdigit():
        has_digit = True

# Finally, check if all criteria flags have turned to True
if is_long_enough and has_uppercase and has_lowercase and has_digit:
    print("Success: Password is valid and strong!")
else:
    print("Error: Password does not meet all the criteria.")
