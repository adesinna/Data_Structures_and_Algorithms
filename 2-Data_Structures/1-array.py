new_list = [1, 3, 5]

new_list.append(4) # O(1) for space


new_list.insert(0, 8)   # O(n) for space

new_list.extend([2, 4])  # O(k) where n is the number of element

new_list.pop(0)

print(new_list)

my_list = [1, 2, 3]
my_list.insert(1, 99)  # Insert 99 at index 1 → [1, 99, 2, 3]
my_list.pop(1)         # Remove item at index 1 → [1, 2, 3]