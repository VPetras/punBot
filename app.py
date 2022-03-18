#!/usr/bin/env python3
# -*- coding: utf-8 -*-

##################################################
# Discord BOT
# Title: Discord Bot for cringe jokes
# Author: Vojtěch Petrásek 
# Generated: 18/03/2022 20:55:01
##################################################

###
# imports
###

import asyncio
import os
import sys

import discord
from discord.ext import commands

bot = commands.Bot(command_prefix = "/")

@bot.command("hi")
async def pun(ctx):
    await ctx.send("hi")

@bot.event
async def on_ready():
    print(f'{bot.user} has connected to Discord!')

if __name__ == '__main__':
    try:
        with open('token') as t:
            token = t.readline()
            print(token)
        t.close()
        bot.run(token)
    except Exception as e:
        print('Exited with error: {}'.format(e))
        sys.exit(1)