import discord
from discord.ext import commands
import os
import google.generativeai as genai
from flask import Flask, render_template
from threading import Thread
app = Flask('')
@app.route('/')
def home():
  return "bot python is online!"
def index():
  return render_template("index.html")
def run():
  app.run(host='0.0.0.0', port=8080)
def high():
  t = Thread(target=run)
  t.start()
  
high()  
token = os.environ.get('bot')


bot = commands.Bot(
    command_prefix='>',
    help_command=None,
    intents=discord.Intents.all(),
    strip_after_prefix=True,
    case_insensitive=True, 
)

genai.configure(api_key="AIzaSyBFcXa1SDd_bJLv43XOBPWv0LefTv_H_NI")

model = genai.GenerativeModel('gemini-pro',
	safety_settings = [
    {
        "category": "HARM_CATEGORY_DANGEROUS",
        "threshold": "BLOCK_NONE",
    },
    {
        "category": "HARM_CATEGORY_HARASSMENT",
        "threshold": "BLOCK_NONE",
    },
    {
        "category": "HARM_CATEGORY_HATE_SPEECH",
        "threshold": "BLOCK_NONE",
    },
    {
        "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
        "threshold": "BLOCK_NONE",
    },
    {
        "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
        "threshold": "BLOCK_NONE",
    },
	]
	)


@bot.event
async def on_ready():
  print(f"Bot {bot.user.name} is ready!")
  await bot.change_presence(activity=discord.Streaming(
      name='Black Market!', url='https://www.twitch.tv/example_channel'))


@bot.command(name = "bmkai")
async def bmkai(ctx: commands.Context, *, prompt: str):
	response = model.generate_content(prompt)

	await ctx.reply(response.text)

bot.run(token)
