import os
import Stats
import Update
from discord.ext import commands, tasks

DISCORD_TOKEN = os.environ.get('ESPORTAL_LEADERBOARD_DISCORD_TOKEN')
DISCORD_GUILD = os.environ.get('RELIEF_DISCORD_GUILD_ID')

TOKEN = DISCORD_TOKEN

client = commands.Bot(command_prefix='!')

channelID = int(os.environ.get('RELIEF_LEADERBOARD_CHANNEL_ID'))

nameList = ["microstatic", "Lime", "MatroseN", "Plixz"]

update = Update.Update()


@client.event
async def on_ready():
    print("Bot is ready")
    channel = client.get_channel(channelID)
    await channel.purge()
    await channel.send(f'{update.composeAndGetMessage()}')
    updateLeaderboard.start()


@client.event
async def on_member_join(member):
    print(f'{member} has joined the server.')


@client.event
async def on_member_remove(member):
    print(f'{member} has left the server')


@client.command()
async def ping(ctx):
    await ctx.send(f'Pong! {round(client.latency * 1000)}ms')


@client.command()
async def clear(ctx):
    await ctx.channel.purge()


@tasks.loop(minutes=1)
async def updateLeaderboard():
    if update.checkForUpdate():
        channel = client.get_channel(channelID)
        await channel.purge()
        await channel.send(f'{update.composeAndGetMessage()}')


@client.command()
async def stats(ctx, playername):
    inputPlayerName = playername
    stats = Stats.Stats("playerStats.json", playername, nameList)

    if stats.checkIfNameExists():
        await ctx.author.send("/////// STATS ////// \n Stats PLAYER **{}**: \n".format(playername) + "{}".format(stats.messagePlayerStats()))
        await ctx.channel.purge(limit=1)
    else:
        if (len(inputPlayerName)) < 4:
            await ctx.author.send("Type at least 4 characters!" + '\n' + "Try again!")
        else:
            await ctx.author.send("PLAYER **{}**: Not found".format(inputPlayerName) + '\n' + "Try again!")
            await ctx.channel.purge(limit=1)

client.run(TOKEN)
