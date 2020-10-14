input_arr = [0, 11, 5, 12, 1, 2, 9, 3, 13, 14, 4, 6, 7, 8, 10]


def merge_sort(arr):
    if len(arr) < 2:
        return arr

    middle = len(arr) // 2
    left = arr[:middle]
    right = arr[middle:]
    merge_sort(left)
    merge_sort(right)

    i, j = 0, 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            arr[i+j] = left[i]
            i += 1
        else:
            arr[i+j] = right[j]
            j += 1

    while i < len(left):
        arr[i+j] = left[i]
        i += 1
    while j < len(right):
        arr[i+j] = right[j]
        j += 1

    return arr


print(merge_sort(input_arr))
