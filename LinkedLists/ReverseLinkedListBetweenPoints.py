# Reverse a linked list from position m to n. Do it in-place and in one-pass.
#
# For example:
# Given 1->2->3->4->5->NULL, m = 2 and n = 4,
#
# return 1->4->3->2->5->NULL.
#
#     Note:
#     Given m, n satisfy the following condition:
#     1 <= m <= n <= length of list.
#
#     Note 2:
#     Usually the version often seen in the interviews is reversing the whole linked list which is obviously an easier version of this question.

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

node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)
node4 = ListNode(4)
node5 = ListNode(5)
node6 = ListNode(6)
node7 = ListNode(7)
node8 = ListNode(8)
node9 = ListNode(9)
node10 = ListNode(10)
node11 = ListNode(11)
node12 = ListNode(12)
node13 = ListNode(13)
node14 = ListNode(14)
node15 = ListNode(15)
node16 = ListNode(16)
node17 = ListNode(17)
node18 = ListNode(18)

def reverse(head):
    A = head
    next_node = A.next
    A.next = None
    while next_node:
        temp = next_node.next
        next_node.next = A
        A = next_node
        next_node = temp
    return A


def reverseBetween(A, m, n):
    head = A
    m_counter = 1
    n_counter = 1
    m_node = None
    m_node_prev = None
    while A.next and n_counter <= n:
        if m_counter == m-1 or m == 1: #start reversing
            print "start reversing"
            if m == 1:
                m_node_prev = None
                m_node = A
                new_end_of_list = A
                n_counter -= 1
            else:
                m_node_prev = A
                m_node = A.next
                new_end_of_list = A.next
            next_node = m_node.next

            while next_node and n_counter < n - 1:
                temp = next_node.next
                next_node.next = m_node
                m_node = next_node
                next_node = temp
                n_counter += 1

            new_beginning_of_list = m_node
            new_end_of_list.next = next_node
            if m == 1:
                head = new_beginning_of_list
            else:
                m_node_prev.next = new_beginning_of_list
            break
        m_counter += 1
        n_counter += 1
        A = A.next
    return head

# For example:
# 1->2->3->4->5->NULL, m = 2 and n = 4
# returns 1->4->3->2->5->NULL

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5
node5.next = node6
node6.next = node7
node7.next = node8
node8.next = None
m = 4
n = 8
A = node1
print_nodes(reverseBetween(A, m, n))
