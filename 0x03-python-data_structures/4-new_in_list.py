#!/usrbin/python3

def new_in_list(my_list, idx, element):
    list = my_list[:]

    if idx < 0 or idx > len(my_list) - 1:
        return list

    list[idx] = element
    return list
