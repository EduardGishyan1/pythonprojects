from typing import Any

class Comment:
    __slots__ = ("author","content")
    def __init__(self,author:"User",content:Any) -> None:
        self.author = author
        self.content = content
    
    def edit_comment(self,content:Any):
        self.content = content
    
    def delete_comment(self,post:"Post"):
        post.comments.remove(self)
        print(f"Comment by {self.author.username} deleted.")