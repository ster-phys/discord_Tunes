#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import re
import subprocess

import discord
from discord.ext import commands

class play():
    def __init__(self,ctx,arg):
        self._ctx = ctx
        self._arg = re.match(r"https://youtu.be/.{11}", arg).group()
        self._ROOTPATH = os.path.dirname(os.path.abspath(__file__))
        self._CFGPATH = os.path.dirname(os.path.dirname(self._ROOTPATH))
        self._path = "/tmp/{}.mp3".format(ctx.author.id)

    async def main(self):
        # User must be on the voice channel to use the command
        if not self._ctx.author.voice:
            await self._ctx.send("You need to connect to the voice channel.")
            return

        # check connection
        if not self._ctx.guild.voice_client:
            await self._ctx.send("There is no connection.")
            return

        # Need URL
        if not self._arg:
            await self._ctx.send("`{}tunes play https://youtu.be/XXXXXXXXXXX`".format(self._ctx.prefix))
            return

        # Download from youtube
        cmd = "youtube-dl -o {} -x -f bestaudio --audio-format mp3 --audio-quality 0 {}".format(self._path.replace("mp3","%(ext)s"), self._arg).split()
        subprocess.check_call(cmd)

        # Send to Voice Channnel
        audioSource = discord.FFmpegPCMAudio(self._path)
        voiceClient = self._ctx.guild.voice_client
        voiceClient.play(audioSource)
        return
