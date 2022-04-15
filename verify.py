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
        **Добро пожаловать на дискорд сервер {ctx.guild.name}!! <a:welcome:963325186294308864>**,\n
Для получения доступа к серверу, вам необходимо пройти верификацию, нажав кнопку ниже.\n\n
После верификации мы вам настоятельно рекоменудем прочитать правила нашего сервера.\n\nТак же для навигации по серверу советуем посетить чат информация.\n\n
Желаем вам хорошего времяпрепровождения на нашем сервере!
        """,
        colour = 0xFE3F48
    )
    emb.set_image(url = 'https://cdn.discordapp.com/attachments/963037714414972999/964441522516922388/Welcome.png')

    row = ActionRow(
        Button(
            style = ButtonStyle.gray,
            label = '✅ Пройти верификацию',
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
bot.run('OTIyNTc4ODg2MTA0MDU1ODY4.YcDgiw.-h1KhU_Q55jH1wVPEmMnIUrnVng')
