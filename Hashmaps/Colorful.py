# A number can be broken into different contiguous sub-subsequence parts.
# Suppose, a number 3245 can be broken into parts like 3 2 4 5 32 24 45 324 245.
# And this number is a COLORFUL number, since product of every digit of a contiguous subsequence is different
#
# Example:
#
# N = 23
# 2 3 23
# 2 -> 2
# 3 -> 3
# 23 -> 6
# this number is a COLORFUL number since product of every digit of a sub-sequence are different.
#
# Output : 1
#
#
# N = 123
# 1 2 3 12 23 123

# @param A : integer
# @return an integer
def colorful(A):
    string_a = str(A)
    substrings = []
    dic = {}
    i = 0
    if len(string_a) < 2:
        return 1
    j = 1
    while i < len(string_a):
        if j < len(string_a)+1:
            substrings.append(string_a[i:j])
            j += 1
        else:
            i += 1
            j = i + 1
    for item in substrings:
        # print item
        nums = map(int, list(item))
        print nums
        product = 1
        for x in nums:
            product *= x
        if product in dic:
            return 0
        else:
            dic[product] = 1
    return 1

# print colorful(23)
print colorful(123)
