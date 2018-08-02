import praw
import config
import time
import os

# almost flake8 compliant

REPLY_MESSAGE = ('[Is that a JoJo reference?!](https://i.kym-cdn.com/photos/images/original'
            '/001/217/374/8fa.png) \n ^reference counter: {}.format(jojo_reference_counter')


# bot logs into reddit
def authenticate():
    print("Authenticating...")
    reddit = praw.Reddit(
            username=config.username,
            password=config.password,
            client_id=config.client_id,
            client_secret=config.client_secret,
            user_agent='IsThatAJ0J0Reference test bot v0.1')
    print("Authenticated as {}".format(reddit.user.me()))
    return reddit


# main function
def main():
    reddit = authenticate()
    while True:
        run_bot(reddit, comments_replied_to)
    # print(comments_replied_to)
    # jojo_reference_counter = 0
    # print(jojo_reference_counter)


# bot checks for a simple string in a comment from a subreddit
def run_bot(reddit, comments_replied_to):
    print("Obtaining 25 comments...")
    for comment in reddit.subreddit('test').comments(limit=25):
        if comment == 'JoJo' and comment.id not in comments_replied_to:
            print("JoJoRef_Bot found JoJo referencing!")
            # reply to comment, add to jojo_reference_counter
            # comment.reply(REPLY_MESSAGE)
            # jojo_reference_counter += 1
            comments_replied_to.append(comment.id)
            # writes comment id to file
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
            # comments_replied_to = filter(None, comments_replied_to)
    return comments_replied_to


comments_replied_to = get_saved_comments()


# checks to see if the current 'module' is '__main__'
if __name__ == '__main__':
    main()
