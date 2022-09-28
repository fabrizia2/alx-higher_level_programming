#!/usr/bin/python3

# Delete by value
# If the value doesn’t exist, the dictionary won’t change
# All keys having the searched value have to be deleted

def complex_delete(a_dictionary, value):
    list_keys = list(a_dictionary.keys())

    for value_dic in list_keys:
        if value == a_dictionary.get(value_dic):
            del a_dictionary[value_dic]

    return (a_dictionary)
