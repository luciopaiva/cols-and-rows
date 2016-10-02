#!/usr/bin/python

import sys
import re


def main(args, argc):
    if argc not in (2, 3):
        print 'Usage: ./prepf.py [-x] <filter_pattern>'
        exit(0)

    if argc == 3:
        filter_out = args[1] == '-x'
        pat = re.compile(args[2])
    else:
        filter_out = False
        pat = re.compile(args[1])

    for line in sys.stdin:
        line = line.strip()
        did_match = pat.search(line) is not None
        if did_match != filter_out:
            print line

main(sys.argv, len(sys.argv))
