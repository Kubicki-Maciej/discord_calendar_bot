import json
import random
import discord
from discord.ui import Select, View, Button
from discord.ext import commands
from discord_calendar import Events, DataReader


def load_json(file_name='token.json'):
    with open(file_name) as f:
        return json.loads(f.read())


def discord_token():
    return load_json()['token']


intents = discord.Intents.all()
bot = commands.Bot(command_prefix='/', intents=intents)


@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to Discord!')


@bot.command(name='nine')
async def nine_nine(ctx):
    brooklyn_99_quotes = [
        'I\'m the human form of the 💯 emoji.',
        'Bingpot!',
        (
            'Cool. Cool cool cool cool cool cool cool, '
            'no doubt no doubt no doubt no doubt.'
        ),
    ]

    response = random.choice(brooklyn_99_quotes)
    await ctx.send(response)


@bot.command(name='start')
async def start_event(ctx, arg):
    try:
        print('created new event')
        await ctx.send(f'new event created for {arg}: days')
    except:
        print('no arg')


@bot.command(name='make_event')
async def make_event(ctx, arg):
    try:
        if type(int(arg)) == int:

            # create object representative event in db (json)
            # create objects/event on discord for each day
            await ctx.send(f'new event created for {arg}: days')

        else:
            await ctx.send(f'Some thing went wrong')
    except:
        print('no arg')




@bot.command()
async def make_button(ctx):
    select = Select(

        options=[
            discord.SelectOption(label="Cloudy", description=" test 1"),
            discord.SelectOption(label="Suny", description=" test 2")
        ]
    )

    async def my_callback(interaction):
        await interaction.response.send_message(f"You chose: {select.values[0]}")
    select.callback = my_callback

    view = View()
    view.add_item(select)
    await ctx.send('choose a weather', view=view)


@bot.command()
async def select_class_to_event(ctx):

    select = Select(
        placeholder="Choose class",
        options=[
            discord.SelectOption(label="Druid", description=" test 1"),
            discord.SelectOption(label="Mage", description=" test 2"),
            discord.SelectOption(label="Warlock", description=" test 3")
        ]
    )

    async def my_callback(interaction):
        await interaction.response.send_message(f"You chose: {select.values[0]}")
    select.callback = my_callback

    view = View()
    view.add_item(select)
    await ctx.send('choose a weather', view=view)


@bot.command()
async def sign_user(ctx):
    """
    OWN
    """
    author = ctx.author
    print(ctx.author)

    DataReader('event.json').add_user(str(author))
    await ctx.send(f"Added User to event calendar {author}")

@bot.command()
async def create_event(ctx, arg):
    pass


@bot.command()
async def test_thing(ctx):
    """ create event """
    #setup event id or smth ?
    #get user
    #save user choice

    button_accept = Button(label="Accept", style=discord.ButtonStyle.green)
    button_tentative = Button(label="Tentative", style=discord.ButtonStyle.blurple)
    button_deciline = Button(label="Decline", style=discord.ButtonStyle.red)



    async def button_callback_accept(interaction):
        await interaction.response.send_message(f"User")

    button_accept.callback = button_callback_accept

    view = View()
    view.add_item(button_accept)
    view.add_item(button_tentative)
    view.add_item(button_deciline)

    await ctx.send("", view=view)

bot.run(token=discord_token())