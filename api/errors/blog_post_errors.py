

class PostError(Exception):
    def __init__(self, post_id) -> None:
        self.post_id = post_id
        self.message = f"Error related to post id {self.post_id}"
        
class PostNotFoundError(PostError):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)
        self.message = f"Blog post with id {self.post_id} does not exist"
        
class PostAlreadyExistsError(PostError):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)
        self.message = f"Blog post with id {self.post_id} already exists"