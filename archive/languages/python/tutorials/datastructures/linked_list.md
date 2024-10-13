# Implementing a Linked List in Python

A linked list is a linear data structure where each element is a separate object, called a node. Each node contains two components: data and a reference (or link) to the next node in the sequence. This structure allows for efficient insertion and deletion of elements.

## Components of a Linked List

- **Node**: The building block of a linked list, containing data and a reference to the next node.
- **LinkedList**: A class that manages the nodes, providing methods to manipulate the list.

## Implementing a Node Class

The `Node` class represents each node in the linked list.

```python
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
```

### Example

```python
node1 = Node(5)
node2 = Node(10)
node1.next = node2

print(node1.data)  # Output: 5
print(node1.next.data)  # Output: 10
```

## Implementing a LinkedList Class

The `LinkedList` class manages the nodes and provides methods to manipulate the linked list.

### Basic Methods

- `__init__`: Initializes an empty linked list.
- `append`: Adds a new node at the end of the list.
- `prepend`: Adds a new node at the beginning of the list.
- `insert_after_node`: Inserts a new node after a given node.
- `delete_node`: Deletes a node with a specific value.
- `print_list`: Prints the entire linked list.

```python
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

    def insert_after_node(self, prev_node, data):
        if not prev_node:
            print("Previous node must be in the list.")
            return
        new_node = Node(data)
        new_node.next = prev_node.next
        prev_node.next = new_node

    def delete_node(self, key):
        current_node = self.head
        if current_node and current_node.data == key:
            self.head = current_node.next
            current_node = None
            return
        prev = None
        while current_node and current_node.data != key:
            prev = current_node
            current_node = current_node.next
        if current_node is None:
            return
        prev.next = current_node.next
        current_node = None

    def print_list(self):
        current_node = self.head
        while current_node:
            print(current_node.data)
            current_node = current_node.next
```

### Example Usage

```python
llist = LinkedList()
llist.append(1)
llist.append(2)
llist.append(3)

llist.prepend(0)

llist.insert_after_node(llist.head.next, 1.5)

llist.print_list()
# Output:
# 0
# 1
# 1.5
# 2
# 3

llist.delete_node(1.5)
llist.print_list()
# Output:
# 0
# 1
# 2
# 3
```

## Conclusion

Implementing a linked list in Python provides an excellent understanding of fundamental data structures. The `Node` class represents each element in the list, while the `LinkedList` class provides methods to manipulate the list, including appending, prepending, inserting, deleting, and printing nodes. This implementation can be extended with additional features such as reversing the list, finding the length, and more.