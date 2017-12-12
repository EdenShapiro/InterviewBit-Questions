# Create the sqrt function
# If x is not a perfect square, return floor(sqrt(x))

def sqrt(A):
    lower = 0
    higher = A
    mid_point = (lower + higher) / 2
    while mid_point * mid_point != A:
        if lower + 1 == higher:
            return lower
        if mid_point * mid_point > A:
            higher = mid_point
        elif mid_point * mid_point < A:
            lower = mid_point
        mid_point = (lower + higher) / 2
    return mid_point

assert sqrt(9) == 3
print sqrt(9)
assert sqrt(11) == 3
print sqrt(11)
assert sqrt(81) == 9
print sqrt(81)
assert sqrt(100) == 10
print sqrt(100)
