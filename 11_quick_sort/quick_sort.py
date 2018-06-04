#-*- coding: utf-8 -*-

def quick_sort(unsorted_list):
    if len(unsorted_list) < 2:
        return unsorted_list
    mid = unsorted_list[0]
    equal = [i for i in unsorted_list if i == mid]
    low = [i for i in unsorted_list if i < mid]
    high = [ i for i in unsorted_list if i > mid]
    return quick_sort(low) + equal + quick_sort(high)

if __name__ == '__main__':
    my_list = [3, 1, 4, 6, 5, 4, 2, 8]
    print(my_list)
    print(quick_sort(my_list))

