# merged two sorted arrays

# merged_sorted([0, 3, 4, 31], [4, 6, 30])
# [0, 3, 4, 4, 6, 30, 31]


def merged_sorted(arr1: list, arr2: list) -> list:
    merged = []
    i = j = 0

    while i < len(arr1) and j < len(arr2):  # this compares the two list and appends the smallest value
        if arr1[i] <= arr2[j]:
            merged.append(arr1[i])
            i += 1                  # increase i by 1

        else:
            merged.append(arr2[j])
            j += 1               # increase j by 1

    while i < len(arr1):
        merged.append(arr1[i])
        i += 1

    while j < len(arr2):
        merged.append(arr2[j])
        j += 1

    return merged
print(merged_sorted([0, 3, 4, 31], [4, 6, 30]))





