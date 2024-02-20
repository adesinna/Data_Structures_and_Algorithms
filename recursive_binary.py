def recursive_binary(arr, target):
    low, high = 0, len(arr) - 1

    if low <= high:
        mid = (low + high) // 2

        if arr[mid] == target:
            return True  # Element found at middle index
        elif arr[mid] < target:
            # If the target is greater, search the right half
            return recursive_binary(arr[mid + 1:], target)
        else:
            # If the target is smaller, search the left half
            return recursive_binary(arr[:mid], target)
    else:
        return False


x = recursive_binary(list(range(6370)), -1)
print(x)

