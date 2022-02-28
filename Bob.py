from ctypes.wintypes import PINT
from distutils import command
import discord
from discord.ext import commands
import time 
import asyncio 
import  os
import requests
import json
import random
###################################################################
bot=commands.Bot(command_prefix='')
####################################################################

sad_words = ["sad" , "เศร้า" ,"แย่","Sad" ]

starter_encouragemenst = [
          "อย่าจมปักกับความรู้สึกที่เลวร้าย เพราะมันจะทำให้เราไม่เดินไปไหน by Bob",                      "อย่าคิดแบบนั้นดิ!",
          "ชีวิตเรานั้นมีค่า ยิ่งกว่าละคร ฉะนั้นอย่ายอมแพ้ให้กับอุปสรรคเพียงเล็กน้อย.-bob",
          "จง ลุกขึ้น! แล้วก้าวต่อไปครับ"
]

good_words=["thank ", "thx", "Thx", "Thank", "ดี", "ขอบคุณ", "Feel good", "feel good"]

starter_yui =[
          "ต้องอย่างนั้นสิ!",
          "ไม่เป็นไรแค่นี้เอง"
      ]    

##################################
def get_quote( ):
	reponse =  requests.get   ('http://zenquotes.io/api/random')
	json_data = json.loads(reponse.text)
	quote = json_data [0] ['q']  + " -"  + json_data [0] ['a']
	return (quote)
	       

##################################
@bot.event
async def on_ready():
	print('{0.user} is ready'.format(bot))
####################################################################
@bot.event
async def on_message(message):   
    channel = message.channel
   
    msg = message.content
    
    if msg.startswith('inspire' ):
        quote = get_quote( )
        await message.channel.send (quote)
        


    if any (word in msg for word in sad_words):
            await message.channel.send(random.choice (starter_encouragemenst ))
   
    if any (word in msg for word in good_words):
           await message.channel.send(random.choice(starter_yui))
           

           	
           
    if msg.startswith('Hello bob'):
        await message.channel.send('Hello! ')
    if msg.startswith('Say') :
        await message.channel.send('ว่าไงครับ')
    if msg.startswith('Ping'):
        await message.channel.send('Pong!')
    if msg.startswith('Bye bob'):
       await message.channel.send ('Bye!')
    if 'hbd' in msg.lower():
        await message.channel.send('Happy Birthday! 🎈🎉')
        await message.channel.send('Happy Birthday! 🎈🎉')
        await message.channel.send('Happy Birthday! 🎈🎉')
        return

              
    if msg.startswith('Thumb'):
        channel = message.channel
        await channel.send('กด 👍 ให้หน่อย ครับ')

        def check(reaction, user):
            return user == message.author and str(reaction.emoji) == '👍'

        try:
            reaction, user = await bot.wait_for('reaction_add', timeout=10.0, check=check)
        except asyncio.TimeoutError:
            await channel.send('👎')
            await channel.send('ทำไมถึงปล่อยให้ฉันรอ')
        else:
            await channel.send('👍')
#################################

bot.run(os.environ['TOKEN'])