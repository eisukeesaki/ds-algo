# import random
# import time

def swap(items, i, k):
    tmp = items[i]
    items[i] = items[k]
    items[k] = tmp

# def bubble_sort(arr: list[int]) -> None:
#     for sorted in range(len(arr)-1):
#         for i in range(len(arr)-1):
#             if arr[i] > arr[i+1]:
#                 arr[i], arr[i+1] = arr[i+1], arr[i]

# def bubble_sort(items):
#     for i in range(len(items)-1):
#         swapped = False
#         for k in range(len(items)-1-i):
#             if items[k] > items[k+1]:
#                 swap(items, k, k+1)
#                 swapped = True
#         if not swapped:
#             break

def bubble_sort(items):
    i = 0
    while i < len(items) - 1:
        swapped = False
        k = 0
        while k < len(items) - 1 - i:
            if items[k] > items[k + 1]:
                swap(items, k, k + 1)
                swapped = True
            k += 1
        if not swapped:
            break
        i += i

l = [395,2,-4,20,47,200,-50,-12]
bubble_sort(l)
print(l)

# if __name__ == '__main__':
#     l = [random.randint(0, 999) for _ in range(1000)]

#     start_time = time.time()
#     bubble_sort(l)
#     end_time = time.time()

#     is_sorted = all(l[i] <= l[i+1] for i in range(len(l)-1))
#     if is_sorted:
#         exec_time = (end_time - start_time) * 1000
#         print(f'execution time: {exec_time:.1f}ms')
#     else:
#         print('list not sorted in ascending order')

