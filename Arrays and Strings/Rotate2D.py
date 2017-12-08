def rotate2D(A):

    l = zip(*A[::-1])
    for i in range(len(l)):
        temp = l[i]
        l[i] = list(temp)
    return l




print rotate2D([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
# [1, 2, 3],
# [4, 5, 6],
# [7, 8, 9]

# 7, 4, 1
# 8, 5, 2
# 9, 6, 3

# temp1 = A[0][0]
# A[0][0] = A[2][0]
#
# temp2 = A[0][2]
# A[0][2] = temp1
#
# temp1 = A[2][2]
# A[2][2] = temp2
#
# temp2 = A[2][0]:
# A[2][0] = temp1
#
#
# temp1 = A[0][1]
# A[0][1] = A[1][0]
#
# temp2 = A[1][2] #6
# A[1][2] = temp1
#
# temp3 = A[2][1] #8
# A[2][1] = temp2
#
# temp4 = A[1][0]
# A[1][0] = temp3
