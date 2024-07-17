def get_index_of_target_in_unsorted_array(array, target):
    i = 0
    while i < len(array):
        if arr[i] == target:
            return i
        i += 1
    # for i in range(len(arr)):
    #     if arr[i] == target:
    #         return i

arr = [1, 8, 3, 9, 0, 42, 24]
to_find = arr[5]
index = get_index_of_target_in_unsorted_array(arr, to_find)
print(index)
