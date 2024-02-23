# embed_templates.py

from discord import Embed
from typing import Optional, Any, Self
from datetime import datetime


class InformationalEmbed(Embed):
    _defaults: dict = {
        'description': 'Info',
        'colour': 0x051453,
        'url': 'https://0.0.0.0:8006',
        'title': 'Informational Notification',
        'author_name': 'XBI1 - Notification Bot',
        'author_url': 'https://github.com/programmer-666/xbi1',
        'author_icon_url': 'https://cdn.discordapp.com/app-icons/' \
            + '1176948443839737996/4750381453e4a1b72513529c8cbe4423.png',
        'thumbnail': 'https://cdn.discordapp.com/attachments/121054285254' \
            + '7809320/1210543709913878638/information-image.png?ex=' \
            + '65eaf1af&is=65d87caf&hm=a6dc8ba27b265d61bc773832650a69060' \
            + '0ade267c72ce54312a60c97a30b600f&',
        'image_url': 'https://cdn.discordapp.com/app-icons/' \
            + '1176948443839737996/4750381453e4a1b72513529c8cbe4423.png',
        'footer_text': 'Footer',
        'footer_icon_url': 'https://cdn.discordapp.com/app-icons/' \
            + '1176948443839737996/4750381453e4a1b72513529c8cbe4423.png'
    }

    def __init__(
        self,
        title: Optional[Any] = _defaults['title'],
        url: Optional[Any] = _defaults['url'],
        colour: Optional[Any] = _defaults['colour'],
        description: Optional[Any] = _defaults['description'],
        timestamp=datetime.now()
    ):
        super().__init__()

        self.title = title
        self.url = url
        self.colour = colour
        self.description = description
        self.timestamp = timestamp

    def set_author(
        self,
        *,
        name: Any = _defaults['author_name'],
        url: Optional[Any] = _defaults['author_url'],
        icon_url: Optional[Any] = _defaults['author_icon_url']
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
        *,
        url: Optional[Any] = _defaults['thumbnail']
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
        *,
        url: Optional[Any] = _defaults['image_url']
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
        *,
        text: Optional[Any] = _defaults['footer_text'],
        icon_url: Optional[Any] = _defaults['footer_icon_url']
    ) -> Self:

        self._footer = {}
        if text is not None:
            self._footer['text'] = str(text)

        if icon_url is not None:
            self._footer['icon_url'] = str(icon_url)

        return self


class WarningEmbed(Embed):
    _defaults: dict = {
        'description': 'Warning',
        'colour': 0xFFFF00,
        'url': 'https://0.0.0.0:8006',
        'title': 'Warning Notification',
        'author_name': 'XBI1 - Notification Bot',
        'author_url': 'https://github.com/programmer-666/xbi1',
        'author_icon_url': 'https://cdn.discordapp.com/app-icons/' \
            + '1176948443839737996/4750381453e4a1b72513529c8cbe4423.png',
        'thumbnail': 'https://cdn.discordapp.com/attachments/1210542852547809320/1210574389800603698/warning-thumbnail.png?ex=65eb0e41&is=65d89941&hm=d5e20772ead94ed9ab58a5ce0ef9d40e9608f2e2d52e02e71c63463d61a43602&',
        'image_url': 'https://cdn.discordapp.com/app-icons/' \
            + '1176948443839737996/4750381453e4a1b72513529c8cbe4423.png',
        'footer_text': 'Footer',
        'footer_icon_url': 'https://cdn.discordapp.com/app-icons/' \
            + '1176948443839737996/4750381453e4a1b72513529c8cbe4423.png'
    }

    def __init__(
        self,
        title: Optional[Any] = _defaults['title'],
        url: Optional[Any] = _defaults['url'],
        colour: Optional[Any] = _defaults['colour'],
        description: Optional[Any] = _defaults['description'],
        timestamp=datetime.now()
    ):
        super().__init__()

        self.title = title
        self.url = url
        self.colour = colour
        self.description = description
        self.timestamp = timestamp

    def set_author(
        self,
        *,
        name: Any = _defaults['author_name'],
        url: Optional[Any] = _defaults['author_url'],
        icon_url: Optional[Any] = _defaults['author_icon_url']
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
        *,
        url: Optional[Any] = _defaults['thumbnail']
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
        *,
        url: Optional[Any] = _defaults['image_url']
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
        *,
        text: Optional[Any] = _defaults['footer_text'],
        icon_url: Optional[Any] = _defaults['footer_icon_url']
    ) -> Self:

        self._footer = {}
        if text is not None:
            self._footer['text'] = str(text)

        if icon_url is not None:
            self._footer['icon_url'] = str(icon_url)

        return self


class SuccessEmbed(Embed):
    _defaults: dict = {
        'description': 'Success',
        'colour': 0x386b38,
        'url': 'https://0.0.0.0:8006',
        'title': 'Success Notification',
        'author_name': 'XBI1 - Notification Bot',
        'author_url': 'https://github.com/programmer-666/xbi1',
        'author_icon_url': 'https://cdn.discordapp.com/app-icons/' \
            + '1176948443839737996/4750381453e4a1b72513529c8cbe4423.png',
        'thumbnail': 'https://cdn.discordapp.com/attachments/1210542852547809320/1210578330697334845/success-stabil-thumbnail.png?ex=65eb11ed&is=65d89ced&hm=5a4aa7e146a126f9d638471177585219e71d033d2ba8ff2602929865a77a2d18&',
        'image_url': 'https://cdn.discordapp.com/app-icons/' \
            + '1176948443839737996/4750381453e4a1b72513529c8cbe4423.png',
        'footer_text': 'Footer',
        'footer_icon_url': 'https://cdn.discordapp.com/app-icons/' \
            + '1176948443839737996/4750381453e4a1b72513529c8cbe4423.png'
    }

    def __init__(
        self,
        title: Optional[Any] = _defaults['title'],
        url: Optional[Any] = _defaults['url'],
        colour: Optional[Any] = _defaults['colour'],
        description: Optional[Any] = _defaults['description'],
        timestamp=datetime.now()
    ):
        super().__init__()

        self.title = title
        self.url = url
        self.colour = colour
        self.description = description
        self.timestamp = timestamp

    def set_author(
        self,
        *,
        name: Any = _defaults['author_name'],
        url: Optional[Any] = _defaults['author_url'],
        icon_url: Optional[Any] = _defaults['author_icon_url']
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
        *,
        url: Optional[Any] = _defaults['thumbnail']
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
        *,
        url: Optional[Any] = _defaults['image_url']
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
        *,
        text: Optional[Any] = _defaults['footer_text'],
        icon_url: Optional[Any] = _defaults['footer_icon_url']
    ) -> Self:

        self._footer = {}
        if text is not None:
            self._footer['text'] = str(text)

        if icon_url is not None:
            self._footer['icon_url'] = str(icon_url)

        return self
