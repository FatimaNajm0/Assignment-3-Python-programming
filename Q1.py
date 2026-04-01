def count_vowels(text):
    # Initialize the counter to 0
    count = 0
    
    # Convert the string to lowercase to make checking easier
    text = text.lower()
    
    # Loop through each letter in the string
    for letter in text:
        # Check if the letter is a vowel
        if letter == 'a' or letter == 'e' or letter == 'i' or letter == 'o' or letter == 'u':
            count = count + 1  # Increase the counter
            
    # Print the final result
    print("Number of vowels:", count)

# Accept a string from the user
user_string = input("Enter a string: ")

# Call the function
count_vowels(user_string)
