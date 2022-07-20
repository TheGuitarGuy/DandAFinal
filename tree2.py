class Node: 
    def __init__(self, key): 
        self.key = key
        self.left = None
        self.right = None
         
def sumBinaryTree(root): 
    #this handles case of tree not being populated
    if (root == None):
        return 0
    else:

        return (root.key + sumBinaryTree(root.left) +
                       sumBinaryTree(root.right)) 
def main():
    root = Node(1) 
    root.left = Node(2) 
    root.right = Node(3) 
    root.left.left = Node(4) 
    root.left.right = Node(5) 
    root.right.right = Node(7)
    sum = sumBinaryTree(root) 
 
    print(sum)
main()