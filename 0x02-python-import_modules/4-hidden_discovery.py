#!/usr/bin/python3
import hidden_4
for i in dir(hidden_4):
    if i[:2] != "__":
        print("{}".format(i))
