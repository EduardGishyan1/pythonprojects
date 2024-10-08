from Comment import Comment
from Feed import Feed
from Post import Post
from User import User

if __name__ == "__main__":
  
    alice = User(username="alice", email="alice@example.com", password="password123")
    bob = User(username="bob", email="bob@example.com", password="password456")
    charlie = User(username="charlie", email="charlie@example.com", password="password789")

    
    alice.register()
    bob.register()
    charlie.register()

    alice.follow(bob)
    alice.follow(charlie)
    bob.follow(charlie)

    post1 = alice.create_post("Hello, world!")
    post2 = bob.create_post("This is Bob's first post!")
    post3 = charlie.create_post("This is Charlie's first post!")

    comment = post1.add_comment(bob, "Nice post, Alice!")
    post1.add_comment(charlie, "I agree!")
    comment.delete_comment(post1)
    post1.like_post(bob)
    post2.like_post(alice)
    comments = post1.see_comments()
    alice_feed = Feed(alice)
    alice_feed.generate_feed()
    alice_feed.display_feed()
   

