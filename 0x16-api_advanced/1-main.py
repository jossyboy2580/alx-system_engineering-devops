#!/usr/bin/python3

import sys


if __name__ == '__main__':
    top_ten = __import__('1-top_ten').top_ten
    if len(sys.argv) >= 2:
        top_ten(sys.argv[1])
