# Define a function named list_sum that takes a list of numbers as input
def list_sum(num_List):

    # Check if the length of the input list is 1
    if len(num_List) == 1:
        # If the list has only one element, return that element
        return num_List[0]

    else:
        # If the list has more than one element, return the sum of the first element
        # and the result of recursively calling the list_sum function on the rest of the list
        return num_List[0] + list_sum(num_List[1:])

# Print the result of calling the list_sum function with the input [2, 4, 5, 6, 7]
print(list_sum([2, 4, 5, 6, 7]))


# Define a function named recursive_list_sum that calculates the sum of elements in a nested list
def recursive_list_sum(data_list):
    # Initialize a variable 'total' to store the cumulative sum
    total = 0

    # Iterate through each element in the input list
    for element in data_list:
        # Check if the current element is a list (nested list)
        if type(element) == type([]):
            # If the element is a list, recursively call the recursive_list_sum function on the element
            total = total + recursive_list_sum(element)
        else:
            # If the element is not a list, add its value to the total
            total = total + element

    # Return the total sum
    return total


# Print the result of calling the recursive_list_sum function with the input list [1, 2, [3,4], [5,6]]
print(recursive_list_sum([1, 2, [3, 4], [5, 6]]))