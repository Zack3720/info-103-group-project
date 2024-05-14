import praw
import api_keys as keys

reddit = praw.Reddit(
    username=keys.reddit_username, password=keys.reddit_password,
    client_id=keys.reddit_client_id, client_secret=keys.reddit_client_secret,
    user_agent="a custom python script for user /" + str(keys.reddit_username)
)

def getRedditSubmissions(subredditName: str):
    
    pass