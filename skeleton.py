#!/usr/bin/python
# -*- coding: UTF-8 -*-

import sys
import traceback
def main(argv=None):
    if argv is None:
        argv = sys.argv
    try:

    except Exception, err:
        print err.message
        traceback.print_exc()


if __name__ == "__main__":
    main()
