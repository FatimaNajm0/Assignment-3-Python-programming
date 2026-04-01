# Set the number we want to generate the table for
number = 5

# Print a clear title for the output
print("Multiplication Table for:", number)
print("-" * 25)

# Use a for loop to multiply the number by 1 through 10
# range(1, 11) generates numbers from 1 up to 10 (it stops before 11)
for i in range(1, 11):
    # Calculate the multiplication result
    result = number * i
    
    # Print the formatted equation (e.g., 5 x 1 = 5)
    # The 'f' before the string allows us to put variables directly inside {}
    print(f"{number} x {i} = {result}")
