def linear_time_example(data):
    """
    A function with O(n) time complexity - linear time.

    Args:
        data: A list of elements

    Returns:
        The sum of all elements in the list
    """
    total = 0
    # This loop runs exactly len(data) times
    for item in data:
        total += item
    return total


# Example usage:
numbers = [1, 2, 3, 4, 5, 6]
print(linear_time_example(numbers))  # Output: 15