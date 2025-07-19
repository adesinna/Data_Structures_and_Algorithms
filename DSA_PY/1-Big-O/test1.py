array1 = ['a', 'b', 'c', '1']

array2 = ['x', 'a', 'y', 'z', 'c']

# Brute force


def brute(arr1: list, arr2: list):
    commons = []

    for i in arr1:
        for j in arr2:
            if (i == j) and (j not in commons):
                commons.append(j)

    if commons:
        print("We have common elements")
        return f"Elements are {commons}"
    else:
        return "No commons"


print(brute(array1, array2))


def optimize(arr1: list, arr2: list):
    set_1 = set(arr1)  # converts the list into the set
    commons = []

    for i in arr2:
        if i in set_1 and i not in commons:
            commons.append(i)

    if commons:
        print(f"the set {commons}")
        return True
    else:
        return False

print(optimize(array1, array2))
