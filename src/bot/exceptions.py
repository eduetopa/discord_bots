class FailedToJoinChannel(Exception):
    def __init__(self, message="Filaed to join channel") -> None:
        self.message = message
        super().__init__(self.message)
        