import discord
import json
from discord.ext import commands

token = DISCORD TOKEN
client = commands.Bot(command_prefix="-")
bot = commands.Bot(command_prefix='-')


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


@client.event
async def on_ready():
    await client.change_presence(activity=discord.Game(name=' "-" Prefix'))


@client.event
async def on_member_join(member):
    print(f'{member} has joined the server UwU!')


@client.event
async def on_member_leave(member):
    print(f'{member} has left the server (ㄒoㄒ)!')


@client.event
async def on_member_join(member):
    with open('users.json', 'r') as f:
        users = json.load(f)
        person = member
        role = discord.utils.get(member.guild.roles, name="Newbie")
        await person.add_roles(role)

    users = int_keys(users)
    await update_data(users, member)
    with open('users.json', 'w') as f:
        json.dump(users, f, indent=4)


def int_keys(users):
    new_users = {}
    for key, value in users.items():
        new_users[int(key)] = value
    return new_users


@client.event
async def on_message(message):
    print(message)
    with open('users.json', 'r') as r:
        users = json.load(r)

    users = int_keys(users)

    await update_data(users, message.author)
    await add_experience(users, message.author, 5)
    await level_up(users, message.author, message.channel)

    with open('users.json', 'w') as f:
        json.dump(users, f)


@client.event
async def update_data(users, user):
    if user.id not in users:
        users[user.id] = {}
        users[user.id]['experience'] = 0
        users[user.id]['level'] = 1


@client.event
async def add_experience(users, user, exp):
    users[user.id]['experience'] += exp


@client.event
async def level_up(users, user, channel):
    experience = users[user.id]['experience']
    lvl_start = users[user.id]['level']
    lvl_end = int(experience ** (1 / 4))

    if lvl_start < lvl_end:
        await channel.send('{} has leveled up to level {}'.format(user.mention, lvl_end))
        users[user.id]['level'] = lvl_end
        person = user
        role = discord.utils.get(channel.guild.roles, name="Familiar")
        role1 = discord.utils.get(channel.guild.roles, name="Cool")
        role2 = discord.utils.get(channel.guild.roles, name="Gamer")
        role3 = discord.utils.get(channel.guild.roles, name="Veteran Gamer")
        role4 = discord.utils.get(channel.guild.roles, name="Gamer Clan")
        role5 = discord.utils.get(channel.guild.roles, name="Champion")
        role6 = discord.utils.get(channel.guild.roles, name="Newbie")

        if "Bots" in person.roles:
            pass
        elif lvl_end == 5 and not "Familiar" in person.roles:
            await channel.send('{} you seem familiar.'.format(user.mention))
            await person.add_roles(role)
            await person.remove_roles(role6)

        elif lvl_end == 10 and not "Cool" in person.roles:
            await channel.send('{} your cool, stay awhile.'.format(user.mention))
            await person.add_roles(role1)
            await person.remove_roles(role)

        elif lvl_end == 20 and not "Gamer" in person.roles:
            await channel.send('{} hey, ive seen u where a lot. You\'r a Gamer.'.format(user.mention))
            await person.add_roles(role2)
            await person.remove_roles(role2)

        elif lvl_end == 30 and not "Veteran Gamer" in person.roles:
            await channel.send('{} Hey, u seem like a Veteran Gamer'.format(user.mention))
            await person.add_roles(role3)
            await person.remove_roles(role3)

        elif lvl_end == 40 and not "Gamer Clan" in person.roles:
            await channel.send('{} Hey, Wanna join my clan?.'.format(user.mention))
            await person.add_roles(role4)
            await person.remove_roles(role4)

        elif lvl_end == 50 and not "Champion" in person.roles:
            await channel.send('{} Wow, you became a champion. Congratulations'.format(user.mention))
            await person.add_roles(role5)
            await person.remove_roles(role5)


client.run(token)
