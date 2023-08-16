#!/usr/bin/python3


'''
 ' weight_avarage - function that returns the weighted average of all integers
 ' tuple (<score>, <weight>)
 '
 ' @my_list: the list
 '
 ' Return: return the weighted average
 '         return 0 if list is empty
'''


def weight_average(my_list=[]):
    sum = 0
    av_sum = 0

    if my_list is None or my_list == []:
        return (0)

    for i in my_list:
        rxn = 1

        for j in i:
            # multiply the values in each element
            # (row X column) or (score X weight)
            rxn *= j

        # add each consequent value of rxn and i[-1]
        sum += rxn
        av_sum += i[-1]

    # get the weighted average
    average = sum / av_sum

    return (average)
