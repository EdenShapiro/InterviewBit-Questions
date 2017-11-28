# Given a list of non negative integers, arrange them such that they form the largest number.
#
# For example:
#
# Given [3, 30, 34, 5, 9], the largest formed number is 9534330.

def compare(a, b):
    x_1 = int(a + b)
    x_2 = int(b + a)
    if(x_1 > x_2):
        return 1
    elif(x_2 > x_1):
        return -1
    else:
        return 0

def largestNumber(A):
    l = [str(x) for x in A]
    sorted_l = sorted(l, cmp=compare, reverse=True)
    string = "".join(x for x in sorted_l)

    return int(string)

assert compare("1", "5") == -1
assert compare("34", "3") == 1
assert compare("30", "3") == -1

print largestNumber([3, 30, 34, 5, 9])
