# ZigZag Level Order Traversal BT
#
# Given a binary tree, return the zigzag level order traversal of its nodes' values. (ie, from left to right, then right to left for the next level and alternate between).
#
# Example :
# Given binary tree
#
#     3
#    / \
#   9  20
#     /  \
#    15   7
#
# return
#
# [
#          [3],
#          [20, 9],
#          [15, 7]
# ]
#

# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param A : root node of tree
    # @return a list of list of integers
    def zigzagLevelOrder(self, A):
        depth = self.get_max_depth(A)
        result_list = [[] for x in xrange(depth)]
        counter = 0
        return self.tree_traverser(A, counter, result_list)

    def tree_traverser(self, A, counter, result_list):
        if A:
            if counter % 2 == 0:
                result_list[counter].append(A.val)
            else:
                result_list[counter].insert(0, A.val)
            counter += 1
            result_list = self.tree_traverser(A.left, counter, result_list)
            result_list = self.tree_traverser(A.right, counter, result_list)
            return result_list
        else:
            return result_list


    def get_max_depth(self, A):
        if not A:
            return 0
        else:
            return max(self.get_max_depth(A.left) + 1, self.get_max_depth(A.right) + 1)


node1 = TreeNode(3)
node2 = TreeNode(9)
node3 = TreeNode(20)
node4 = TreeNode(15)
node5 = TreeNode(7)
node1.left = node2
node1.right = node3
node3.left = node4
node3.right = node5
sol = Solution()
print sol.get_max_depth(node1)
print sol.zigzagLevelOrder(node1)
# node1.left = node2
# node1.right = node2
# node1.left = node2
