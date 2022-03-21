class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data


preorder = []


def pre(root):
    if root:
        preorder.append(root.data)
        pre(root.left)
        pre(root.right)


inorder = []


def inord(root):
    if root:
        inord(root.left)
        inorder.append(root.data)
        inord(root.right)


postorder = []


def post(root):
    if root:
        post(root.left)
        post(root.right)
        postorder.append(root.data)


if __name__ == '__main__':
    root = Node(10)
    root.left = Node(34)
    root.right = Node(89)
    root.left.left = Node(45)
    root.left.right = Node(50)
    # parent = Node(34)
    # parent.left = Node(45)
    # parent.right = Node(50)
    # root = Node(parent)
    # root.right = Node(89)

    pre(root)
    inord(root)
    post(root)
    print(preorder)
    print(inorder)
    print(postorder)


