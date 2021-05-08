#!/usr/bin/env python
# -*- coding: utf-8 -*-

import discord
from discord.ext import commands

import config

# Get TOKEN
TOKEN = config.DISCORD_TOKEN

# Bot setting
commandPrefix = '?'
bot = commands.Bot(command_prefix=commandPrefix)
bot.remove_command("help")

# Operation at startup
@bot.event
async def on_ready():
    print("Logged in as {} ({})".format(bot.user.name,bot.user.id))

# Ignore commands from bots
@bot.event
async def from_bot(ctx):
    if ctx.author.bot:
        return

## Template to here

import Tunes

@bot.group()
async def tunes(ctx):
    if ctx.invoked_subcommand is None:
        await ctx.send("Invalid tunes command passed...")

@tunes.command()
async def join(ctx,*,arg=""):
    await Tunes.join(ctx,arg).main()
    return

@tunes.command()
async def leave(ctx,*,arg=""):
    await Tunes.leave(ctx,arg).main()
    return

@tunes.command()
async def play(ctx,*,arg=""):
    await Tunes.play(ctx,arg).main()
    return

@tunes.command()
async def stop(ctx,*,arg=""):
    await Tunes.stop(ctx,arg).main()
    return

bot.run(TOKEN)
