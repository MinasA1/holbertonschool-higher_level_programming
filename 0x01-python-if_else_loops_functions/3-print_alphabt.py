#!/usr/bin/python3
for i in range(0, 26):
    if i+ord("a") != ord("q") and i+ord("a") != ord("e"):
        print(chr(ord('a')+i), end='')
