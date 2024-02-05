# datacs.py
from discord.ext import commands


class PVEICog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='testx')
    async def testx(self, ctx):
        await ctx.send('HelloWorld')


def setup(bot):
    bot.add_cog(PVEICog(bot))
