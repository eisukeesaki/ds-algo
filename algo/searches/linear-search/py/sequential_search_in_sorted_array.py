def get_index_of_target_in_sorted_array(arr, target):
    i = 0
    while i < len(arr) and arr[i] <= target:
        if arr[i] == target:
            return i
        i += 1

arr = [1,20,36,42,51]
target = 42
index_of_target = get_index_of_target_in_sorted_array(arr, target)
print(index_of_target)

