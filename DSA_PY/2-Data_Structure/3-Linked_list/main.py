class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)

        if not self.head:
            self.head = new_node
            return

        last_node = self.head

        while last_node.next:
            last_node = last_node.next

        last_node.next = new_node

    def prepend(self, data):
        new_node = Node(data)

        new_node.next = self.head
        self.head = new_node

    def insert_after(self, prev_node, data):
        if not prev_node:
            print("The node does not exist")
            return

        new_node = Node(data)

        new_node.next = prev_node.next
        prev_node.next = new_node

    def search(self, key):
        current_node = self.head

        while current_node:
            if current_node.data == key:
                return True
            current_node = current_node.next

        return False

    def count(self):
        current_node = self.head
        count = 0

        while current_node:
            count += 1
            current_node = current_node.next

        return count

    def print(self):
        current_node = self.head

        while current_node:
            print(current_node.data, end="->")
            current_node = current_node.next

        print("None")

    def delete(self, key):
        current_node = self.head

        # if the head holds the key
        if current_node and current_node.data == key:
            self.head = current_node.next
            current_node = None  # garbage collector will delete it automatically
            return

        # search for the key if it is not head
        prev_node = None

        while current_node and current_node.data != key:
            prev_node = current_node
            current_node = current_node.next

        if current_node is None:
            return

        prev_node.next = current_node.next
        current_node = None

    def reverse(self):
        current_node = self.head
        prev_node = None

        while current_node:
            next_node = current_node.next  # Fixed: was next_node
            current_node.next = prev_node
            prev_node = current_node
            current_node = next_node

        self.head = prev_node  # Fixed: Update the head to the new first node