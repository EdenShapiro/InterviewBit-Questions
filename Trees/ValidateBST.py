# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#
#    15
#   /  \
#  9   20
# /   /  \
#3   16   25

import sys
class Solution:
    # @param A : root node of tree
    # @return an integer
    def isValidBST(self, A):
        min_num = -sys.maxint
        max_num = sys.maxint
        return self.helperIsValidBST(A, min_num, max_num)

    def helperIsValidBST(self, A, min_num, max_num):
        if not A:
            return True
        return (self.helperIsValidBST(A.left, min_num, A.val)
        and self.helperIsValidBST(A.right, A.val, max_num)
        and A.val < max_num and A.val > min_num)
        
