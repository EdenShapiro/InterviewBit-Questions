def reverseWords(A):
    lis = A.split()
    new_sentence = ""
    for word in lis[::-1]:
        new_sentence = new_sentence + word + " "
    return new_sentence[:-1]

print reverseWords("the sky is blue")
