#!/usr/bin/python

import sys
import re


def main(args):
    if len(args) < 3:
        print 'Usage: ./prep.py <search_pattern> <replace_pattern>'
        exit(0)

    pat = re.compile(args[1])
    repl = args[2]

    for line in sys.stdin:
        # print line.strip()
        print pat.sub(repl, line.strip())

main(sys.argv)
