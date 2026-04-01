# Define a sample set of numbers
my_set = {15, 42, 8, 99, 23, 7}

# Initialize a variable to store the largest number
# We use None because sets are unordered and cannot be indexed
largest_num = None

# Iterate through each number in the set using a for loop
for num in my_set:
    # If it's the first number we check, or if the current number is greater than largest_num
    if largest_num is None or num > largest_num:
        # Update largest_num with the new higher value
        largest_num = num

# Output the final result
print("The largest number in the set is:", largest_num)
