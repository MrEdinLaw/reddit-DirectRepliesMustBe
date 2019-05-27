# Copyright (C) 2019 Edin Demic @MrEdinLaw - All Rights Reserved
# You may use, and modify this code but not distribute

# Imports
import praw

# Keys and Config
from keys import keys
from config import config

# Reddit API Connection
reddit = praw.Reddit(client_id=keys['client_id'],
                     client_secret=keys['client_secret'],
                     user_agent=keys['user_agent'],
                     username=keys['username'],
                     password=keys['password'])
# Subreddit Work
subreddit = reddit.subreddit(config['subreddit'])

for comment in subreddit.stream.comments():
    if comment.parent_id[:2] == "t3":
        if ">!" and "!<" not in comment.body:
            comment.mod.remove(config['removal_reason'])
            print(f"Comment Removed: {comment.id}\nComment Text: {comment.body}")
            comment.author.message(config['removal_pm_title'], config['removal_pm_body'])
