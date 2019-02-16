#!/usr/bin/env python3
# -*- coding: utf-8 -*-
def find_smallest(arr):
    smallest = arr[0]
    smallest_index = 0
    for i in range(1, len(arr)) :
        if arr[i] > smallest:
            smallest = arr[i]
            smallest_index = i
    return smallest_index

def selection_sort(arr):
    for i in range(0, len(arr)):
        smallest = arr[i]
        smallest_index = i
        for j in range(i+1, len(arr)):
            if arr[j] < smallest:
                smallest = arr[j]
                smallest_index = j

        #swap smallest and arr[i]
        tmp = arr[i]
        arr[i] = smallest;
        arr[smallest_index] = tmp;

#test function
if __name__ == "__main__":
    my_arr = [1,22,9, 15, 18, 3, 2, 6, 8]
    selection_sort(my_arr)
    print my_arr
