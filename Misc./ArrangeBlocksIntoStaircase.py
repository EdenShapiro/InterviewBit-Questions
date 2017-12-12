# Return the height of a staircase you can make given a certain number of blocks
# Example:
# If blocks = 3, you can make this structure:
# *
# **
# height == 2

# If blocks = 5, you can make this structure:
# *
# **
# **
# so still only height of 2, because you can't complete the third stair level

import math

def arrangeBlocks(blocks):
    for b in blocks:
        print staircase(b)


def staircase(b):
    return int(round(math.sqrt(2*b + 1))) - 1


# (naive solution) recursive:

# def staircase(what_ive_got, need_to_print):
#     if what_ive_got <= 0:
#         return 0
#     elif what_ive_got < need_to_print:
#         return 0
#     else:
#         return staircase(what_ive_got - need_to_print, need_to_print + 1) + 1


# (naive solution) iterative:

# def staircase2(what_ive_got):
#     need_to_print = 1
#     staircases = 0
#     while what_ive_got > 0:
#         what_ive_got = what_ive_got - need_to_print
#         if what_ive_got >= 0:
#             staircases += 1
#             need_to_print += 1
#         else:
#             return staircases
#     return staircases


print staircase(0) #== 0
print staircase(1) #== 1
print staircase(2) #== 1
print staircase(3) #== 2
print staircase(4) #== 2
print staircase(5) #== 2
print staircase(6) #== 3
print staircase(7) #== 3
print staircase(8) #== 3
print staircase(9) #== 3
print staircase(10)# == 4
print staircase(11)# == 4
print staircase(12)# == 4
print staircase(13)# == 4
print staircase(14)# == 4
print staircase(15)# == 5



assert staircase(0) == 0
assert staircase(1) == 1
assert staircase(2) == 1
assert staircase(3) == 2
assert staircase(4) == 2
assert staircase(5) == 2
assert staircase(6) == 3
assert staircase(7) == 3
assert staircase(8) == 3
assert staircase(9) == 3
assert staircase(10) == 4
assert staircase(11) == 4
assert staircase(12) == 4
assert staircase(13) == 4
assert staircase(14) == 4
assert staircase(15) == 5
