def get_pairs(array:list):
    for i in range(len(array)):
        for j in range(len(array)):
            print(f"{array[i]}, {array[j]}")

    return "Done"

list_a = list(range(4))

print(get_pairs(list_a))