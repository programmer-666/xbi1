# embed_templates.py

from discord import Embed
from typing import Optional, Any, Self


class InformationalEmbed(Embed):
    __def_description: str = 'Info'
    __def_colour: hex = 0xc65059
    __def_url: str = 'https://0.0.0.0:8006'
    __def_title: str = 'Informational Notification'

    __def_author_name: str = 'XBI1 - Notification Bot'
    __def_author_url: str = 'https://github.com/programmer-666/xbi1'
    __def_author_icon_url: str = 'https://cdn.discordapp.com/app-icons/'\
        + '1176948443839737996/4750381453e4a1b72513529c8cbe4423.png?size=256'

    __def_thumbnail: str = __def_author_icon_url

    __def_image: str = __def_author_icon_url
    # default values

    def __init__(
        self,
        title: Optional[Any] = __def_title,
        url: Optional[Any] = __def_url,
        colour: Optional[Any] = __def_colour,
        description: Optional[Any] = __def_description,
    ):
        super().__init__()

        self.title = title
        self.url = url
        self.colour = colour
        self.description = description

    def set_author(
        self,
        name: Any = __def_author_name,
        url: Optional[Any] = __def_author_url,
        icon_url: Optional[Any] = __def_author_icon_url
    ) -> Self:

        self._author = {
            'name': str(name),
        }

        if url is not None:
            self._author['url'] = str(url)

        if icon_url is not None:
            self._author['icon_url'] = str(icon_url)

        return self

    def set_thumbnail(
        self,
        url: Optional[Any] = __def_thumbnail
    ) -> Self:
        if url is None:
            try:
                del self._thumbnail
            except AttributeError:
                pass
        else:
            self._thumbnail = {
                'url': str(url),
            }
        return self

    def set_image(
        self,
        url: Optional[Any] = __def_image
    ) -> Self:

        if url is None:
            try:
                del self._image
            except AttributeError:
                pass
        else:
            self._image = {
                'url': str(url),
            }

        return self

    def set_footer(
        self,
        text: Optional[Any] = None,
        icon_url: Optional[Any] = None
    ) -> Self:

        self._footer = {}
        if text is not None:
            self._footer['text'] = str(text)

        if icon_url is not None:
            self._footer['icon_url'] = str(icon_url)

        return self
