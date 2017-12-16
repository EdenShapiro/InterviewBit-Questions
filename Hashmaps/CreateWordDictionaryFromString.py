import string
import re
def create_word_dictionary(input_string):
    all_word_list = re.split("[\.\,\:\;\-\s+]", input_string)
    word_list = [x.lower() for x in all_word_list]
    word_list = filter(None, word_list)
    dic = {}
    for word in word_list:
        if word in dic:
            dic[word] += 1
        else:
            dic[word] = 1
    return dic

print create_word_dictionary("To be or not to be, that is the question")
