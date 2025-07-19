def constant_time_example(data):
    """
    A function with O(1) time complexity - constant time.

    Args:
        data: A list of elements

    Returns:
        The first element of the list (access is O(1) in Python lists)
    """
    if len(data) > 0:
        return data[0]
    else:
        return None


# Example usage:
numbers = []
print(constant_time_example(numbers))  # Output: 1 (takes same time even if list has 1M elements)