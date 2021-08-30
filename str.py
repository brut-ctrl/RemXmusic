import asyncio

from pyrogram import Client

print("Enter your app information from my.telegram.org/apps below.")


async def main():
    async with Client(":memory:", api_id=int(input("API ID:")), api_hash=input("API HASH:")) as app:
        PYRO_SESSION = await app.export_session_string()
        await app.send_message("me", f"**Pyrogram String Session:** \n`{PYRO_SESSION}` \n\n**Source  by @fantaestheticgang ðŸ˜‡**")
        print(f"Here is your Pyrogram String Session: \n {PYRO_SESSION} \n\nPro tip: Check your saved message also, Backup of this session is also saved in there :)")


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
