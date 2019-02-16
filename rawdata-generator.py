#!/usr/bin/python
# -*- coding: UTF-8 -*-

import csv
import random
import sys
import getopt
import traceback

def main(argv=None):
    if argv is None:
        argv = sys.argv
    try:
        f = open("raw_sort_data", 'w')
        writer = csv.writer(f)
        for i in range(0, 10000):
            temp = random.randint(0, 10000)
            writer.writerow([temp])

    except Exception, err:
        print err.message
        traceback.print_exc()


if __name__ == "__main__":
    main()
