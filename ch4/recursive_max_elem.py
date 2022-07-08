# grokking algorithms exercise 4.3:
# write a recursive func to find the
# maximum number in a list

def recursive_max_elem(list):
    # return null if nothing in the list
    if not list:
        return None
    # otherwise, get the max between the
    # first index of current call and
    # the rest of list
    else:
        return (max(list[0], recursive_max_elem(list[:1])))