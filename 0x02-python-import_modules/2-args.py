#!/usr/bin/python3
import sys


if __name__ == "__main__":
    args = sys.argv
    if len(args) != 1:
        s = "s" if (len(args) - 1) > 1 else ""
        print("{:d} argument{}:".format((len(args) - 1), s))
        for index, value in enumerate(args[1:]):
            print("{:d}: {}".format((index + 1), value))
    else:
        print("0 arguments.")
