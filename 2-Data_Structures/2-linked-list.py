class Node:
    data = None
    next_node = None

    def __init__(self, data):
        self.data = data

    def __repr__(self):
        return "<Node data: %s>" % self.data


class LinkedList:

    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head == None

    def size(self):
        """
        This will take a linear time of O(n)
        :return:
        """
        count = 0
        current = self.head

        while current:
            count += 1
            current = current.next_node

        return count

