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

bot = commands.Bot(command_prefix = '/')
"""
@bot.command('hi')
async def pun(ctx):
    await ctx.send('hi')

@bot.command('h')
async def help_desc(ctx):
    await ctx.send('help')
"""

@bot.command('pun')
async def pun(ctx):
    pundog = discord.File('pundog.jpeg')
    await ctx.send(file=pundog)

@bot.command('gen')
async def gen_joke(ctx):
    embed=discord.Embed(title='Z čeho se skládá písek?',
        description='Z tatrovky',
        color=discord.Color.blue())
    img = discord.File('pundog.jpeg')
    embed.set_image(url='attachment://pundog.jpeg')
    #embed.add_field(name='Z čeho se skládá písek', value='Z tatrovky', inline=False) 
    await ctx.send(file=img, embed=embed)

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