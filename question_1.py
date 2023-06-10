'''
Get your basics right - Implement selection sort algorithm in python. The function accepts a
list in the input and returns a sorted list.
E.g.
Input f1([5,416,54,21,6135,15,741]) should
Return [5, 15, 21, 54, 416, 741, 6135]
'''
# Selection sort function
def selection_sort(arr):
    for i in range(0,len(arr)-1):
        for j in range(i+1, len(arr)):
            if arr[i]>arr[j]:
                temp = arr[i]
                arr[i] = arr[j]
                arr[j] = temp
    return arr
                
input_list = input("Enter a list of numbers (separated by spaces): ").split()
input_list = [int(num) for num in input_list]

# Call the selection_sort function
sorted_list = selection_sort(input_list)
print("Sorted List:", sorted_list)