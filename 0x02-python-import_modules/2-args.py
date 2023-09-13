#!/usr/bin/python3
import sys


def main():
    """main function
    """
    if len(sys.argv) >= 2:
        if len(sys.argv) == 2:
            print(len(sys.argv) - 1, "argument:")
        else:
            print(len(sys.argv) - 1, "arguments:")
        for i in range(1, len(sys.argv)):
            print(i, ": ", sys.argv[i],sep="")
    else:
        print(len(sys.argv) - 1, "arguments.")


if __name__ == "__main__":
    main()
