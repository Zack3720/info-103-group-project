import discord
import api_keys as keys
import get_reddit_info as reddit
from discord.ext import commands

def main():
    client = commands.Bot(command_prefix='$', intents=discord.Intents.all())

    # Provide instructions for what your discord bot should do once it has logged in
    @client.event
    async def on_ready():
        await client.tree.sync()
        # Load the discord channel you want to post to
        channel_id = 1234989181499871366
        channel = client.get_channel(channel_id)

        # Post a messages to your discord channel
        # TODO: modify this code to post at least 7 times
        # await channel.send("Bot started!")

    # Adds a command called getPost to the bot. Can be accessed through typing /getPost on discord server
    # @client.tree.command(name= "getpost", description= "Get some number of posts from a subreddit")
    @client.command()
    async def getPost(ctx: discord.Interaction, subredditName, postCount):
        if subredditName == '':
            await ctx.channel.send("Missing first arguement, subredditName!")
            return
        elif postCount == '':
            await ctx.channel.send("Missing second arguement, subredditName!")
            return
        elif not postCount.isdigit():
            await ctx.channel.send("Second argument must be a number!")
            return
        
        print(type(subredditName))
        print(postCount)

        submissions = reddit.getRedditSubmissions(subredditName, int(postCount))

        await ctx.channel.send("Here is the titles of the submissions:")

        for submission in submissions:
            await ctx.channel.send(submission.title)
        return

    # Now that we've defined how the bot should work, start running your bot
    client.run(keys.discord_token)

if __name__ == '__main__':
    main()


