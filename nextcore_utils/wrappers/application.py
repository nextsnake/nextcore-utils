from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from discord_typings import ApplicationData
    from nextcore.http import BotAuthentication, HTTPClient

from nextcore.http import Route
from ..base_wrapper import BaseWrapper

__all__ = ("Application",)

class Application(BaseWrapper):
    def __init__(self, client: HTTPClient, authentication: BotAuthentication) -> None:
        super().__init__(client, authentication)

    async def get_current_application(self) -> ApplicationData:
        """
        Returns
        -------
        ApplicationData
            The [application](https://discord.com/developers/docs/resources/application#application-object) object associated with the requesting bot user.
        """

        route = Route(
            "GET", 
            "/applications/@me"
        )

        r = await self.client.request(
            route,
            rate_limit_key = self.authentication.rate_limit_key,
            headers = self.authentication.headers,
        )

        return await r.json()