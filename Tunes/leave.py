#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os

import discord
from discord.ext import commands

class leave():
    def __init__(self,ctx,arg):
        self._ctx = ctx
        self._arg = arg
        self._ROOTPATH = os.path.dirname(os.path.abspath(__file__))

    async def main(self):
        # check connection
        if not self._ctx.guild.voice_client:
            await self._ctx.send("There is no connection.")
            return
        # disconnect
        await self._ctx.guild.voice_client.disconnect()
        await self._ctx.send("Successfully disconnected.")
        return
