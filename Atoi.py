def atoi(s):
    number_dic = {"0":0,"1":1, "2":2, "3":3,"4":4, "5":5,"6":6,"7":7, "8":8, "9":9}
    string = s.strip().split()[0]
    start = 0
    end = len(string)
    is_negative = False
    for i, char in enumerate(string):
        if char in number_dic:
            if string[i-1]:
                if string[i-1] == "-":
                    is_negative = True
                    start = i
                    break
                if string[i-1] == "+":
                    is_negative = False
                    start = i
                    break
    for k, char in enumerate(string[start:]):
        if char not in number_dic:
            end = k + start
            break
    s = string[start:end]
    index = 0
    result = 0
    for char in s[::-1]: #and while index > len(s)-1
        if char in number_dic:
            result = result + (number_dic[char] * (10**index))
        else:
            return 0
        index += 1
    if is_negative:
        result = result * -1
    if result > 2147483647:
        return 2147483647
    if result < -2147483647 - 1:
        return -2147483647 - 1
    return result

print atoi("88297DJHGD  248252140B12 37239U4622733246I218 9 1303 44 A83793H3G2 1674443R591 4368 7 97")
print atoi("-6435D56183011M11 648G1 903778065 762 75316456373673B5 334 19885 90668 8 98K X277 9846")

print atoi("-44024E11 G24 378556582G0467E 6 613 1 2173 9829 5K5H099 2Q 458890732 94 0")

print atoi("V515V 5793K 627 23815945269 1 1249794L 631 8755 7")
