class LoginError(Exception):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)
        
class BadServerResponseCode(Exception):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)