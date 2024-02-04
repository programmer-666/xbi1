# datacs.py
import discord
from discord.ext import commands


class PVEICommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
