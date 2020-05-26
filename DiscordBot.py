import json
import os
from discord.ext import commands

DISCORD_TOKEN = os.environ.get('ESPORTAL_LEADERBOARD_DISCORD_TOKEN')
DISCORD_GUILD = os.environ.get('RELIEF_DISCORD_GUILD_ID')

TOKEN = DISCORD_TOKEN

client = commands.Bot(command_prefix='!')


@client.event
async def on_ready():
    print("Bot is ready")


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
async def update(ctx):
    with open('leaderboard.json', encoding='utf-8') as leaderboard_file:
        leaderboard = json.load(leaderboard_file)
        msg_leaderboard = "__***Stats based on 10 latest matches:***__" + '\n' + '\n'

        for k, v in leaderboard.items():
            msg_leaderboard += ('**' + str(k) + ": " + '**' + '\n')
            for m, n in v.items():
                if k == 'Headshot machine':
                    msg_leaderboard += (str(m) + ": " + str(n) + '%' + '\n')
                else:
                    msg_leaderboard += (str(m) + ": " + str(n) + '\n')
            msg_leaderboard += "\n"
    await ctx.channel.purge()
    await ctx.send(f'{msg_leaderboard}')


@client.command()
async def clear(ctx):
    await ctx.channel.purge()


@client.command()
async def stats(ctx, playername):
    with open('playerStats.json', encoding='utf-8') as stat_file:
        stats = json.load(stat_file)

    message = ""
    stat = ""
    value = ""
    for player in stats:
        for k, v in player.items():
            if k == playername:
                for m, n in v.items():
                    if m == "most defuses":
                        stat = "defuses"
                        value = str(n)
                    elif m == "most plants":
                        stat = "plants"
                        value = str(n)
                    else:
                        stat = str(m)
                        value = str(n)
                    message += "**" + stat + "**" + ': ' + value + '\n'

    await ctx.author.send("/////// STATS ////// \n Stats PLAYER **{}**: \n".format(playername) + "{}".format(message))
    await ctx.channel.purge(limit=1)


client.run(TOKEN)
