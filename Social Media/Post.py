from typing import Any
from Comment import Comment

class Post:
    __slots__ = ("post_id","content","author","likes","comments")
    def __init__(self,post_id:int,content:Any,author:"User") -> None:
        self.post_id = post_id
        self.content = content
        self.author = author
        self.likes : list = []
        self.comments: list = []
    
    
    def edit_post(self,content:Any):
        self.content = content
        print(f"Content is {self.content} , Author is {self.author}")
        print(f"Likes {len(self.likes)} comments {len(self.comments)}")         
        
    def delete_post(self):
        print(f"Post {self.post_id} deleted.")
        
    def like_post(self,user:"User"):
        if not user in self.likes:
            self.likes.append(user)
            print(f"{user.username} liked post {self.post_id}")
        else:
            raise ValueError("User has already liked your post")
    
    def add_comment(self,user:"User",content:Any):
        comment = Comment(user,content)
        self.comments.append(comment)

        print(f"{user.username} commented post {self.post_id}")
        return comment

    def see_comments(self):
        comments = [f"User :{comment.author.username}, Content: {comment.content}" for comment in self.comments]
        for comment in comments:
            print(comment)

