import asyncio

from pyrogram import Client, filters
from pyrogram.types import Message

def get_arg(message):
    msg = message.text
    msg = msg.replace(" ", "", 1) if msg[1] == " " else msg
    split = msg[1:].replace("\n", " \n").split(" ")
    if " ".join(split[1:]).strip() == "":
        return ""
    return " ".join(split[1:])

@Client.on_message(filters.me & filters.command(["q", "quotly"], "."))
async def quotly(client: Client, message: Message):
    args = get_arg(message)
    if not message.reply_to_message and not args:
        return await message.edit(" Please reply to a message")
    bot = "QuotLyBot"
    if message.reply_to_message:
        await message.edit("Making a quote...")
        await client.unblock_user(bot)
        if args:
            await client.send_message(bot, f"/qcolor {args}")
            await asyncio.sleep(1)
        else:
            pass
        await message.reply_to_message.forward(bot)
        await asyncio.sleep(5)
        async for quotly in client.search_messages(bot, limit=1):
            if quotly:
                await message.delete()
                await message.reply_sticker(
                    sticker=quotly.sticker.file_id,
                    reply_to_message_id=message.reply_to_message.id
                    if message.reply_to_message
                    else None,
                )
            else:
                return await message.edit("Failed to Create Quotly Sticker")
                
                
