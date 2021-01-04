import sys

class Node:
  def __init__(self, data):
    self.data = data
    self.left = None
    self.right = None

class Tree:
  def __init__(self, root_node):
    self.root = root_node

  def insert(self, node, mid, left, right):
    if node.data == mid:
      node.left = Node(left)
      node.right = Node(right)
      return
    
    if node.left == None :
      return
    if node.right == None :
      return

    self.insert(node.left, mid, left, right)
    self.insert(node.right, mid, left, right)
    
    return

  def pre_order(self, node): # root == 'A'
    if node.data != '.' :
      print(node.data, end=(''))
    
    if node.left == None :
      return
    if node.right == None :
      return
  
    self.pre_order(node.left)
    self.pre_order(node.right)
    return

  def post_order(self, node):

    if node.left == None :
      return
    if node.right == None :
      return

    self.post_order(node.left)
    self.post_order(node.right)

    if node.data != '.' :
      print(node.data, end=(''))

    return

  def in_order(self, node):

    if node.left == None :
      return
    if node.right == None :
      return

    self.in_order(node.left)

    if node.data != '.' :
      print(node.data, end=(''))

    self.in_order(node.right)

    return

n = int(sys.stdin.readline().strip())

root_node = Node('A')
tree = Tree(root_node)

for i in range(0, n):
  cmd = list(sys.stdin.readline().strip().split())
  tree.insert(root_node, cmd[0], cmd[1], cmd[2])

tree.pre_order(root_node)
print()
tree.in_order(root_node)
print()
tree.post_order(root_node)
