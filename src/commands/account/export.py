"https://data.typeracer.com/pit/export_data?universe=play"

from discord.ext import commands

from database.bot.users import get_user
from utils.embeds import Page, Message

command = {
    "name": "export",
    "aliases": ["exportdata"],
    "description": "Links to the official TypeRacer export data feature",
}


class Export(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=command["aliases"])
    async def export(self, ctx):
        user = get_user(ctx)

        message = Message(
            ctx=ctx,
            user=user,
            pages=[Page(
                title="Data Export",
                description=(
                    "You can download your data directly\n"
                    "from TypeRacer by visiting [this link](https://data.typeracer.com/pit/export_data)"
                ),
            )],
            header="",
        )

        await message.send()


async def setup(bot):
    await bot.add_cog(Export(bot))
