#!/usr/bin/python

import sys
import cols


def show_help(cmd):
    usage()


def usage():
    print 'Usage: exie <cmd> [params]'
    print ''
    print 'Available commands:'
    print '\trows: filter lines in or out'
    print '\tcols: select columns from each line'
    print ''
    print 'Type `exie help <cmd>` for specific instructions'


def main(args):
    argc = len(args)
    if argc < 2:
        usage()
        return

    cmd, args = args[1:]

    if cmd == 'help':
        show_help()
    elif cmd == 'cols':
        cols.main(args, len(args))
    else:
        print 'Unknown command ' + cmd
        show_help('')

main(sys.argv)
