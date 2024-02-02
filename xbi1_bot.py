# xbi1_bot.py
# :scc:2:1003:

import discord
from discord.ext import commands


intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)


@bot.command(name='test')
async def test(ctx: commands.context.Context, *args):
    await ctx.send(
        embed=discord.Embed(title='Test', description=' '.join(args))
    )
