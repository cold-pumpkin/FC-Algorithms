# 1991. 트리순회

# 클래스로 노드를 표현
class Node:
    def __init__(self, data, left, right):
        self.data = data
        self.left = left
        self.right = right

# 1. 전위 순회
def preorder_traversal(node):
    print(node.data, end='')
    if node.left != '.':
        preorder_traversal(tree[node.left])
    if node.right != '.':
        preorder_traversal(tree[node.right])

# 2. 중위 순회
def inorder_traversal(node):
    if node.left != '.':
        inorder_traversal(tree[node.left])
    print(node.data, end='')
    if node.right != '.':
        inorder_traversal(tree[node.right])

# 3. 후위 순회
def postorder_traversal(node):
    if node.left != '.':
        postorder_traversal(tree[node.left])
    if node.right != '.':
        postorder_traversal(tree[node.right])
    print(node.data, end='')

n = int(input())
tree = {}
for _ in range(n):
    data, left, right = input().split()
    tree[data] = Node(data, left, right)

preorder_traversal(tree['A'])
print()
inorder_traversal(tree['A'])
print()
postorder_traversal(tree['A'])