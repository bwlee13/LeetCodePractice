class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


preorder = []


def pre(root):
    if root:
        preorder.append(root.value)
        pre(root.left)
        pre(root.right)


inorder = []


def inord(root):
    if root:
        inord(root.left)
        inorder.append(root.value)
        inord(root.right)


postorder = []


def post(root):
    if root:
        post(root.left)
        post(root.right)
        postorder.append(root.value)


if __name__ == '__main__':
    root = Node(10)
    root.left = Node(34)
    root.right = Node(89)
    root.left.left = Node(45)
    root.left.right = Node(50)
    # parent = Node(34)
    # parent.left = Node(45)
    # parent.right = Node(50)
    # root = Node(10)
    # root.left = Node(parent.value)
    # root.right = Node(89)

    pre(root)
    inord(root)
    post(root)
    print(preorder)
    print(inorder)
    print(postorder)


