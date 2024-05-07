import discord
import api_keys as keys
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

    # Adds a command called hello to the bot. Can be accessed through typing $hello on discord server
    @client.tree.command(name= "hello", description= "Prints hellow world")
    async def hello(ctx: discord.Interaction):
        await ctx.channel.send("Hello world!")

    # Now that we've defined how the bot should work, start running your bot
    client.run(keys.discord_token)

if __name__ == '__main__':
    main()


