import asyncio

import discord

from datetime import datetime,timedelta

class Player:
    """
    Base player class for Werewolf game
    """

    def __init__(self, member: discord.Member):
        self.user = member
        self.role = None
        self.id = None
        
        self.alive = True
        self.muted = False
        self.protected = False
        
    async def assign_role(self, role):
        """
        Give this player a role
        """
        role.player = self
        self.role = role