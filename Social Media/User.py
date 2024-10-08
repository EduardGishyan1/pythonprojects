from typing import Any
from Comment import Comment
from Post import Post

class User:
    __slots__ = ("__username","__email","__password","_followers","_followings","_posts")
    def __init__(self,username:str,email:str,password:str) -> None:
        self.username = username
        self.email = email
        self.password = password
        self._followers : list = []
        self._followings: list = []
        self._posts:list = []
    
    @property
    def username(self)->str:
        return self.__username
    
    @username.setter
    def username(self,username:str) -> None:
        if not username or not isinstance(username, str):
            raise ValueError("Username must be a non-empty string.")
        if not (3 <= len(username) <= 20):
            raise ValueError("Username must be between 3 and 20 characters long.")
        if not username.isalnum() and "_" not in username:
            raise ValueError("Username can only contain letters, numbers, and underscores.")
        
        self.__username = username
    
    @property
    def email(self)->str:
        return self.__email
    
    @email.setter
    def email(self,email:str)->None:
        if not "@" in email:
            raise ValueError("Enter valid email address for user...")
        
        username,domain = email.split("@")
        
        if not username or len(domain) < 3 or "." not in domain:
            raise ValueError("Enter valid email address for user...")

        self.__email = email
    
    @property
    def password(self)->str:
        return self.__password
    
    @password.setter
    def password(self,password:str):
        if not password or not isinstance(password, str):
            raise ValueError("Password must be a non-empty string.")
        if len(password) < 6:
            raise ValueError("Password must be at least 6 characters long.")
        
        self.__password = password
    
    @property
    def followers(self):
        return self._followers
    
    @property
    def followings(self):
        return self._followings
    
    def register(self):
        print(f"{self.username} registered successfully!")
    
    def login(self,username:str,password:str):
        if username == self.username and password == self.password:
            print("success...")
        else:
            raise ValueError("Invalid username or password try again...")
    
    def follow(self,user:"User")->None:
        if self == user:
            print("You can't follow yourself")
            return
        
        if not user in user.followers:
            user._followers.append(self)
            self._followings.append(user)
            print(f"{self.username} is now following {user.username}.")
            
        else:
           print("You have already in followers list...")
    
    def unfollow(self,user:"User") -> None:
        if user in self.followings:
                self.followings.remove(user)
                user.followers.remove(self)
        else:
            print(f"You have not follower User")
    
    def create_post(self, content:Any):
        post_id = len(self._posts) + 1
        post = Post(post_id, content, self)
        self._posts.append(post)
        print(f"{self.username} created a post: {content}")
        return post
