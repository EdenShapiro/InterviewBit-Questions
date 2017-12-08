# Given a roman numeral, convert it to an integer.
#
# Input is guaranteed to be within the range from 1 to 3999.
#
# Read more details about roman numerals at Roman Numeric System
#
# Example :
#
# Input : "XIV"
# Return : 14
#
# Input : "XX"
# Output : 20
#

# I = 1
# V = 5
# X = 10
# L = 50
# C = 100
# D = 500
# M = 1000

def romanToInt(s): #if there is a smaller number in front, do subtraction
# if there is an equal or greater number after, do addition
    roman_dic = {"I":1, "V":5, "X":10, "L":50, "C": 100, "D":500, "M":1000}
    sum = 0
    i = len(s) - 1
    while i >= 0:
        j = i - 1
        substraction_amount = 0
        while j >= 0 and roman_dic[s[i]] > roman_dic[s[j]]:
            substraction_amount = substraction_amount + roman_dic[s[j]]
            j-=1
        sum = sum + (roman_dic[s[i]] - substraction_amount)
        i = j

    return sum


print romanToInt("X") # 10
print romanToInt("XX") # 20
print romanToInt("IX") # 9
print romanToInt("XIX") # 19
print romanToInt("XIV") # 14
print romanToInt("MDCCLXXVI") #  1776
print romanToInt("MCMLIV") # 1954   90054
print romanToInt("X") # 10
