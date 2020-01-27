from random import randint, shuffle

class Node:

    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def __repr__(self):
        return f"<Node {self.value} l {self.left} r {self.right}>"

def insert(root, value):
    if root is None:
        root = Node(value)
    else:
        _rinsert(root, value)

def _rinsert(curr, value):
    if value < curr.value:
        if curr.left is None:
            curr.left = Node(value)
        else:
            _rinsert(curr.left, value)
    elif value > curr.value:
        if curr.right is None:
            curr.right = Node(value)
        else:
            _rinsert(curr.right, value)
    elif value == curr.value:
        return None


def search(root, key):
    curr = root
    while True:
        if curr is None or curr.value == key:
            break
        if key < curr.value:
            curr = curr.left
        else:
            curr = curr.right
    return curr

def find_min(node: Node) -> (Node, Node): 
    prev = curr = node
    while curr.left:
        curr = curr.left
    return prev, curr

def replace_node(parent, node, new_node=None) -> None:
    if parent is not node:
        if parent.left == node:
            parent.left = new_node
        else:
            parent.right = new_node

def delete(node, key):
    if node.value == key and not (node.left and node.right):
        return node.left if node.left else node.right
    rdel(None, node, key)
    return node
    
def rdel(parent, node, key):
    if parent is None:
        parent = node
    if key < node.value:
        return rdel(node, node.left, key)
    if key > node.value:
        return rdel(node, node.right, key)
    if key == node.value:
        if node.left and node.right:
            p, s = find_min(node.right)
            node.value = s.value
            rdel(p, s, s.value)
        elif node.left:
            replace_node(parent, node, node.left)
        elif node.right:
            replace_node(parent, node, node.right)
        else:
            replace_node(parent, node, None)

def isBST(node, min, max):
    if node is None: return True
    if node.value < min or node.value > max: return False
    return isBST(node.left, min, node.value - 1) and isBST(node.right, node.value +1, max)

def rtree_gen(n):
    b = None
    l = [x for x in range(1, n+1)]
    shuffle(l)
    for i in l:
        if b is None:
            b = Node(i)
        else:
            insert(b, i)
    return b
        
def preorder(root):
    print(f"{root.value} -> ", end="")
    if root.left: preorder(root.left)
    if root.right: preorder(root.right)

def inorder(root):
    if root.left: inorder(root.left)
    print(f"{root.value} -> ", end="")
    if root.right: inorder(root.right)

def postorder(root):
    if root.left: postorder(root.left)
    if root.right: postorder(root.right)
    print(f"{root.value} -> ", end="")

def reverseorder(root):
    if root.right: reverseorder(root.right)
    print(f"{root.value} -> ", end="")
    if root.left: reverseorder(root.left)

def inRange(root, a, b): # prints values between [a..b] inclusive in ascending order
    if root.left: inRange(root.left, a, b)
    if root.value >= a and root.value <= b:
        print(f"{root.value} -> ", end="")
    if root.right: inRange(root.right, a, b)

def bleaf(root): # prints values of leaf nodes in descending order
    if root.right: bleaf(root.right)
    if not (root.left or root.right):
        print(f"leaf.value={root.value}")
    if root.left: bleaf(root.left)
    
if __name__ == '__main__':
    b = rtree_gen(20)
    isBST(b, 0, 21)
    bleaf(b)
    inRange(b, 1, 10)
    print()
    inorder(b)
    print()
    preorder(b)
    print()
    postorder(b)
    print()
    reverseorder(b)
    print()