def swap_first_last(lst):
    if len(lst) >= 2:
        lst[0], lst[-1] = lst[-1], lst[0]
    return lst
my_list = [1, 2, 3, 4, 5]
print("Swapped list:", swap_first_last(my_list))