#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def quick_sort(arr):
    if len(arr) < 2 :
        return arr
    else:
         pivot = arr[0]
         less = [i for i in arr[1:] if i <= pivot]
         great = [i for i in arr[1:] if i > pivot]
         return quick_sort(less) + [pivot] + quick_sort(great)

# TODO: int 比较时还有异常
def quick_sort_int(arr):
    if len(arr) < 2 :
        return arr
    else:
         pivot = arr[0]
         less = [int(i) for i in arr[1:] if int(i) <= int(pivot)]
         great = [int(i) for i in arr[1:] if int(i) > int(pivot)]
         return quick_sort(less) + [int(pivot)] + quick_sort(great)

import csv
import time
import os

if __name__ == "__main__":
    script_dir = os.path.dirname(__file__)
    rel_path = "raw_sort_data"
    file_path = os.path.join(script_dir, rel_path)
    with open(file_path, 'rb') as f:
        reader = csv.reader(f)
        sort_list = list(reader)
        start_time = time.time()
        sort_result = quick_sort(sort_list)
        end_time = time.time()
        cost = end_time-start_time
        print "quick sort 10000 item cost is " , cost 
        with open("sort-result", 'w') as wf:
            writer = csv.writer(wf)
            writer.writerows(sort_result)
