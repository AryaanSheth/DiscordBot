import random

import discord
from discord.ext import commands

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
              "Black Clover", "Kakegurui – Compulsive Gambler",
              "Black Butler, Glepnir, A Certain Scientific Railgun, Sailor Moon, Magi, Beyond the Boundry"]

coal = ['Young fool. ...', "There is a great disturbance in the Force",
        "Your feeble skills are no match for the power of the dark side!", 'Once more the Sith will rule the galaxy!',
        'That is UNFORTUNATE...',
        'Do not fear their feeble attack, my faithful. Nothing will stop the return of the sith!',
        'As once I fell, so falls the last skywalker.',
        'The attempt on my life has left me scarred and deformed, but I assure you, my resolve has never been stronger!',
        'The dark side of the force is a pathway to many abilities some consider to be unnatural',
        'It is your end, my little green friend',
        'Now witness the firepower of this fully armed and operational battle station',
        'It is of no concern. Soon the rebellion will be crushed and young Skywalker will be one of us.',
        'Now you will experience the full power of the dark side']

def int_keys(users):
    new_users = {}
    for key, value in users.items():
        new_users[int(key)] = value
    return new_users

class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged in as')
        print(self.user.name)
        print(self.user.id)
        print('------')
        await client.change_presence(activity=discord.Game(name=' "-" Prefix'))

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
            except:
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

            # sus Meter
        if message.content.startswith('-sus'):
            sus_lvl = random.randint(1, 100)
            await message.channel.send("```You Are {0}% sus!```".format(sus_lvl))

            # send my Socials
        if message.content.startswith('-socials'):
            channel = message.channel
            await message.channel.send(
                "```My Twitch is https://www.twitch.tv/spretzelz \nMy Discord is Spoopy#4645```")

        if message.content.startswith('-coal'):
            clist = len(coal)
            cnum = random.randint(0, clist)
            await message.channel.send("```{0}```".format(coal[cnum]))

        if message.content.startswith('-femboy'):
            id = '<@356248821464039425>'
            await message.channel.send(id + " is a femboy")

        # Help Command
        if message.content.startswith('-help'):
            await message.channel.send('''```
Hey, here's what I can do:
    -roll ~ Dice roll game if you are feeling lucky
    -animerec ~ Want a new anime to watch? Try this to find new show. (if you would like to add an anime, message Spoopy#4645 on Discord) 
    -coinflip ~ Does what is says; flips a coin
    -socials ~ Displays Socials
    -sus ~ Checks how sus you are
    -coal ~ Says a Coal quote.
    
If you have anymore questions feel free to ask an Admin or Moderators ```''')


client = MyClient()
client.run("NjgwMTk2MjUzNjM5NzcwMTMy.XlA7hw.0sM_0J8oSacPBPjuFodRV3uMUDs")

