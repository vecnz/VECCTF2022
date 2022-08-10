import interactions
from arrr import translate
from bs4 import BeautifulSoup
import aiohttp


def main():
    bot.start()


bot = interactions.Client(
    token="MTAwNDI5NDk3MDAyNDQwMjk1NA.GQk07F.HrA3KrB1tdXPkjE1eqemt-AgAQNGAomIqVktqo"
)


@bot.command(
    name="yarrr",
    description="yarrrify a wikipedia page!",
    options=[
        interactions.Option(
            name="url",
            description="URL of the wikipedia page to yarrrify",
            type=interactions.OptionType.STRING,
            required=True,
            default_member_permissions=0,
            default_permission=False,
        ),
    ],
)
async def yarrr(ctx: interactions.CommandContext, url: str):
    print(url)
    async with aiohttp.ClientSession() as session:
        await ctx.defer(ephemeral=False)
        try:
            async with session.get(url) as resp:
                htmldata = await resp.text()
                soup = BeautifulSoup(htmldata, "html.parser")
                paragraphs = soup.find_all("p")
                for para in paragraphs:
                    if para.get_text().strip() != "":
                        await ctx.send(translate(para.get_text()))
                        return
                await ctx.send(translate(soup.get_text()))
                return
        except aiohttp.ClientError as e:
            await ctx.send(repr(e))
        except:
            await ctx.send("Unknown error")


if __name__ == "__main__":
    main()
