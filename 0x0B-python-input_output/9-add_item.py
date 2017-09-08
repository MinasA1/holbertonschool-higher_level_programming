#!/usr/bin/python3
"""add item to json file"""
save = __import__('7-save_to_json_file').save_to_json_file
load = __import__('8-load_from_json_file').load_from_json_file
if __name__ == "__main__":
    import sys
    lis = sys.argv[1:]
    try:
        jsold = load("add_item.json")
        lis = jsold + lis
        save(lis)
    except:
        save(lis, "add_item.json")



    

