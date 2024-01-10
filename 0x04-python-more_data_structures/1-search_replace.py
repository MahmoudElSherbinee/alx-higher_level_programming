#!/usr/bin/python3
# new_list = list(map(lambda x: replace if x == search else x, my_list))
# return new_list
def search_replace(my_list, search, replace):
    new_list = my_list.copy()
    for i in range(len(my_list)):
        if my_list[i] == search:
            new_list[i] = replace
    return new_list
