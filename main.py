import discord
import api_keys as keys
import get_reddit_info as reddit
from discord.ext import commands
import datetime


def main():
    client = commands.Bot(command_prefix="$", intents=discord.Intents.all())

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
    async def getPost(
        ctx: discord.Interaction, subredditName, postCount, sentiment="unspecified"
    ):
        if subredditName == "":
            await ctx.channel.send("Missing first arguement, subredditName!")
            return
        elif postCount == "":
            await ctx.channel.send("Missing second arguement, postCount!")
            return
        elif not postCount.isdigit():
            await ctx.channel.send("Second argument must be a number!")
            return
        elif sentiment not in ["unspecified", "positive", "negative"]:
            await ctx.channel.send("Sentiment is either 'unspecified', 'positive', or 'negative'!")
            return

        print(
            f"Receive request: (subredditName: {subredditName}, postCount={postCount}, sentiment={sentiment})"
        )

        submissions = reddit.getRedditSubmissions(subredditName, int(postCount), sentiment)

        await ctx.channel.send(
            f"Hi, {ctx.author.display_name}. Here are the {int(postCount)} submissions:"
        )

        for i, submission in enumerate(submissions):
            text = (
                submission.selftext[:150] + "..."
                if len(submission.selftext) > 150
                else submission.selftext
            )
            time = datetime.datetime.fromtimestamp(submission.created_utc)
            embed = discord.Embed(
                title=f"Post {i + 1}: {submission.title}",
                url=submission.url,
                description=text,
                color=discord.Color.blue(),
            )
            embed.set_author(
                name=submission.author.name, icon_url=submission.author.icon_img
            )
            embed.set_footer(text=f"Posted on {time.strftime("%Y-%m-%d %H:%M:%S UTC")}")
            await ctx.channel.send(embed=embed)
        return

    # Now that we've defined how the bot should work, start running your bot
    client.run(keys.discord_token)


if __name__ == "__main__":
    main()
