# Define a function that takes a list of numbers as a parameter
def print_largest_number(numbers_list):
    # It's a good practice to check if the list is empty first
    if len(numbers_list) == 0:
        print("The list is empty!")
        return

    # Assume the first number in the list is the largest initially
    largest = numbers_list[0]

    # Loop through each number in the list
    for num in numbers_list:
        # If the current number is greater than our assumed largest
        if num > largest:
            # Update 'largest' with this new higher value
            largest = num

    # Print the final result
    print("The largest number in the list is:", largest)

# Define a sample list of numbers
my_list = [24, 76, 12, 99, 5, 42]

# Call the function and pass the list to it
print_largest_number(my_list)
