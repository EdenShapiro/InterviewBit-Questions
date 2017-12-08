# Challenge 2 - Add two numbers
#
# In this exercise, we'll use your LinkedListNode implementation to represent a non-negative integer such that each node in the list represents a single digit (in base 10) and the digits are stored in reverse order.
#
# 1     == 1
# 1->2   == 21
# 1->2->3 == 321
#
# Write a program which takes as its input two such lists, a and b, and adds them arithmetically one decimal at a time. Your algorithm should traverse both lists together, adding the values for each node and carrying the 1 to the next place when the sum >= 10. The result should be returned as a linked list in the same format as the input lists.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def print_nodes(head):
        A = head
        while A:
            print str(A.val) + " -> ",
            A = A.next
        print "None"

def add_two_linked_lists(A, B):
    head_A = A
    head_B = B
    while A and B:
        A = A.next
        B = B.next
    if A and not B:
        longer = head_A
        shorter = head_B
    elif B and not A:
        longer = head_B
        shorter = head_A
    else:
        longer = head_A
        shorter = head_B

    carry = 0
    head = longer
    while longer:
        shorter_val = 0 if not shorter else shorter.val
        mini_sum = shorter_val + longer.val + carry
        if mini_sum < 10:
            longer.val = mini_sum
            carry = 0
        else:
            carry = int(mini_sum/10)
            longer.val = mini_sum%10
            if not longer.next:
                longer.next = ListNode(carry)
                break
        longer = longer.next
        shorter = None if not shorter else shorter.next
    return head
# Examples:
#
# 1->2     +   5->3   == 6->5      // 21 + 35 == 56
# 1->2     +   1->2->3 == 2->4->3    // 21 + 321 == 342
# 1->2->3   +   7->8->9 == 8->0->3->1  // 321 + 987 == 1308

node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)
node4 = ListNode(4)
node5 = ListNode(5)
node6 = ListNode(6)
node7 = ListNode(7)
node8 = ListNode(8)
node9 = ListNode(9)
B_node1 = ListNode(1)
B_node2 = ListNode(2)
B_node3 = ListNode(3)

node7.next = node8
node8.next = node9
node9.next = None

B_node1.next = B_node2
B_node2.next = B_node3
B_node3.next = None

# node5.next = node3
# node3.next = None

# 1->2->3   +   7->8->9 == 8->0->3->1  // 321 + 987 == 1308

A = node7
# B = node5
B = B_node1
print_nodes(add_two_linked_lists(A, B))
