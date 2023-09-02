from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from typing import List
    from nextcore.http import BotAuthentication, HTTPClient
    from discord_typings import AutoModerationRuleData, Snowflake

from nextcore.http import Route
from ..base_wrapper import BaseWrapper

__all__ = ("AutoModeration",)

class AutoModeration(BaseWrapper):
    def __init__(self, client: HTTPClient, authentication: BotAuthentication) -> None:
        super().__init__(client, authentication)

    async def list_auto_moderation_rules(
        self,
        guild_id: Snowflake
        ) -> List[AutoModerationRuleData]:
        """
        Get a list of all rules currently configured for the guild. 
        This endpoint requires the ``MANAGE_GUILD`` permission.

        Parameters
        ----------
        guild_id:
            The ID of the guild.

        Returns
        -------
        AutoModerationRuleData
            Returns a list of [auto moderation rule](https://discord.com/developers/docs/resources/auto-moderation#auto-moderation-rule-object) 
            objects for the given guild.
        """

        route = Route(
            "GET", 
            "/guilds/{guild_id}/auto-moderation/rules",
            guild_id = guild_id
        )

        r = await self.client.request(
            route,
            rate_limit_key = self.authentication.rate_limit_key,
            headers = self.authentication.headers,
        )

        return await r.json()


    # TODO: Add Get, Create, Modify and Delete Auto Moderation Rule