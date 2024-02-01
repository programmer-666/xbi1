# xbi1_dcbot.__init__.py
# :scc:2:1003:
import discord
from discord.ext import commands


intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)


class MyBot(commands.Bot):
    @bot.command(name='test')
    async def test(self, ctx: commands.context.Context, *args):
        await ctx.send(embed=discord.Embed(title='Test', description=' '.join(args)))


bot.run('')
