import sys

def preorder(ch):
    result = ''
    if(ch!='.'):
        result += ch
        result += preorder(tree[ch][0])
        result += preorder(tree[ch][1])
    return result

def inorder(ch):
    result = ''
    if(ch!='.'):
        result += inorder(tree[ch][0])
        result += ch
        result += inorder(tree[ch][1])
    return result

def postorder(ch):
    result = ''
    if(ch!='.'):
        result += postorder(tree[ch][0])
        result += postorder(tree[ch][1])
        result += ch
    return result

N = int(sys.stdin.readline())
tree = {}

for i in range(N):
    line = sys.stdin.readline().replace('\n', '').split(' ')
    tree[line[0]] = [line[1], line[2]]

print(preorder('A'))
print(inorder('A'))
print(postorder('A'))