# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def detectCycle(A):
    head = A
    runner = A.next
    within_the_cycle = None
    # move runner by two, move A by one

    while A and runner:
        if runner == A:
            # return A
            within_the_cycle = runner
            break
        if runner.next:
            if runner.next.next:
                runner = runner.next.next
            else:
                runner = None
        else:
            runner = None
        A = A.next

    if within_the_cycle:
        A = within_the_cycle
        length_of_loop = 0
        while A.next != within_the_cycle:
            length_of_loop += 1
            A = A.next

        A = head
        B = head
        counter = 0
        while counter <= length_of_loop:
            A = A.next
            counter += 1
        while A != B:
            A = A.next
            B = B.next
        return A
    else:
        return None

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

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5
node5.next = node6
node6.next = node7
node7.next = node8
node8.next = node9
node9.next = node10
node10.next = node11
node11.next = node12
node12.next = node13
node13.next = node13
node13.next = node14
node14.next = node15
node15.next = node7

assert detectCycle(node1).val == 7
