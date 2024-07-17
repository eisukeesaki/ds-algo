def binarySearch (first, last):
    if first > last:
        return False
    else:
        middle = (first + last)/ 2
        if item == data[middle]:
            return True
        else:
            if item < data[middle]:
                return binarySearch (first, middle – 1)
            else:
                return binarySearch (middle + 1, last)

