#!/usr/bin/python3
import sys
l = len(sys.argv) - 1
print("{:d} {:s}:".format(l, "arguments" if l > 1 else "argument"))
for i in range(1, len(sys.argv)):
    print("{:d}: {:s}".format(i, sys.argv[i]))
