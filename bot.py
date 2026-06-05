import discord

from discord import app_commands

from discord.ext import commands

import yt_dlp

import os



# إعدادات البوت

intents = discord.Intents.default()

bot = commands.Bot(command_prefix="!", intents=intents)



@bot.event

async def on_ready():

    # مزامنة أوامر السلاش مع ديسكورد

    await bot.tree.sync()

    print(f'تم تسجيل الدخول كـ {bot.user} وتمت مزامنة أوامر السلاش!')



@bot.tree.command(name="download", description="تحميل فيديو من رابط")

@app_commands.describe(url="ضع رابط الفيديو هنا")

async def download(interaction: discord.Interaction, url: str):

    await interaction.response.send_message("جاري المعالجة، يرجى الانتظار...")

    

    ydl_opts = {

        'format': 'best',

        'outtmpl': 'video.mp4',

    }

    

    try:

        with yt_dlp.YoutubeDL(ydl_opts) as ydl:

            ydl.download([url])

        

        # إرسال الملف

        await interaction.followup.send(file=discord.File('video.mp4'))

        os.remove('video.mp4')

    except Exception as e:

        await interaction.followup.send(f"حدث خطأ: {e}")



import os
# احذف السطر الذي فيه التوكن وضع مكانه:
bot.run(os.getenv('MTQ2NDUzMzU1MjUwMTYyMDgxOQ.GkF1Vp.BHe5AUVVvw42rjNUZDmAoKltLgOlYICd7nm0eU'))