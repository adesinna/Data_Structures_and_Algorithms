# A function that will reverse any string

string = "I am Adesina"

def reverse(strings: str):
    list_string = list(strings)[: : -1]

    return "".join(list_string)

print(reverse(string))

# Time and Space complexity of O(n)
