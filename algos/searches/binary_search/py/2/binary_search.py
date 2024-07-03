arr = [10, 20, 30, 40, 50, 60, 70, 80, 90]
to_find = 100

def binary_search(scope, target):
    first = 0
    last = len(scope) - 1
    while first <= last:
        middle = int((last + first) / 2)
        if scope[middle] == target:
            return True
        elif scope[middle] < target:
            first = middle + 1
        elif scope[middle] > target:
            last = middle - 1
    return False

result = binary_search(arr, to_find)
print(result)
