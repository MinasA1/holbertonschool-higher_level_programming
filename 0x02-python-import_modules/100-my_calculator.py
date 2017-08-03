#!/usr/bin/python3
add = __import__('calculator_1').add
sub = __import__('calculator_1').sub
mul = __import__('calculator_1').mul
div = __import__('calculator_1').div
import sys
if len(sys.argv)-1 != 3:
    print("Usage: ./100-my_calculator.py <a> <operator> <b>")
    exit(1)
a = int(sys.argv[1])
b = int(sys.argv[3])
if sys.argv[2] == "+":
    print("{:d} + {:d} = {:d}".format(a, b, add(a, b)))
elif sys.argv[2] == "-":
    print("{:d} - {:d} = {:d}".format(a, b, sub(a, b)))
elif sys.argv[2] == "*":
    print("{:d} * {:d} = {:d}".format(a, b, mul(a, b)))
elif sys.argv[2] == "/":
    print("{:d} / {:d} = {:d}".format(a, b, div(a, b)))
else:
    print("Unknown operator. Available operators: +, -, * and /")
    exit(1)
