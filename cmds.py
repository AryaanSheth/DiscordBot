import discord
from discord.ext import commands
import random
import asyncio


client = commands.Bot(command_prefix="-")

anime_list = ["Aquarion Evol", "Bakemonogatari", "C: The Money of Soul and Possibility Control", "D-Frag!",
              "Made in the Abyss", "Darling in the Franxx", "From the New World - Shinsekai Yori", "Naruto", "Attack on titan",
              "Rising of the Shield Hero", "Dororo", "Parasyte - the maxim-",
              "Nekopara", "Astro Lost in Space", "Isekai Quartet", "Somali and the Forest Spirit", "Naruto Shippuden",
              "Steins;Gate", "Darwins Game",
              "Noragami", "K-On!", "My Hero Academia", "Goblin Slayer", "In/Spectre", "Blue Exorcist",
              "No Game No Life", "Radiant", "Dr.Stone", "Demon Slayer",
              "Violet Evergarden", "HunterxHunter", "Seven Deadly Sins", "Gurren Lagann", "Re:Zero", "One-Punch Man",
              "Kaguya-Sama: Love is War", "Assassination Classroom", "Promised Neverland",
              "Black Clover", "Kakegurui – Compulsive Gambler", "Black Butler"]

def int_keys(users):
    new_users = {}
    for key, value in users.items():
        new_users[int(key)] = value
    return new_users

@client.event
async def on_ready():
    print("Bot Ready")
    print("---------")

class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged in as')
        print(self.user.name)
        print(self.user.id)
        print('------')

    async def on_message(self, message):
        # we do not want the bot to reply to itself
        if message.author.id == self.user.id:
            return

        # roll Game
        if message.content.startswith('-roll'):
            await message.channel.send('```Guess a number between 1 and 6.```')

            def is_correct(m):
                return m.author == message.author and m.content.isdigit()

            answer = random.randint(1, 6)

            try:
                guess = await self.wait_for('message', check=is_correct, timeout=5.0)
            except asyncio.TimeoutError:
                return await message.channel.send('```Sorry, you took too long it was {}.```'.format(answer))

            if int(guess.content) == answer:
                await message.channel.send('```You are right!```')
            else:
                await message.channel.send('```Oops. It is actually {}.```'.format(answer))

        # Anime Recommendation
        if message.content.startswith('-animerec'):
            rec = random.randint(1, len(anime_list)-1)
            frec = anime_list[rec]
            await message.channel.send('```I recommend the anime {}```'.format(frec))

        # coin flip
        if message.content.startswith('-coinflip'):
            channel = message.channel
            face = random.randint(1, 2)

            if face == 1:
                await message.channel.send("```The Coin Flipped Heads```")
            elif face == 2:
                await message.channel.send("```The Coin Flipped Tails```")

        # Help Command
        if message.content.startswith('-help'):
            await message.channel.send('''```
Hey, here's what I can do:
    -roll ~ Dice roll game if you are feeling lucky
    -animerec ~ Want a new anime to watch? Try this to find new show. (if you would like to add an anime message @Nezuko Chan
    -coinflip ~ Does what is says; flips a coin
    -twitch ~ Displays twitch channel
    
If you have anymore questions feel free to ask an Admin or Moderators ```''')

        if message.content.startswith('-twitch'):
            channel = message.channel
            await message.channel.send("```My Twitch is https://www.twitch.tv/spretzelz```")

client = MyClient()
client.run("NjgwMTk2MjUzNjM5NzcwMTMy.XlA7hw.0sM_0J8oSacPBPjuFodRV3uMUDs")