
def preorderTraversalWithoutRecursion(A):
    root = A
    nodes = []
    result_array = []
    nodes.append(A)

    while nodes:
        node = nodes.pop()
        result_array.append(node.val)
        if node.right:
            nodes.append(node.right)
        if node.left:
            nodes.append(node.left)

    return result_array
