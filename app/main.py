"""
This is a SHELL challenge
"""

import sys
from typing import List, Optional, Tuple


class EmptyCommandException(Exception):
    """
    Exception for when a command is empty
    """

    def __init__(self, message="Empty command was given as input"):
        self.message = message
        super().__init__(self.message)


class CommandNotFoundException(Exception):
    """
    Exception for when a command is not found
    """

    def __init__(self, message="command not found"):
        self.message = message
        super().__init__(self.message)


class ArgumentNotFoundException(Exception):
    """
    Exception for when an argument is not found when looked up
    """

    def __init__(self, message="argument not found"):
        self.message = message
        super().__init__(self.message)


class ExitException(Exception):
    """
    Exception for when a user types "exit"
    """

    def __init__(self, message="exit"):
        self.message = message
        super().__init__(self.message)


def main():
    """
    main function
    """
    while True:
        sys.stdout.write("$ ")
        sys.stdout.flush()
        input_str = sys.stdin.readline()
        cmd = ""
        args = []
        try:
            cmd, args = parse_command(input_str)
        except EmptyCommandException:
            break

        try:
            handle_command(cmd, args)
        except CommandNotFoundException:
            sys.stdout.write(f"{cmd}: command not found\n")
        except ArgumentNotFoundException:
            sys.stdout.write(f"{args[0]}: not found\n")
        except ExitException:
            return


def handle_command(command: str, args: List[str]):
    """
    Handles a command pattern,
    returning a bool indicating whether it should break the main loop
    """
    valid_commands = ["exit", "echo", "type"]

    match command:
        case "exit":
            raise ExitException
        case "echo":
            sys.stdout.write(" ".join(args) + "\n")
        case "type":
            local_cmd = args[0]
            if local_cmd not in valid_commands:
                raise ArgumentNotFoundException
            sys.stdout.write(f"{local_cmd} is a shell builtin\n")

        case _:
            raise CommandNotFoundException


def parse_command(input_str: Optional[str]) -> Tuple[str, List[str]]:
    """
    parse a command
    """
    if not input_str:
        raise EmptyCommandException

    split_command = input_str.split()
    cmd = split_command[0]
    args = split_command[1:]
    return cmd, args


if __name__ == "__main__":
    main()
