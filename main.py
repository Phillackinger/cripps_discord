import discord
import random
import time
import os
from dotenv import load_dotenv

load_dotenv()

client = discord.Client()

GPquotes=[
    "One time, I almost helped a clown steal an elephant...",
    "When you get too old to fight, what choice have you got? It's either work or beg and I'd rather work.",
    "Guy claimed he couldn't speak, talked in his sleep.",
    "Did I ever tell you about that bank job in Tennessee. It was me,  Limpy Pete and Phil the Crab. Managed to get ourselfs locked in the safe. After a weekend of nature callin' the stench in there nocked the clerk on his back when he opend the door and we managed to escape. Neither Pete nor Phil were very good runners. They good picket up at the end of town and hanged the next day, which seemed harsh to me.",
]

LeaveQuotes=[
    "Don't do anything I wouldn't.",
]

JoinQuotes=[
    "Howdy, partner!",
    "The wanderer returns.",
    "There you are. Queen of the supply runs"
]

DogQuotes=[
    "You won't catch me petting that thing.",
    "Don't be surprised when that dog turns on you and rips your face off.",
    "I'd rather pet a pig"
]

TauraQuotes=[
    "I'd pet that thing.",
    "The cute one?",
]

AcyQuotes=[
    "The plant Lady? I'm not into that stuff but she's lookin' fine!",
]

@client.event
async def on_message(message: discord.message):
    if message.author == client.user:
        return
    
    if 'cripps' in message.content.lower():
        await message.channel.send(random.choice(GPquotes))
        sleep()

    if 'leave' in message.content.lower():
        await message.channel.send(random.choice(LeaveQuotes))
        sleep()

    if 'join' in message.content.lower():
        await message.channel.send(random.choice(JoinQuotes))
        sleep()

    if 'dog' in message.content.lower():
        await message.channel.send(random.choice(DogQuotes))
        sleep()

    if 'taura' in message.content.lower():
        await message.channel.send(random.choice(TauraQuotes))
        sleep()

    if 'acy' in message.content.lower():
        await message.channel.send(random.choice(AcyQuotes))
        sleep()

def sleep():
    time.sleep(0)

client.run(os.getenv('KEY'))