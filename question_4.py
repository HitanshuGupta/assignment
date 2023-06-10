def switch_keys_values(dictionary):
    return {v: k for k, v in dictionary.items()}

# Take input from the user
input_dict = eval(input("Enter the dictionary: "))

# Test the function
switched_dict = switch_keys_values(input_dict)
print(switched_dict)
