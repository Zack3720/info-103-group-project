import praw
import api_keys as keys

reddit = praw.Reddit(
    username=keys.reddit_username, password=keys.reddit_password,
    client_id=keys.reddit_client_id, client_secret=keys.reddit_client_secret,
    user_agent="a custom python script for user /" + str(keys.reddit_username)
)

# Gets a specified number of post from a given subreddit.
#
# Parameters:
#   subredditName   - the name of the subreddit to return post from
#   postCount       - the number of post to return
#
# Returns: A list of reddit submissions
def getRedditSubmissions(subredditName: str, postCount: int) -> list:
    subreddit = reddit.subreddit(subredditName)
    submissions = subreddit.hot(limit=postCount)
    # This function returns a list of submissions, if you want to learn more about what is in
    # a reddit submission here is the link to the documentation:
    # https://praw.readthedocs.io/en/stable/code_overview/models/submission.html
    return list(submissions)