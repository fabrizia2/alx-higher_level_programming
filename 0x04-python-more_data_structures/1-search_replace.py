#!/usr/bin/python3

# @my_list is the initial list
# @search is the element to replace in the list
# @replace is the new element

def search_replace(my_list, search, replace):
    if not my_list:
        return my_list

    new_list = []
    for i in my_list:
        if i == search:
            new_list.append(replace)

        else:
            new_list.append(i)

    return new_list
