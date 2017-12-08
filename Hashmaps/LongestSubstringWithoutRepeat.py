# Longest Substring Without Repeat
#
# Given a string,
# find the length of the longest substring without repeating characters.
#
# Example:
#
# The longest substring without repeating letters for "abcabcbb" is "abc", which the length is 3.
#
# For "bbbbb" the longest substring is "b", with the length of 1.

def length_of_longest_non_repeating_substring(string):
    i = 0
    dic = {}
    substring_start_index = 0
    max_length = 0
    while i < len(string):
        if string[i] in dic:
            max_length = max(len(string[substring_start_index:i]), max_length)

            substring_start_index = dic[string[i]] + 1
            i = substring_start_index
            dic = {}
        dic[string[i]] = i
        i += 1
        print ""
    max_length = max(len(string[substring_start_index:i]), max_length)
    return max_length

print length_of_longest_non_repeating_substring("abcabcbb") #3
print length_of_longest_non_repeating_substring("bbbbb") #1
print length_of_longest_non_repeating_substring("abcabcbbdgh") #4
print length_of_longest_non_repeating_substring("dadbc") #4
