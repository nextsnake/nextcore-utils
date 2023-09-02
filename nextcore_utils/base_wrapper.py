from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from nextcore.http import HTTPClient, BotAuthentication

from abc import ABC

class BaseWrapper(ABC):
    def __init__(self, client: HTTPClient, authentication: BotAuthentication) -> None:
        """
        The base interface of http wrappers.

        Parameters
        ----------
        client:
            Your nextcore http client.
        authentication:
            Your nextcore bot authentication.
        """
        self.client = client
        self.authentication = authentication

        super().__init__()