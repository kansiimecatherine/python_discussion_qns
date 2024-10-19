
#Question 4(i)
# Create a list of five of your favorite foods. Write a Python program to:
# Add two more items to the list.
# Remove one item from the list.
# Print the updated list.
# Initial list of favorite foods

# favorite_food_list = ["Pizza", "eggs", "Chocolate", "capatti", "irish"]
# favorite_food_list.append("chicken")#use append to add something to the list
# favorite_food_list.append("Fish")
# favorite_food_list.remove("Chocolate")
# print(f"Updated list of favorite foods: {favorite_food_list}")



#Question 4(ii)
# Given the list numbers = [2, 5, 8, 10, 3, 6], write a Python program to:
# Print the first and last elements of the list.
# Print the list in reverse order.
# Calculate and print the sum of all the elements in the list.
# Given list of numbers
numbers = [2, 5, 8, 10, 3, 6]

# Print the first and last elements of the list
first_element = numbers[0] #positive indexing(left to right)
last_element = numbers[-1] #negative indexing(right to left)
print("The first element:", first_element)
print("The last element:", last_element)

# Print the list in reverse order
# reversed_list = numbers[::-1]
# print("List in reverse order:", reversed_list)
numbers.reverse()
print(f"The reverse order of the list is : {numbers}")


total_sum = sum(numbers)
print("The Sum of all elements is:", total_sum)
