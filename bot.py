import discord
from discord.ext import commands, tasks
import datetime
import asyncio
import mysql.connector



colors = discord.Color
bot = commands.Bot(command_prefix='g!')
mycursor = mydb.cursor(buffered=True)

mydb = mysql.connector.connect(
    host="89.37.194.114",
    user="testuser",
    password="h=ik.vREx+EMWuNyim!Zsd.c",
    database="communities_test"
)

guilds = []


@bot.event
async def on_ready():
    print('logged in as')
    # print(CLIENT.user.name)
    print(bot.user.name)
    await bot.change_presence(activity=discord.Activity(name="Testtiiing", type=1))
    if mydb:
        print('Mysql connection successfull')
    print('Done!')



@bot.command()
async def test(message, arg1, *, arg2):
    await message.send('You passed {} and the rest is {}'.format(arg1, arg2))
    print(message.author)
    print(message.message)
    print(message.guild)

@tasks.loop(seconds=60)
async def check_activity(self):
    for guild in guilds:
        for vc in guild.voice_channels:
            for member in vc.members:
                sql_search = "SELECT * FROM users WHERE member_id = '{}' AND guild_id = '{}' "
                mycursor.execute(sql_search.format(str(member.id), str(guild.id)))
                record = mycursor.fetchone()
                if not record:
                    sql_query = "INSERT INTO users (member_id, messages, voice_mins, guild_id) VALUES ('{}', '{}', '{}', '{}')"
                    mycursor.execute(sql_query.format(str(member.id), 0, 0, str(guild.id)))
                    mydb.commit()
                sql_query = "UPDATE users SET voice_mins = voice_mins + 1 WHERE member_id = '{}' AND guild_id = '{}' "
                mycursor.execute(sql_query.format(str(member.id), str(guild.id)))
                mydb.commit()
            




bot.run('NjY4Mjc2Mjk1ODUwOTE3OTE4.XiO6zA.l7LV6fRbvDpFGuNkkS5DlFPSpSk'
