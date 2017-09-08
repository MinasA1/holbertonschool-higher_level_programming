#!/usr/bin/python3
"""append after"""


def append_after(filename="", search_string="", new_string=""):
    with open(filename, 'r', encoding="utf-8") as f:
        file = f.readlines()
        for nl, line in enumerate(file):
            if search_string in line:
                file.insert(nl + 1, new_string)
        f.close()
    with open(filename, 'w', encoding="utf-8") as f:
        file = "".join(file)
        f.write(file)


append_after("append_after_100.txt", "Python", "\"C is fun!\"\n")
