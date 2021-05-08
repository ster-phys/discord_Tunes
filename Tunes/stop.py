#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import subprocess

import discord
from discord.ext import commands

class stop():
    def __init__(self,ctx,arg):
        self._ctx = ctx
        self._arg = arg
        self._ROOTPATH = os.path.dirname(os.path.abspath(__file__))
        self._CFGPATH = os.path.dirname(os.path.dirname(self._ROOTPATH))
        self._path = "/tmp/{}.mp3".format(ctx.author.id)

    async def main(self):
        voiceClient = self._ctx.guild.voice_client
        voiceClient.stop()
        os.remove(self._path)
        return
