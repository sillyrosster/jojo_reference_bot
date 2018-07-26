import praw
import config
import time
import os

# bot logs into reddit
def bot_login():
    print("Logging in...")
    login = praw.Reddit(username = config.username,
                        password = config.password,
                        client_id = config.client_id,
                        client_secret = config.client_secret,
                        user_agent = "IsThatAJ0J0Reference test bot v0.1")
    print("Logged In!")
    return login

# bot checks for a simple string in a comment from a subreddit
def run_bot(login, comments_replied_to):
    print("Obtaining 25 comments...")

    for comment in login.subreddit('test').comments(limit=25):
        if ("dogboi" in comment.body) and (comment.id not in comments_replied_to): #and (comment.author != login.user.me()):
            print("test dogboi found! id=" + comment.id)
            # replies to comment
            #comment.reply("test dogboi successful!")
            print("Replied to comment id=" + comment.id)

            comments_replied_to.append(comment.id)
            # writes comment id replied to, to file
            with open("comments_replied_to.txt", "a") as f:
                print("Writing id to file...")
                f.write(comment.id + "\n")

    print("Sleeping for 10 seconds...")
    time.sleep(10)

# checks if file exists. if so, reads file
def get_saved_comments():
    if not os.path.isfile("comments_replied_to.txt"):
        comments_replied_to = []
    else:
        with open("comments_replied_to.txt", "r") as f:
            comments_replied_to = f.read()
            comments_replied_to = comments_replied_to.split("\n")
            #comments_replied_to = filter(None, comments_replied_to)
    return comments_replied_to


    
login = bot_login()
comments_replied_to = get_saved_comments()
print(comments_replied_to)

while True:
    run_bot(login, comments_replied_to)