# embed_templates.py

from discord import Embed

proxmox_url: str = 'https://0.0.0.0:8006'

class InformationalEmbed(Embed):
    def __init__(self, description: str = 'Info', **kwargs):
        super().__init__()

        self.title = 'Informational Notification'
        self.url = proxmox_url
        self.description = description
        self.colour = 0xc65059
        # self.timestamp