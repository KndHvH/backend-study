

class PostError(Exception):
    def __init__(self, post_id) -> None:
        self.post_id = post_id
        self.status_code = 400
        self.success = False
        self.message = f"Error related to post id {self.post_id}"
        self.data = None
    
    def as_response(self):
        return {
            "status_code": self.status_code,
            "body": {
                "success": self.success,
                "message": self.message,
                "data": self.data
            }
        }
        
class PostNotFoundError(PostError):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)
        self.message = f"Blog post with id {self.post_id} does not exist"
        
class PostAlreadyExistsError(PostError):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)
        self.message = f"Blog post with id {self.post_id} already exists"