# Merge K Sorted Lists
#
# Merge k sorted linked lists and return it as one sorted list.
#
# Example :
#
# 1 -> 10 -> 20
# 4 -> 11 -> 13
# 3 -> 8 -> 9
#
# will result in
#
# 1 -> 3 -> 4 -> 8 -> 9 -> 10 -> 11 -> 13 -> 20
#

import heapq
# @param A : list of linked list
# @return the head node in the linked list
def mergeKLists(self, A):
    heap = []
    for head_node in A:
        while head_node:
            heapq.heappush(heap, head_node.val)
            head_node = head_node.next
    new_head = ListNode(heapq.heappop(heap))
    node = new_head
    for i in range(len(heap)):
        node.next = ListNode(heapq.heappop(heap))
        node = node.next
    return new_head
