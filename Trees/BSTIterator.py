# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
# root, smaller node, smallest node
class BSTIterator:
    # @param root, a binary search tree's root node
    def __init__(self, root):
        node = root
        self.nodes = self.inorder(node)
    # @return a boolean, whether we have a next smallest number
    def hasNext(self):
        if self.nodes:
            return True
        else:
            return False

    # @return an integer, the next smallest number
    def next(self):
        return self.nodes.pop(0).val

    def inorder(self, node, node_list=[]):
        if node:
            if node.left:
                node_list = self.inorder(node.left, node_list)
            node_list.append(node)
            if node.right:
                node_list = self.inorder(node.right, node_list)
        return node_list

# Your BSTIterator will be called like this:
# i = BSTIterator(root)
# while i.hasNext(): print i.next(),
