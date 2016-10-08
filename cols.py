#!/usr/bin/python

import sys
import re


def main(args):
    if len(args) < 3:
        print 'Usage: ./cols.py <search_pattern> <replace_pattern>'
        exit(0)

    pat = re.compile(args[1])
    repl = args[2]

    try:
        for line in sys.stdin:
            # print line.strip()
            print pat.sub(repl, line.strip())
    except IOError:
        # may happen if stdout is closed by the process that follows in the pipeline
        pass

main(sys.argv)
