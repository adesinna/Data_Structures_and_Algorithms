def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1


x = linear_search(list(range(1, 101)), 129)


print(x)