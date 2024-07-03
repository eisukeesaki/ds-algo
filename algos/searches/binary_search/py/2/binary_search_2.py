scope = [1, 3, 5, 8, 9, 10, 23, 39, 46, 59, 68, 70, 80]
target = 68

def binary_search(scope, target):
    found = False
    count = 0
    start = 0
    end = len(scope) - 1
    mid = (end + start) / 2
    while start <= end && found == True:


