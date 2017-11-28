
def rotate(A, num):
    return A[num%len(A):] + A[:num%len(A)]
#
# print rotate("helloworld", 3)
# print rotate("helloworld", 8)
# print rotate("helloworld", 1)
# print rotate("helloworld", 2)
#
