# Define a function that takes username and password as parameters
def check_login(username, password):
    # Simulate a check against saved credentials
    # Let's assume the correct username is 'admin' and password is 'secret123'
    if username == "admin" and password == "secret123":
        # Return True if both match
        return True
    else:
        # Return False if any of them is wrong
        return False

# Prompt the user to enter their credentials
entered_username = input("Please enter your username: ")
entered_password = input("Please enter your password: ")

# Call the function, pass the inputs, and store the returned boolean value
is_valid = check_login(entered_username, entered_password)

# Check the result and inform the user
if is_valid == True:
    print("Login successful! Welcome to the system.")
else:
    print("Login failed! Invalid username or password.")
