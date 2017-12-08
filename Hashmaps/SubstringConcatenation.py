# Substring Concatenation
#
# You are given a string, S, and a list of words, L, that are all of the same length.
#
# Find all starting indices of substring(s) in S that is a concatenation of each word in L exactly once and without any intervening characters.
#
# Example :
#
# S: "barfoothefoobarman"
# L: ["foo", "bar"]
#
# You should return the indices: [0,9].
# (order does not matter).

# @param A : string
# @param B : tuple of strings
# @return a list of integers
def findSubstring(A, B):
    result_list = set()
    dic = {}
    word_length = len(B[0])
    for word in B:
        if word in dic:
            dic[word] += 1
        else:
            dic[word] = 1
    reference_dic = dic.copy()
    i = 0
    substring_start_index = 0
    j = word_length
    while i < len(A) and j <= len(A):
        if A[i:j] in dic and dic[A[i:j]] >= 1:
            dic[A[i:j]] -= 1
            every_word_has_been_used = all(value == 0 for value in dic.itervalues())
            if every_word_has_been_used:
                # print "every_word_has_been_used. starting over"
                result_list.add(substring_start_index)
                dic = reference_dic.copy()
                substring_start_index += 1
                i = substring_start_index
                j = substring_start_index + word_length
            else:
                i = j
                j = j + word_length
        else:
            substring_start_index += 1
            i = substring_start_index
            j = substring_start_index + word_length
            dic = reference_dic.copy()
    return list(result_list)


# S: "barfoothefoobarman"
# L: ["foo", "bar"]
print findSubstring("barfoothefoobarman", ["foo", "bar"])
# 0,9

print findSubstring("cacabbabcbccbccbbbcccabaaacaaccbbaccca", [ "c", "c", "b", "a", "c" ])
# 17 18 32


print findSubstring("bcabbcaabbccacacbabccacaababcbb", [ "c", "b", "a", "c", "a", "a", "a", "b", "c" ])
# 6 16 17 18 19 20

print findSubstring("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", [ "aaa", "aaa", "aaa", "aaa", "aaa" ])
# 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50 51 52 53 54 55 56 57 58 59 60 61 62 63 64 65 66 67 68 69 70 71 72 73 74 75 76 77 78 79 80 81 82 83 84 85 86 87 88 89 90 91 92 93 94 95 96 97 98
