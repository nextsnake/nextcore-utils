from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from typing import Dict
    from discord_typings import AuditLogData, Snowflake
    from nextcore.http import BotAuthentication, HTTPClient

from nextcore.http import Route
from ..base_wrapper import BaseWrapper

__all__ = ("AuditLog",)

class AuditLog(BaseWrapper):
    def __init__(self, client: HTTPClient, authentication: BotAuthentication) -> None:
        super().__init__(client, authentication)

    async def get_guild_audit_log(
        self,
        guild_id: Snowflake,

        user_id: Snowflake = None,
        action_type: int = None,
        before: Snowflake = None,
        after: Snowflake = None,
        limit: int = None,

        **kwargs
    ) -> AuditLogData:
        """
        Parameters
        ----------
        guild_id:
            The ID of the guild.
        user_id:
            Entries from a specific user ID.
        action_type:
            Entries for a specific audit log event.
        before:
            Entries with ID less than a specific audit log entry ID.
        after:
            Entries with ID greater than a specific audit log entry ID.
        limit:
            Maximum number of entries (between 1-100) to return, defaults to 50.

        Returns
        -------
        AuditLogData
            Returns an [audit log](https://discord.com/developers/docs/resources/audit-log#audit-log-object) object for the guild.
            Requires the [VIEW_AUDIT_LOG](https://discord.com/developers/docs/topics/permissions#permissions-bitwise-permission-flags) permission.
        """
        query_params: Dict[str, Snowflake | int] = {}

        if user_id is not None:
            query_params["user_id"] = user_id

        if action_type is not None:
            query_params["action_type"] = action_type

        if before is not None:
            query_params["before"] = before

        if after is not None:
            query_params["after"] = after

        if limit is not None:
            query_params["limit"] = limit

        query_params.update(kwargs)

        route = Route(
            "GET", 
            "/guilds/{guild_id}/audit-logs",
            guild_id = guild_id
        )

        r = await self.client.request(
            route,
            rate_limit_key = self.authentication.rate_limit_key,
            headers = self.authentication.headers,
            params = query_params
        )

        return await r.json()