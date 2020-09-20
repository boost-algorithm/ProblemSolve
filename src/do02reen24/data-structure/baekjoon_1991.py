import sys

class Node(object):
    def __init__(self, depth, left, right):
        self.depth = depth
        self.left = left
        self.right = right

def preOrder(tree, index):
    if index != '.':
        node = tree[index]
        print(index, end='')
        preOrder(tree, node.left)
        preOrder(tree, node.right)
    return

def inOrder(tree, index):
    if index != '.':
        node = tree[index]
        inOrder(tree, node.left)
        print(index, end='')
        inOrder(tree, node.right)
    return

def postOrder(tree, index):
    if index != '.':
        node = tree[index]
        postOrder(tree, node.left)
        postOrder(tree, node.right)
        print(index, end='')
    return

if __name__ == '__main__':
    n = int(sys.stdin.readline())
    tree = None
    treeRoot = None

    for i in range(n):
        root, left, right = sys.stdin.readline().split()
        depth = 0
        if tree == None:
            tree = dict()
            treeRoot = root
            tree[root] = Node(depth, left, right)
        else:
            tree[root].left = left
            tree[root].right = right
            depth = tree[root].depth
        
        if not left=='.':
            tree[left] = Node(depth+1, '.', '.')
        if not right=='.':
            tree[right] = Node(depth+1, '.', '.')

    preOrder(tree, treeRoot)
    print()
    inOrder(tree, treeRoot)
    print()
    postOrder(tree, treeRoot)