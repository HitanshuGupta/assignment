'''Given a list of dicts, write a program to sort the list according to a key given in input.'''

def sort_list_of_dicts(list_of_dicts, sort_key):
    sorted_list = sorted(list_of_dicts, key=lambda x: x[sort_key])
    return sorted_list

# Take input from the user
list_of_dicts = []
n = int(input("Enter the number of dictionaries: "))
for i in range(n):
    fruit = input("Enter the fruit name: ")
    color = input("Enter the color: ")
    dict_entry = {"fruit": fruit, "color": color}
    list_of_dicts.append(dict_entry)

sort_key = input("Enter the key to sort by (fruit or color): ")

# Call the function
sorted_list = sort_list_of_dicts(list_of_dicts, sort_key)
print(sorted_list)
