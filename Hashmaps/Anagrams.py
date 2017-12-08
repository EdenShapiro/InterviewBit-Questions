# Given an array of strings, return all groups of strings that are anagrams. Represent a group by a list of integers representing the index in the original list. Look at the sample case for clarification.
#
#     Anagram : a word, phrase, or name formed by rearranging the letters of another, such as 'spar', formed from 'rasp'
#
#     Note: All inputs will be in lower-case.
#
# Example :
#
# Input : cat dog god tca gdo
# Output : [[1, 4], [2, 3]]
#
# cat and tca are anagrams which correspond to index 1 and 4.
# dog and god are another set of anagrams which correspond to index 2 and 3.
# The indices are 1 based ( the first element has index 1 instead of index 0).

def are_anagrams(a, b): # O(n)
    dic = {}
    if len(a) != len(b):
        return False

    for letter in a:
        if letter in dic:
            dic[letter] += 1
        else:
            dic[letter] = 1
    for letter in b:
        if letter in dic:
            dic[letter] -= 1
        else:
            return False
    for key, value in dic.items():
        if value != 0:
            return False
    return True


def anagrams(A):
    result = []
    dic = {}
    if len(A) < 2:
        return [[1]]
    for i, word in enumerate(A): #rememebr to go back and add 1 to the index
        if word not in dic:
            dic[word] = [i+1]
        else:
            dic[word].append(i+1)
    i = 0
    j = 1
    print dic
    while A and i < len(A):
        if j < len(A):
            if not are_anagrams(A[i], A[j]):
                j += 1
            else:
                if A[i] in dic and A[j] in dic and A[i] != A[j]:
                    dic[A[i]].extend(dic[A[j]])
                    del dic[A[j]]
                    print dic
                A.pop(j)
        else:
            i += 1
            j = i + 1

    for item in dic:

        result.append(sorted(dic[item]))

    return result

print are_anagrams("cat", "bat") #false
print are_anagrams("cat", "act") #true
print are_anagrams("cata", "atca") #true
print are_anagrams("cata", "atcaa") #false
print are_anagrams("a", "a") #true
print are_anagrams("a", "b") #false
# print anagrams(["cat", "dog", "god", "tca", "gdo"])
# print anagrams(["cat", "dog", "god", "tca"])
print anagrams([ "abcd", "dcba", "dcba", "abcd", "abcd", "adbc", "dabc", "adcb"])
# [1,2,3,4,5,6,7,8]

# Input : cat dog god tca
# Output : [[1, 4], [2, 3]]
