# Info 103 Group 4 Final Project

Our project is a Discord bot that can pull posts from any public subreddit on Reddit and display it to users on Discord. The bot can also filter through post using a sentiment analysis filter to determine if a post is either positive or negative. For the user to use the bot they must use the command prefix '$' and use the bot command getPost. This command takes in a subreddit, number of post to get and a sentiment (optional).<br>
### Command Usage
``` $getPost <subreddit> <# of post> <sentiment>``` <br> <br>
Example: <br>
``` $getPost udub 20 positive ```
## How to use

1. Make sure you have [Python installed.](https://www.datacamp.com/blog/how-to-install-python)

2. Install dependencies with pip
```bash
$ pip install -r requirements.txt
```

3. Install nltk model
```bash
$ python -c "import nltk; nltk.download('vader_lexicon')"
```

4. Run main.py!
```bash
$ python main.py
```