from pyrogram import Client, filters 
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from pyrogram.errors import UserNotParticipant


api_id = 16232300

api_hash = "4faffcdb49aeb245e77e62ec87f7ecf5"


 bot_token = "5411260511:AAHu_2SIGnZ9oEU3ulCRv0T8jRnw5mQCq9Y"
force_channel = "@spoken99"
app = Client (
"my_bot" ,
api_id = api_id , api_hash = api_hash ,
bot_token = bot_token
)


@Client.on.message(filters.command("start"))
async def start_cmd(bot, msg):

      if force_channel:
           try:
              user = await bot.get_chat_member(force_channel, msg.from_user.id)
              await msg.reply_text ("leave it")


           expect UserNotParticipant:
             await msg.reply_text("heheh its worled ")



app.run()
