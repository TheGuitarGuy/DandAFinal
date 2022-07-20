# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.next = None
# class LinkedList:
#     def __init__(self):
#         self.head = None

# # Adding nodes in Python

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
class LinkedList:
    def __init__(self):
        self.head = None
first_item = Node("First")
second_item = Node("Second")
third_item = Node("Third")

#Creating the linked list
the_list = LinkedList()
the_list.head = first_item
first_item.next = second_item
second_item.next = third_item
node = the_list.head
#prints first node data

while node is not None:
    print(node.data)
    node = node.next



