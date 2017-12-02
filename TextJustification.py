# Given the inputs:
#
# String text = "This is an example of text justification.";
# int length = 16;
#
# ...the output array should be:
#
# String[] output = {
#   "This    is    an",
#   "example  of text",
#   "justification.  "
# };

def justify(text, length):
    lines = []
    if len(text) <= length:
        lines.append(text)
        return lines

    words = text.strip().split()
    if length == 1:
        # return lines.append(letter) for letter in "".join(words)
        for letter in "".join(words):
            lines.append(letter)
        return lines
    line_words = [words[0]]
    spaceless_length = len(words[0])
    curr_line_length = len(words[0])
    for word in words[1:]:
        if (curr_line_length + 1 + len(word)) <= length:
            line_words.append(word)
            curr_line_length = curr_line_length + 1 + len(word)
            spaceless_length = spaceless_length + len(word)
        else: # adding another word to the line wouldn't fit

            # wrap up current line # "to"
            total_extra_space_length = length - spaceless_length # 4
            number_of_gaps = len(line_words) - 1
            if number_of_gaps == 0:
                number_of_gaps = 1
            uneven_extra_space_length = total_extra_space_length%number_of_gaps # 0
            space_length_between_words = total_extra_space_length/number_of_gaps # 4
            line = line_words[0]
            if total_extra_space_length == 0:
                if len(line_words) > 1:
                    space_length_between_words = 1
            else:
                if len(line_words) == 1:
                    line = line + " "*space_length_between_words
            for l_word in line_words[1:]:
                add_space = 0
                if uneven_extra_space_length > 0:
                    add_space = space_length_between_words + 1
                    uneven_extra_space_length -= 1
                else:
                    add_space = space_length_between_words
                line = line + " "*add_space + l_word
            lines.append(line)

            # set up new line
            curr_line_length = len(word)
            spaceless_length = len(word)
            line_words = [word]

    line = " ".join(line_words)
    extra_space_length = length - curr_line_length
    line = line + " "*extra_space_length
    lines.append(line)

    for line in lines:
        assert len(line) == length
    return lines

print justify("This is an example of text justification.", 16)



# def justify(text, length):
#     lines = []
#     if len(text) <= length:
#         lines.append(text)
#         return lines
#
#     words = text.strip().split()
#     line = ""
#     for word in words:
#         if (len(line) + 1 + len(word)) <= length:
#             line = line + " " + word
#         else:
#             lines.append(line)
#             line = word + " "
#     lines.append(line)
#     return lines
#
# print justify("This is an example of text justification.", 16)
#
