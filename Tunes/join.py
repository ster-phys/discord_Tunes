#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os

import discord
from discord.ext import commands

class join():
    def __init__(self,ctx,arg):
        self._ctx = ctx
        self._arg = arg
        self._ROOTPATH = os.path.dirname(os.path.abspath(__file__))

    async def main(self):
        # User must be on the voice channel to use the command
        if not self._ctx.author.voice:
            await self._ctx.send("You need to connect to the voice channel.")
            return
        # already connected
        if self._ctx.guild.voice_client:
            await self._ctx.send("Already connected.")
            return
        # connect
        await self._ctx.author.voice.channel.connect()
        await self._ctx.send("Successfully connected.")
        return
