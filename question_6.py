def get_sublist(lst, start_index, end_index):
    sub_list = lst[start_index:end_index+1:2]
    return sub_list

# Test the function
input_list = input("Enter the list elements separated by spaces: ").split()
input_list = [int(x) for x in input_list]
start_index = int(input("Enter the start index: "))
end_index = int(input("Enter the end index: "))
sub_list = get_sublist(input_list, start_index, end_index)
print(sub_list)
