class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
class LinkedList:
    def __init__(self):
        self.head = None
def main():
    first_car = Node(600)
    second_car = Node(700)
    third_car = Node(100)
    fourth_car = Node(800)
    fifth_car = Node(400)
    sixth_car = Node(300)
    seventh_car = Node(200)
    eighth_car = Node(500)

    #Creating the linked list
    the_list = LinkedList()
    the_list.head = first_car
    first_car.next = second_car
    second_car.next = third_car
    third_car.next = fourth_car
    fourth_car.next = fifth_car
    fifth_car.next = sixth_car
    sixth_car.next = seventh_car
    seventh_car.next = eighth_car
    node = the_list.head
    print(find_min_values(node))
#prints first node data
def find_min_values(node):
    min_so_far = 10000
    min = []
    while node.next is not None:
        if node.data + node.next.data <min_so_far:
            min = [node.data, node.next.data]
            min_so_far = node.data + node.next.data
        else:
            node = node.next
    return min
main()
