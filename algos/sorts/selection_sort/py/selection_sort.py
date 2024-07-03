import random
import time

def selection_sort(arr: list[int]) -> None:
    for unsorted_start in range(len(arr) - 1):
        min = unsorted_start
        for i in range(unsorted_start + 1, len(arr)):
            if arr[i] < arr[min]:
                min = i
        arr[unsorted_start], arr[min] = arr[min], arr[unsorted_start]

if __name__ == '__main__':
    l = [random.randint(0, 999) for _ in range(1000)]

    start_time = time.time()
    selection_sort(l)
    end_time = time.time()

    is_sorted = all(l[i] <= l[i+1] for i in range(len(l)-1))
    if is_sorted:
        exec_time = (end_time - start_time) * 1000
        print(f'execution time: {exec_time:.1f}ms')
    else:
        print('list not sorted in ascending order')

