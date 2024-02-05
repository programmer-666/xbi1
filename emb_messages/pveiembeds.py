# embeds.py

from json import dumps
from discord import Embed, Color


def em_basic_status(pvei_data):
    return Embed(
        title='Test',
        colour=Color.yellow(),
        description='```' + dumps(pvei_data, indent=4) + '```'
    )
