class Feed:
    def __init__(self, user:"User"):
        self.user = user
        self.posts:list = []

    def generate_feed(self):
        for followed_user in self.user._followings:
            self.posts.extend(followed_user._posts)  
        self.posts.sort(key=lambda post: post.post_id, reverse=True) 

    def display_feed(self):
        print(f"Feed for {self.user.username}:")
        for post in self.posts:
            print(f"{post.author.username}: {post.content}")
