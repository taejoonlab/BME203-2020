#!/usr/bin/env python3
import sys

query_term = ''

filename_fa = sys.argv[1]

f_fa = open(filename_fa, 'r')
for line in f_fa:
    if line.startswith('>'):
        tmp_h = line.strip()
        if tmp_h.find('complete genome') >= 0 and tmp_h.find(query_term) >= 0:
            is_print = 1
            sys.stderr.write('%s\n' % tmp_h)
            print(tmp_h)
        else:
            is_print = 0
    elif is_print > 0:
        print(line.strip())
f_fa.close()
