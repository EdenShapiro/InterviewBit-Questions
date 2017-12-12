# Given an unsorted array of integers, find the length of the longest consecutive elements sequence.
#
# Example:
# Given [100, 4, 200, 1, 3, 2],
# The longest consecutive elements sequence is [1, 2, 3, 4]. Return its length: 4.
#
# Your algorithm should run in O(n) complexity.

def longestConsecutive(self, A):
        hashmap = {}
        for ele in A:
            if ele not in hashmap:
                new_tail = hashmap[ele - 1][0] if (ele - 1) in hashmap else ele
                new_head = hashmap[ele + 1][1] if (ele + 1) in hashmap else ele
                new_length = new_head - new_tail + 1

                hashmap[new_tail] = (new_tail, new_head, new_length)
                hashmap[new_head] = (new_tail, new_head, new_length)

        return max(hashmap.values(), key=lambda x: x[2])[2]
