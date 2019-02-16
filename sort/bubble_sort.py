#!/usr/bin/env python3
# -*- coding: utf-8 -*-
def bubble_sort(arr):
    for i in range(0, len(arr)):
        for j in range(i+1, len(arr)):
            if arr[j] < arr[i]:
                tmp = arr[i]
                arr[i] = arr[j]
                arr[j] = tmp

import csv
import os
import time

if __name__ == "__main__":
    my_arr = [1,22,9, 15, 18, 3, 2, 6, 8]
    bubble_sort(my_arr)
    print my_arr

    script_dir = os.path.dirname(__file__)
    rel_path = "raw_sort_data"
    file_path = os.path.join(script_dir, rel_path)
    with open(file_path, 'rb') as f:
       reader = csv.reader(f)
       sortlist = list(reader)
       start_time = time.time()
       bubble_sort(sortlist)
       end_time = time.time()
       print "bubble sort 10000 item cost is " , (end_time-start_time)
