import string

def isPalindrome(A):
    A = A.translate(None, string.punctuation).lower()
    A = "".join(A.split(" "))
    print A
    i = 0
    j = len(A)-1
    while i<j:
        if A[i] != A[j]:
            return 0
        i += 1
        j -= 1
    return 1

print isPalindrome("A man, a plan, a canal: Panama")
