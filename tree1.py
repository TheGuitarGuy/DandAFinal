#Node class taken from tutorialspoint.com
class Node:
   def __init__(self, data):
      self.left = None
      self.right = None
      self.data = data
   def insert(self, data):
      if self.data:
         if data < self.data:
            if self.left is None:
               self.left = Node(data)
            else:
               self.left.insert(data)
         else:
            if self.right is None:
               self.right = Node(data)
            else:
               self.right.insert(data)
      else:
         self.data = data
   def PrintTree(self):
      if self.left:
         self.left.PrintTree()
      print( self.data),
      if self.right:
         self.right.PrintTree()
   def traverse(self, root):
      res = []
      if root:
         res = self.traverse(root.left)
         res.append(root.data)
         res = res + self.traverse(root.right)
      return res
root = Node(27)
root.insert(12)
root.insert(10)
root.insert(16)
root.insert(17)
root.insert(37)
root.insert(56)
print(root.traverse(root))  