# Define a function that takes length and width as parameters
def calculate_rectangle_area(length, width):
    # Calculate the area by multiplying length by width
    area = length * width
    
    # Return the calculated area back to where the function was called
    return area

# Call the function and store the returned value in a new variable
my_rectangle_area = calculate_rectangle_area(5, 8)

# Now we can print the stored result
print("The area of the rectangle is:", my_rectangle_area)
