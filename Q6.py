# Define two lists to compare
list1 = [10, 25, 30, 45, 50, 60]
list2 = [15, 25, 35, 45, 55, 60]

# Create an empty list to store the common elements
common_elements = []

# Use zip() to pair elements from both lists at the same index
# item1 gets the value from list1, and item2 gets the value from list2
for item1, item2 in zip(list1, list2):
    # Check if the paired elements are exactly the same
    if item1 == item2:
        # If they match, add the element to our new list
        common_elements.append(item1)

# Print the final result
print("List 1:", list1)
print("List 2:", list2)
print("Common elements at the same positions:", common_elements)
