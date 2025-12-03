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
