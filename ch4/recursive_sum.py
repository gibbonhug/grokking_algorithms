# grokking algorithms exercise 4.1:
# code a recursive sum func, which is
# described on grokking algorithms page 57

# get a list
def recursive_sum(list):
    # return 0 if list is empty
    if not list:
        return 0
    # otherwise, total sum is first num in list,
    # + sum of the rest of the list
    else:
        return (list[0] + recursive_sum(list[1:]))