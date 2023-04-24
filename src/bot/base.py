from abc import ABC, abstractmethod
import discord
from .exceptions import FailedToJoinChannel
import os


class AbstractBot:

    def __init__(self) -> None:
        self.client = discord.Client(intents=discord.Intents.all())
        self._join_events()

    def run(self):
        self.client.run("MTA5Mjk0MDg4NDk5NzMxNjczMg.GcNRB_.sBGMtV5qozhDicsSCKsGhZXFIicGD-ePCulbVI")

    async def join_channel(self, channel_id : int):
        voice_client = await self.client.get_channel(channel_id).connect()
        return voice_client

    async def send_message(self, channel_id : int, message : str):
        channel = self.client.get_channel(channel_id)
        if channel.type == discord.ChannelType.text:
            await channel.send(message)
            return True

        raise Exception("Is not a voice channel")

    def _join_events(self):
        @self.client.event
        async def on_ready():
            await self.on_ready()

        @self.client.event
        async def on_message(msg : discord.Message, ):
            await self.on_message(msg)
        
    @abstractmethod
    async def on_ready(self):
        pass

    @abstractmethod
    async def on_message(self, msg : discord.Message):
        pass

    def getClient(self):
        return self.client
