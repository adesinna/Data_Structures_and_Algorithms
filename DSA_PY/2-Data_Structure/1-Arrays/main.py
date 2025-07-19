strings = ['a', 'b', 'c', 'd']

# The question is how is this list stored in memory, py stores a list with pointers to where each element are in the
# memory, the list would have some metadata like length. It always over provision memory because, if the memory is not
# enough it will copy the list to another block in memory with a larger space, which rarely happens.


# Append
strings.append('e')
print(strings)

# The time complexity of this is O(1) since most time there is extra space, worst case it can be O(n)
# The space complexity is also O(1) since there is most likely extra space, worst case it reallocates the list to a
# larger one which is O(n) and it is very rare

#
# | Operation   | Time Complexity                   | Space Complexity                    |
# | ----------- | --------------------------------- | ----------------------------------- |
# | `append()`  | O(1) amortized but O(n) worst case | O(1) normally but O(n) when resizing |
# | List Growth | Happens at geometric intervals    | Over-allocates \~25-50%             |


# pop
strings.pop()  # This removes the last elements of the list
print(strings)

# The time complexity is O(1) since it does not need to loop through the list to do this, it just removes the last
# elements but for the space complexity is also O(1) since it does not need create any additional space.

strings.pop(0)
print(strings)

# when there is string.pop(i), it pops out i and shift all elements on the left one time, so there is (n-i) number of
# operations required to do that, so the time complexity is O(n), that is linear to do for any pop(i).
# On the other hand, no additional space is used to we have O(1)


# insert
strings.insert(0, 'z')
print(strings)   # space complexity of O(1) since no additional space is needed

# time complexity of O(n) since it has to shift the elements n times and to accommodate the 'z'
# the space complexity is O(1) there is likely extra space


# del
del strings[3]
print(strings)

# time complexity of O(n) since it has to shift the elements n times when deleted

# space complexity is O(1) since no additional space


# Slicing a list

lst = ['a', 'b', 'c', 'd', 'e']
new_lst = lst[1:4]  # ['b', 'c', 'd']

# the time complexity would be O(k) which is linear, it would copy all the element in the slice and give it its own
# space, which makes but time and space O(n). But no so in numpy arrays
