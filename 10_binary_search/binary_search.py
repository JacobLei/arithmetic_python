#-*- coding:utf-8 -*-

def binary_search(search_list, item):
    length = len(search_list)
    low, high = 0, length - 1
    while high >= low:
        mid = (high + low) // 2
        guess = search_list[mid]
        if guess > item:
            high = mid - 1
        elif guess < item:
            low = mid + 1
        else:
            return mid
    return None

if __name__ == '__main__':
    my_list = [0, 0, 0, 1, 2, 3, 4, 5, 6, 7]
    print(binary_search(my_list, 3))
