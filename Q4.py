# Define a list that contains duplicate numbers
original_list = [10, 20, 10, 30, 40, 20, 50, 30]

# Create an empty list to store the unique items
unique_list = []

# Loop through each item in the original list
for item in original_list:
    # Check if the current item is NOT already in our new list
    if item not in unique_list:
        # If it's a new item, append (add) it to the unique_list
        unique_list.append(item)

# Print both lists to see the difference
print("Original list:", original_list)
print("List after removing duplicates:", unique_list)
