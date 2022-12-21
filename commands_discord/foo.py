from discord.ext import commands


@commands.command()
async def foo(ctx, arg1, arg2):
    await ctx.send(f'You passed {arg1} and {arg2}')

