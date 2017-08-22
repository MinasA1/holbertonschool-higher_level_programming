#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        return float(a/b)
    except:
        return None
    finally:
        print("Inside result:", end=" ")
        if not b:
            print(None)
        else:
            print("{:.1f}".format(a / b))
