import praw
import api_keys as keys
import nltk
from nltk.sentiment import SentimentIntensityAnalyzer

sia = SentimentIntensityAnalyzer()

reddit = praw.Reddit(
    username=keys.reddit_username,
    password=keys.reddit_password,
    client_id=keys.reddit_client_id,
    client_secret=keys.reddit_client_secret,
    user_agent="a custom python script for user /" + str(keys.reddit_username),
    check_for_async=False,
)


# Gets a specified number of post from a given subreddit that have a
# given sentiment. Uses sentiment analysis filter to sort through post
# with their title and description.
#
# Parameters:
#   subredditName   - the name of the subreddit to return post from
#   postCount       - the number of post to return
#   sentiment       - the sentiment to filter by. Must be either 
#                     "positive" or "negative"
#
# Returns: reddit submissions iterator
def getRedditSubmissionWithSentiment(
    subreddit: praw.models.Subreddit, postCount: int, sentiment: str
) -> list:
    multiplier = 2
    while postCount * multiplier <= 1000:  # At most 1000 post
        submissions = subreddit.hot(limit=postCount * multiplier)
        filtered_submissions = []

        print(f"Search within {postCount * multiplier} posts")

        # Loop through fetched submissions and filter based on sentiment
        for submission in submissions:
            score = sia.polarity_scores(submission.title + " " + submission.selftext)[
                "compound"
            ]
            if (score > 0 and sentiment == "positive") or (
                score < 0 and sentiment == "negative"
            ):
                filtered_submissions.append(submission)

            # If we have enough filtered submissions, return the list
            if len(filtered_submissions) >= postCount:
                return filtered_submissions

        multiplier *= 2


# Gets a specified number of post from a given subreddit.
#
# Parameters:
#   subredditName   - the name of the subreddit to return post from
#   postCount       - the number of post to return
#
# Returns: A list of reddit submissions
def getRedditSubmissions(subredditName: str, postCount: int, sentiment: str) -> list:
    subreddit = reddit.subreddit(subredditName)
    submissions = (
        subreddit.hot(limit=postCount)
        if sentiment == "unspecified"
        else getRedditSubmissionWithSentiment(subreddit, postCount, sentiment)
    )
    # This function returns a list of submissions, if you want to learn more about what is in
    # a reddit submission here is the link to the documentation:
    # https://praw.readthedocs.io/en/stable/code_overview/models/submission.html
    return list(submissions)
