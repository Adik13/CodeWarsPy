# In this kata you will create a function that
# takes a list of non-negative integers and strings
# and returns a new list with the strings filtered out.
def filter_list(l):
    sort_list = []
    for elements in l:
        if type(elements) is int:
            sort_list.append(elements)
    return sort_list
