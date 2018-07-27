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
def run_bot(login, comments_replied_to, jojo_reference_counter):
    
    print("Obtaining 25 comments...")

    for comment in login.subreddit('ShitPostCrusaders+QualityPostCrusaders').comments(limit=25):
        if redditor('HeMan_Batman') and comment.id not in comments_replied_to:
            print("HeMan_Batman found JoJo referencing!")

            # reply to comment, add to jojo_reference_counter
            comment.reply("[Is that a JoJo reference?!](https://i.kym-cdn.com/photos/images/original/001/217/374/8fa.png) \n ^reference counter: {}").format(jojo_reference_counter)
            jojo_reference_counter += 1

            comments_replied_to.append(comment.id)

            # writes comment id to file
            with open("comments_replied_to.txt", "a") as f:
                print("Writing id to file...")
                f.write(comment.id + "\n")            

    return jojo_reference_counter



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

jojo_reference_counter = 0
print(jojo_reference_counter)

while True:
    run_bot(login, comments_replied_to, jojo_reference_counter)