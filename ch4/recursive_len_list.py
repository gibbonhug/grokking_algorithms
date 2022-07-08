# grokking algorithms exercise 4.2:
# write a recursive func to count the
# number of items in a list

def recursive_len_list(list):
    # return 0 if list is empty
    if not list:
        return 0
    # otherwise, add 1 (for first index),
    # + recursive calls for rest of list
    else:
        return (1 + recursive_len_list([1:]))