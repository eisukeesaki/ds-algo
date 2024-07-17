def insertion_sort(a: list[int]) -> None:
    i = 1
    while i < len(a):
        v = a[i]
        k = i
        while k > 0 and a[k - 1] > v:
            a[k] = a[k - 1]
            k -= 1
        a[k] = v
        i += 1

# def insertion_sort(a: list[int]) -> None:
#     for i in range(1, len(a)):
#         v = a[i]
#         while i > 0 and a[i - 1] > v:
#             a[i] = a[i - 1]
#             i -= 1
#         a[i] = v

if __name__ == '__main__':
    data = [2, 1, 6, 4, 5, 0]
    insertion_sort(data)
    print(data)

