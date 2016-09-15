## DiscordCalc

Discord Permission Calculator for generating permissiosn for discord official bot oauth url's

Usage:

```py
import DiscordCalc
gen = DiscordCalc.General()
tex = DiscordCalc.Text()
vce = DiscordCalc.Voice()
permissions = gen.all + tex.all + vce.all
applicationclientid = "" # Your bot's Application client id from your web browser.
url = "https://discordapp.com/oauth2/authorize?&client_id={1}&scope=bot&permissions={2}".format(
        applicationclientid, permissions)

@asyncio.coroutine
def on_message(client, message)
    if message.content == "invite":
        yield from client.send_message(message.author, "Here is my oauth url to add me to your server(s):\n" + url)

```

This is simple to use.


*Documentation coming soon.*

*pip installation setup.py coming soon*
