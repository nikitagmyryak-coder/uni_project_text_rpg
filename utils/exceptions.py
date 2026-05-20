class GameException(Exception):
    def __init__(self, message="A game error occurred."):
        self.message = f"\033[31m{message}\033[0m"
        super().__init__(self.message)


class InvalidNameException(GameException):
    def __init__(self, message="Invalid name. Name must contain only English letters."):
        super().__init__(message)


class NotEnoughSpace(GameException):
    def __init__(self, message="Not enough space in the inventory."):
        super().__init__(message)


class NotEnoughMoney(GameException):
    def __init__(self, message="Not enough money to complete the transaction."):
        super().__init__(message)


class InvalidChoice(GameException):
    def __init__(self, message="Invalid choice. Please choose a valid option."):
        super().__init__(message)