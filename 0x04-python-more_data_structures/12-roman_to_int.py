#!/usr/bin/python3


'''
 ' roman_to_int - function that roman numerals to integers
 '
 ' @roman_string: the roman numeral to convert
 '
 ' Retuen: return the converted @roman_string on success
 '         return 0 on failure
'''


def roman_to_int(roman_string):
    num = 0

    # check if @roman_string is a string, not an integer
    if type(roman_string) is str:
        # create a dictionary to represent roman numerals
        roman_dict = {
            "I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000
        }

        for i, j in zip(roman_string, roman_string[1:]):
            if roman_dict[i] < roman_dict[j]:
                num -= roman_dict[i]

            else:
                num += roman_dict[i]

        num += roman_dict[roman_string[-1]]

        return (num)

    else:
        return (0)
