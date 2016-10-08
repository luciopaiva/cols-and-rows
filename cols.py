#!/usr/bin/python

import sys
import re


def main(args):
    if len(args) not in (2, 3):
        print 'Usage: ./cols.py [<search_pattern>] <replace_pattern>'
        exit(0)

    if len(args) == 3:
        repl = args[2]
        pat = re.compile(args[1])
    else:
        repl = args[1]
        positions = [re.sub(r'\\', '', pos) for pos in re.findall(r'\\\d+', repl)]
        max_pos = 0
        for pos in positions:
            if pos > max_pos:
                max_pos = pos
        pat = r'^\s*' + r'\s+'.join([r'(\S+)'] * int(max_pos)) + r'.*$'
        pat = re.compile(pat)

    try:
        for line in sys.stdin:
            print pat.sub(repl, line.strip())
    except IOError:
        # may happen if stdout is closed by the process that follows in the pipeline
        pass

main(sys.argv)
