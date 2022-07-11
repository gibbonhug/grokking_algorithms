# grokking algorithms exercise 4.4:
# implement a recursive binary search algorithm

def recursive_binary_search(list, goal, left_index, right_index):
    if left_index <= right_index:
        middle_index = (left_index + right_index) // 2
        if list[middle_index] == goal:
            return middle_index
        # goal is in lower half of list
        elif list[middle_index] > goal:
            return binary_search(list, goal, left_index, middle_index - 1)
        # goal is in upper half of list
            return binary_search(list, goal, middle_index + 1, right_index)
    # goal is not in list if left_index becomes greater than right_index
    else:
        return None