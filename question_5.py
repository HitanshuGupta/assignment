def compare_lists(list1, list2):
    common_elements = list(set(list1) & set(list2))
    non_common_elements = list(set(list1) ^ set(list2))
    return common_elements, non_common_elements

# Take input from the user
mainstream = input("Enter the elements of the mainstream list, separated by commas: ").split(",")
must_watch = input("Enter the elements of the must_watch list, separated by commas: ").split(",")

common, non_common = compare_lists(mainstream, must_watch)
print("Common elements:", common)
print("Non-common elements:", non_common)
