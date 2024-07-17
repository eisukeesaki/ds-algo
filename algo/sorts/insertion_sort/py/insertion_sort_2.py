def insertion_sort(data):
    length = len(data)
    current = 1

    while current < length:
        index = current
        place_found = False

        while index > 0 and not place_found:
            if data[index] < data[index - 1]:
                data[index], data[index - 1] = data[index - 1], data[index]
                index -= 1
            else:
                place_found = True

        current += 1

    return data

data = [0, 4, 3, 0, 3, 5, 8]
sorted_data = insertion_sort(data)
print("Sorted array:", sorted_data)

