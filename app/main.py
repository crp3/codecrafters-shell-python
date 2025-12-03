"""
This is a SHELL challenge
"""

import os
import stat
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
            local = args[0]
            if local in valid_commands:
                sys.stdout.write(f"{local} is a shell builtin\n")
                return

            found, path = browse_path(local)
            if found:
                sys.stdout.write(f"{args[0]} is {path}\n")
            else:
                raise ArgumentNotFoundException

        case _:
            raise CommandNotFoundException


def browse_path(local: str) -> Tuple[bool, str]:
    """
    Browse a filename in PATH and return only if executable
    """
    path_str = os.environ["PATH"]
    path_str_split = path_str.split(":")
    for directory_path in path_str_split:
        try:
            contents = os.listdir(directory_path)
            for content in contents:
                if content == local:
                    file_path = os.path.join(directory_path, content)
                    st = os.stat(file_path)
                    is_executable = st.st_mode & (
                        stat.S_IXUSR | stat.S_IXGRP | stat.S_IXOTH
                    )
                    if is_executable:
                        return True, file_path
        except FileNotFoundError:
            continue

    return False, ""


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
