from discord.ext import commands
from logic import fizz
import requests as rq
import discord.utils
import discord

client = discord.Client()
bot = commands.Bot(command_prefix='noops ', description='Discord hackweek meets noops...')

class Nooper:
    def __init__(self, bot):
        self.bot = bot
        self.noop = fizz()
        self.qlock = False
        self.start = False
        self.question = ''

    @bot.command(pass_context=True, name="start")
    async def _start(self, ctx):
        """
            Start the noops challenge
        """
        if not self.start:
            try:
                noop = self.noop.get_question()
                self.question = noop['message']
                await ctx.send(self.question)
                await ctx.send('Noops challenge started')
                self.start = True
            except Exception as e:
                await ctx.send('something went wong in ask {}'.format(e))
        else:
            await ctx.send('The noops challenge is already running in this server')

    @bot.command(pass_context=True)
    async def ask(self, ctx):
        """
            The noops bot asks you a question.
        """
        try:
            if not self.qlock and self.start:
                noop = self.noop.get_question()
                self.question = noop['message']
                await ctx.send(self.question)
                try:
                    rules = noop['rules']
                    numbers = noop['numbers']
                    await ctx.send('\n Rules {}\n Numbers {}'.format(rules, numbers))
                except:
                    pass
            else:
                await ctx.send('Answer the previous question...\n {}'.format(self.question))
        except Exception as e:
            await ctx.send('something went wong in ask {}'.format(e))

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
            await ctx.send('something went wong in send {}'.format(e))

def setup(bot):
    bot.add_cog(Nooper(bot))
