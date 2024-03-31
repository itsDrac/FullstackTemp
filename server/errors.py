
class AlreadyExist(Exception):
    message: str
    def __init__(self, msg:str = "Item already exist in database"):
        self.message = msg
