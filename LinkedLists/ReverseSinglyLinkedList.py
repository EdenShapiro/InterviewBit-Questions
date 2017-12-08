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


node1.next = node5
node5.next = node4
node4.next = node3
# node3.next = node9
# node9.next = None
node3.next = None

print_nodes(node1)

def reverse(head):
    A = head
    next_node = A.next
    A.next = None
    while next_node:
        temp = next_node.next
        next_node.next = A
        A = next_node
        next_node = temp
    head = A
    return head

print_nodes(reverse(node1))
