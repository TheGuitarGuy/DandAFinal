class Node: 
    def __init__(self, value): 
        self.value = value
        self.left = None
        self.right = None
         
def findMin(root): 
    current_node = root
    if current_node.left == None:
        return current_node.value
    return findMin(current_node.left)

def main():
    root = Node(7) 
    root.left = Node(6) 
    root.right = Node(8) 
    root.left.left = Node(3) 
    root.left.right = Node(7) 
    root.left.left = Node(2)
    print(findMin(root))
main()