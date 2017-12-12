# Given a binary tree, find its maximum depth.
#
# The maximum depth of a binary tree is the number of nodes along the longest path from the root node down to the farthest leaf node.


def maxDepth(self, A):
    if not A:
        return 0
    return max(self.maxDepth(A.left) + 1, self.maxDepth(A.right) + 1)
