# Define a function that takes a string parameter called 'text'
def reverse_string(text):
    # Create an empty string to store the reversed version
    reversed_text = ""
    
    # Loop through each character in the original string
    for char in text:
        # Add the current character to the FRONT of the new string
        # This pushes the older characters to the right, reversing the order
        reversed_text = char + reversed_text
        
    # Return the final reversed string back to the caller
    return reversed_text

# Define a sample string to test
my_word = "Software"

# Call the function and save the returned value in a variable
reversed_word = reverse_string(my_word)

# Print the results to see if it worked
print("Original string:", my_word)
print("Reversed string:", reversed_word)
