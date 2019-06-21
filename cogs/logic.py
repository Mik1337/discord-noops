from discord.ext import commands
from fizzbot import fizz
import requests as rq
import discord.utils
import discord

class Nooper:
    def __init__(self, bot):
        self.bot = bot
        self.noop = fizz()
        self.qlock = False
        self.question = ''

    @bot.command(pass_context=True)
    async def ask(self, ctx, *, message):
        """
            The noops bot asks you a question.
        """
        try:
            if not qlock:
                self.question, next_question = self.noop.get_question()
                await ctx.send(self.question)
            else:
                await ctx.send('Answer the previous question...\n {}'.format(self.question))
        except Exception as e:
            await ctx.send('something went wong {}'.format(e))

    @bot.command(pass_context=True)
    async def send(self, ctx, *, message):
        """
            You answer the noops bot's question.
        """
        try:
            code = self.noop.send_answer(message)
            if code['result'] == 'correct':
                await ctx.send("{}".format(code['message']))
                self.qlock = False
            else:
                await ctx.send("incorrect answer, try again... \n QUESTION \n{}".format(self.question))
                self.qlock = True
        except Exception as e:
            await ctx.send('something went wong {}'.format(e))

def setup(bot):
    bot.add_cog(Nooper(bot))
