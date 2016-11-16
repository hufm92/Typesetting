# -*- coding=UTF-8 -*-
__version__ = '0.1.2'

while True:
    a = raw_input().decode('utf-8')
    line = 3
    count = len(a)
    col = (count-1)/line+1

    print '>>>'
    for i in xrange(line):
        st = list(reversed([a[idx] for idx in xrange(count) if idx%line==i]))
        st = [u'。']*(col-len(st)) + st
        print ' '.join(st).encode('utf-8')
