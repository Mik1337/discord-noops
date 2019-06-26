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
        self.example_format = "POST your answer back to this URL in JSON format. If you are having difficulties, see the exampleResponse provided."
        self.rule_format = """\n\n{\n  "answer": "1 2 Fizz 4 Buzz"\n}"""

        # self.question = ''

    @bot.command(pass_context=True, name="start")
    async def _start(self, ctx):
        """
            Start the noops challenge
        """
        if not self.start:
            try:
                noop = await self.noop.get_question()
                # question = noop['message']
                # await ctx.send(question)
                await ctx.send(':rotating_light::rotating_light: :regional_indicator_n: :regional_indicator_o: :regional_indicator_o:  :regional_indicator_p: :regional_indicator_s:        :regional_indicator_c: :regional_indicator_h: :a: :regional_indicator_l: :regional_indicator_l: :regional_indicator_e: :regional_indicator_n: :regional_indicator_g: :regional_indicator_e:        :regional_indicator_s: :regional_indicator_t: :a: :regional_indicator_r: :regional_indicator_t: :regional_indicator_e: :regional_indicator_d: :rotating_light::rotating_light:')
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
                noop = await self.noop.get_question()
                question = noop['message']
                try:
                    question = question.replace(self.example_format, " ")
                    question = question.replace(self.rule_format, "\n``noops say 1 2 Fizz 4 Buzz``")
                except Exception:
                    pass
                await ctx.send("```{}```".format(question))
                try:
                    rules = noop['rules']
                    numbers = noop['numbers']
                    await ctx.send('\n Rules ```{}```\n Numbers ```{}```'.format(rules, numbers))
                except:
                    pass
            else:
                await ctx.send("Answer the previous question... or start the game\n")
        except Exception as e:
            await ctx.send('something went wong in ask {}'.format(e))

    @bot.command(pass_context=True)
    async def say(self, ctx, *, message):
        """
            You answer the noops bot's question.
        """
        try:
            code = await self.noop.send_answer(message)
            if code['result'] == 'correct':
                await ctx.send("{}".format(code['message']))
                self.qlock = False
            else:
                await ctx.send("incorrect answer, try again... \n ps: check for missing values and typos")
                self.qlock = True
        except Exception as e:
            await ctx.send('something went wong in send {}'.format(e))

def setup(bot):
    bot.add_cog(Nooper(bot))
