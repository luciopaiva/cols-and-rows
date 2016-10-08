#!/usr/bin/python

import sys
import re


class Operation:
    def __init__(self, label):
        self.label = label

    def get_label(self):
        return self.label

    def accrue(self, val):
        raise NotImplementedError()

    def get(self):
        raise NotImplementedError()


class Sum(Operation):
    def __init__(self, label):
        Operation.__init__(self, label)
        self.sum = 0.0

    def accrue(self, val):
        self.sum += val

    def get(self):
        return self.sum


class Avg(Operation):
    def __init__(self, label):
        Operation.__init__(self, label)
        self.sum = 0.0
        self.count = 0

    def accrue(self, val):
        self.sum += val
        self.count += 1

    def get(self):
        return self.sum / self.count


class Max(Operation):
    def __init__(self, label):
        Operation.__init__(self, label)
        self.max = float('-inf')

    def accrue(self, val):
        if val > self.max:
            self.max = val

    def get(self):
        return self.max


class Min(Operation):
    def __init__(self, label):
        Operation.__init__(self, label)
        self.max = float('inf')

    def accrue(self, val):
        if val < self.max:
            self.max = val

    def get(self):
        return self.max


class First(Operation):
    def __init__(self, label):
        Operation.__init__(self, label)
        self.first = None

    def accrue(self, val):
        if self.first is None:
            self.first = val

    def get(self):
        return self.first


class Last(Operation):
    def __init__(self, label):
        Operation.__init__(self, label)
        self.last = None

    def accrue(self, val):
        self.last = val

    def get(self):
        return self.last


class OperationFactory:
    def __init__(self):
        pass

    @staticmethod
    def create_from_name(op_str, label):
        return {
            'sum': Sum(label),
            'avg': Avg(label),
            'min': Min(label),
            'max': Max(label),
            'first': First(label),
            'last': Last(label)
        }.get(op_str, None)


def main(args, argc):
    if argc != 2:
        print 'Usage: ./group.py <output_pattern>'
        print "Example: cat input.tsv | ./group.py 'sum(1) avg(1)'"
        print "Available operations:"
        print "    sum, avg, min, max, first, last"
        print "Input is treated as columns separated by spaces and/or tabs; the first column has index 1."
        print ""
        exit(0)

    ops_in_output_order = []
    op_list_by_col = {}
    cmd_list = re.findall(r'\w+\(\d+\)', args[1])
    for input_cmd in cmd_list:
        op_str = re.match(r'\w+', input_cmd).group(0)
        col_num = int(re.search(r'\d+', input_cmd).group(0)) - 1  # to zero-based index

        op = OperationFactory.create_from_name(op_str, input_cmd)
        if op is None:
            print 'Undefined operation "%s"' % op_str
            exit(1)

        existing_ops = op_list_by_col.get(col_num, [])
        existing_ops.append(op)
        op_list_by_col[col_num] = existing_ops

        ops_in_output_order.append(op)

    col_splitter = re.compile('\s+')

    for line in sys.stdin:
        cols = col_splitter.split(line.strip())
        for col_idx in op_list_by_col.keys():  # only iterate over columns for which we have any operations
            val = float(cols[col_idx].replace('[,.]', ''))
            for op in op_list_by_col[col_idx]:
                op.accrue(val)

    results = [str(op.get()) for op in ops_in_output_order]
    print "\t".join(results)

main(sys.argv, len(sys.argv))
