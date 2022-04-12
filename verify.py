import discord
from discord import member
from discord.ext import commands
from dislash import InteractionClient, ActionRow, Button, ButtonStyle

intents = discord.Intents.all()
bot = commands.Bot(command_prefix = "!", intents = intents)
bot.remove_command("help")

inter_client = InteractionClient(bot)

@bot.event
async def on_ready():
    print(f'Вы вошли как {bot.user}')

@bot.command()
@commands.has_role(963037470373593119)
async def verif(ctx):

    emb = discord.Embed(
        description = 
        f"""
        **Добро пожаловать на сервер {ctx.guild.name} <a:welcome:963325186294308864>**,\nНажмите кнопку ниже, чтобы пройти проверку.\nЕсли у вас возникнут какие-либо проблемы с верификацией, сообщите об этом одному из модераторов!
        """,
        colour = 0xFF8C00
    )
    emb.set_thumbnail(url = '')

    row = ActionRow(
        Button(
            style = ButtonStyle.gray,
            label = '🔓',
            custom_id = 'verif_button'
        )
    )
    await ctx.send(embed = emb, components = [row])

@bot.event
async def on_button_click(inter):

    res = 'Вы успешно верифицировались!'
    guild = bot.get_guild(inter.guild.id)

    if inter.component.id == "verif_button":
        verif = guild.get_role(963330670325800981)
        member = inter.author
        await member.add_roles(verif)
        await inter.reply(res, ephemeral = True)
bot.run('OTIxNDg2MzUyMTk1OTMyMjEy.YbznCg.xtGB_nm4mmUuWdPYtiHq63VNSoc')