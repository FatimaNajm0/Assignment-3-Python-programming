# Define a function that takes a number 'n' as a parameter
def calculate_factorial(n):
    # Handle the edge case for negative numbers (factorial is undefined)
    if n < 0:
        return "Factorial does not exist for negative numbers."
    
    # Handle the base case: factorial of 0 is 1
    if n == 0:
        return 1
        
    # Initialize the result variable to 1 
    # We use 1 because multiplying by 0 would make the whole result 0
    result = 1
    
    # Loop from 1 up to 'n' (inclusive)
    for i in range(1, n + 1):
        # Multiply the current result by the loop variable 'i'
        result = result * i
        
    # Return the final calculated factorial
    return result

# Test the function with a number
my_number = 5
fact_result = calculate_factorial(my_number)

# Print the returned result
print(f"The factorial of {my_number} is: {fact_result}")
