"""
This is a SHELL challenge
"""

import sys


def main():
    """
    main function
    """
    while True:
        sys.stdout.write("$ ")
        sys.stdout.flush()
        input_str = sys.stdin.readline()
        if not input_str:
            break
        input_str = input_str.strip()
        if input_str == "exit":
            return
        sys.stdout.write(f"{input_str}: command not found\n")


if __name__ == "__main__":
    main()
