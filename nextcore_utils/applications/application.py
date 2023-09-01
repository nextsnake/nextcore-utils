from __future__ import annotations
from typing import TYPE_CHECKING

from nextcore.http import Route

if TYPE_CHECKING:
    from discord_typings import ApplicationData
    from nextcore.http import BotAuthentication, HTTPClient

__all__ = ("me",)

async def me(client: HTTPClient, authentication: BotAuthentication) -> ApplicationData:
    """
    Parameters
    ----------
    client:
        Your nextcore http client.
    authentication:
        Your nextcore bot authentication.

    Returns
    -------
    ApplicationData
        The [application](https://discord.com/developers/docs/resources/application#application-object) object associated with the requesting bot user.
    """

    route = Route(
        "GET", 
        "/applications/@me"
    )

    r = await client.request(
        route,
        rate_limit_key = authentication.rate_limit_key,
        headers = authentication.headers,
    )

    return await r.json()