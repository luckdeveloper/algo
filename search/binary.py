#!/usr/bin/env python3
# -*- coding: utf-8 -*-
def binary_search(list, item):
    low = 0
    high = len(list) - 1
    while low <= high:
        mid = (low + high) / 2
        if list[mid] == item:
            return mid
        if list[mid] > item:
            high = mid - 1
        else:
            low = mid + 1
    return None

if __name__ == "__main__":
    my_list = [1,2,4,6,7,9]
    print binary_search(my_list, 6)
    print binary_search(my_list, -1)
