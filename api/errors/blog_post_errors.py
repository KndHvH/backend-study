

class PostError(Exception):
    def __init__(self, post_id) -> None:
        self.post_id = post_id

class PostNotFoundError(PostError):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)
        
class PostAllreadyExists(PostError):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)