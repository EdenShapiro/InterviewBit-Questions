def wave(A):
    A.sort()
    wave_array = [0] * len(A)
    for i in range(1, len(A), 2):
        wave_array[i-1] = A[i]
        wave_array[i] = A[i-1]
    if len(A) % 2 != 0:
            wave_array[len(A) - 1] = A[len(A) - 1]
    return wave_array
# 1, 2, 3, 4, 5, 6
#
# 0  1  2  3  4  5
#
# 2     4     6


# One possible answer : [2, 1, 4, 3]
# Another possible answer : [4, 1, 3, 2]

print wave([1, 2, 3, 4, 5, 6, 7])
