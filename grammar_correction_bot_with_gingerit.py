#!/usr/bin/python3.9
# pylint: disable=C0116,W0613
# This program is dedicated to the public domain under the CC0 license.
#with webhook

import logging
from gingerit.gingerit import GingerIt
import datetime
from telegram import Update, ForceReply
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext

from telegram import InlineQueryResultArticle, ParseMode, InputTextMessageContent, Update
from telegram.ext import Updater, InlineQueryHandler, CommandHandler, CallbackContext
from telegram.utils.helpers import escape_markdown
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import CallbackQueryHandler
from telegram import Update, ForceReply
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext


# Enable logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)

logger = logging.getLogger(__name__)
parser = GingerIt()


api_key = "1977947414:AAGwtoKBw9txvw-53dnPMgZ3v6Y8rtJ-knw"


# Define a few command handlers. These usually take the two arguments update and
# context.
def start(update: Update, context: CallbackContext) -> None:
    """Send a message when the command /start is issued."""
    user = update.effective_user
    update.message.reply_text(
        '''<b>Send or forward a text, you want to see what are the mistakes you've made. ✍️</b>\n\n<b>🧲 Limitations:- </b> \n<i>Free telegram users only allows to send maximum 300 characters only.</i>''',
        reply_markup=ForceReply(selective=True), parse_mode= ParseMode.HTML
    )

    chat_id = update.message.chat_id
    group_id = update.message.chat.id
    type = update.message.chat.type
    group_name = update.message.chat.title
    reyplyed_user_fristName = update.message.from_user.first_name
    reyplyed_user_username = update.message.from_user.username
    reyplyed_user_user_language = update.message.from_user.language_code
    reyplyed_user_user_id = update.message.from_user.id

    print('------------------------------------------')
    print(group_id,type,group_name,reyplyed_user_fristName,reyplyed_user_username,reyplyed_user_user_id,reyplyed_user_user_language)
    print('----------------------------------------------------------')

    #sending report to admins
    context.bot.send_message(chat_id=378984038, text =f'''<u><b>Report released - New bot user</b></u>\n\n<b>Status :- New Bot User</b>\n<i>(A new user starts the bot at now)</i>\n\nName :- {reyplyed_user_fristName}\nusername:- @{reyplyed_user_username}\nChat ID :- {chat_id}\nChat type :- {type}\nGroup :- {group_name}\nlanguage:-{reyplyed_user_user_language}\n\n<code>{datetime.datetime.now().strftime("%Y/%m/%d")}\n{datetime.datetime.now().strftime("%A")}\n{datetime.datetime.now().strftime("%H:%m %p")}</code>''', parse_mode=ParseMode.HTML)
    context.bot.send_message(chat_id=541256326, text =f'''<u><b>Report released - New bot user</b></u>\n\n<b>Status :- New Bot User</b>\n<i>(A new user starts the bot at now)</i>\n\nName :- {reyplyed_user_fristName}\nusername:- @{reyplyed_user_username}\nChat ID :- {chat_id}\nChat type :- {type}\nGroup :- {group_name}\nlanguage:-{reyplyed_user_user_language}\n\n<code>{datetime.datetime.now().strftime("%Y/%m/%d")}\n{datetime.datetime.now().strftime("%A")}\n{datetime.datetime.now().strftime("%H:%m %p")}</code>''', parse_mode=ParseMode.HTML)
    context.bot.send_message(chat_id=942664387, text =f'''<u><b>Report released - New bot user</b></u>\n\n<b>Status :- New Bot User</b>\n<i>(A new user starts the bot at now)</i>\n\nName :- {reyplyed_user_fristName}\nusername:- @{reyplyed_user_username}\nChat ID :- {chat_id}\nChat type :- {type}\nGroup :- {group_name}\nlanguage:-{reyplyed_user_user_language}\n\n<code>{datetime.datetime.now().strftime("%Y/%m/%d")}\n{datetime.datetime.now().strftime("%A")}\n{datetime.datetime.now().strftime("%H:%m %p")}</code>''', parse_mode=ParseMode.HTML)




def help_command(update: Update, context: CallbackContext) -> None:
    """Send a message when the command /help is issued."""
    update.message.reply_text('''<b><i>It's easy to use  ✳️</i></b>\nSend a text, or forward it. That's it. 👍''',reply_markup=ForceReply(selective=True), parse_mode= ParseMode.HTML)


def echo(update: Update, context: CallbackContext) -> None:
    """Echo the user message."""
    chat_id = update.message.chat_id
    group_id = update.message.chat.id
    type = update.message.chat.type
    group_name = update.message.chat.title
    reyplyed_user_fristName = update.message.from_user.first_name
    reyplyed_user_username = update.message.from_user.username
    reyplyed_user_user_language = update.message.from_user.language_code
    reyplyed_user_user_id = update.message.from_user.id


    text = update.message.text
    json_result = parser.parse(text)
    entered_text = f'''{json_result['text']}'''
    result = f'''{json_result['result']}'''

    all_mistakes = "";
    corrections = json_result['corrections']
    for i in range(1,len(json_result['corrections'])+1):
        error_text = f'''{json_result['corrections'][i-1]['text']}'''
        corrected_text = f'''{json_result['corrections'][i-1]['correct']}'''
        all_mistakes = all_mistakes + f"{i}) <s>{error_text}</s> >> {corrected_text} \n"

    if text != result:
        update.message.reply_text(f"<b>[CORRECTED SENTENCE]</b> ✅ \n{result} \n\n <b>There were {len(json_result['corrections'])} mistakes  ❌</b> \n <i>{all_mistakes}</i>",parse_mode= ParseMode.HTML)

        #sending report to Admins
        context.bot.send_message(chat_id=378984038, text =f'''<u><b>Report released - User used the bot</b></u>\n\n<b>Status :- User used the bot</b>\n<i>(A user used the bot for check grammar error of a sentence)</i>\n\nName :- {reyplyed_user_fristName}\nusername:- @{reyplyed_user_username}\nChat ID :- {chat_id}\nChat type :- {type}\nGroup :- {group_name}\nlanguage:-{reyplyed_user_user_language}\n\n———————————————————\n<b>Message sent by user: 👇</b>\n\n❌  <i>{text}</i>\n———————————————————\n\nThere were {len(json_result['corrections'])} mistakes to correct\n\n{all_mistakes}\n\n———————————————————\n<b>Corrected Sentence: 👇</b>\n\n✅   <i>{result}</i>\n\n———————————————————\n\n<code>{datetime.datetime.now().strftime("%Y/%m/%d")}\n{datetime.datetime.now().strftime("%A")}\n{datetime.datetime.now().strftime("%H:%m %p")}</code>''', parse_mode=ParseMode.HTML)
        context.bot.send_message(chat_id=541256326, text =f'''<u><b>Report released - User used the bot</b></u>\n\n<b>Status :- User used the bot</b>\n<i>(A user used the bot for check grammar error of a sentence)</i>\n\nName :- {reyplyed_user_fristName}\nusername:- @{reyplyed_user_username}\nChat ID :- {chat_id}\nChat type :- {type}\nGroup :- {group_name}\nlanguage:-{reyplyed_user_user_language}\n\n———————————————————\n<b>Message sent by user: 👇</b>\n\n❌  <i>{text}</i>\n———————————————————\n\nThere were {len(json_result['corrections'])} mistakes to correct\n\n{all_mistakes}\n\n———————————————————\n<b>Corrected Sentence: 👇</b>\n\n✅   <i>{result}</i>\n\n———————————————————\n\n<code>{datetime.datetime.now().strftime("%Y/%m/%d")}\n{datetime.datetime.now().strftime("%A")}\n{datetime.datetime.now().strftime("%H:%m %p")}</code>''', parse_mode=ParseMode.HTML)
        context.bot.send_message(chat_id=942664387, text =f'''<u><b>Report released - User used the bot</b></u>\n\n<b>Status :- User used the bot</b>\n<i>(A user used the bot for check grammar error of a sentence)</i>\n\nName :- {reyplyed_user_fristName}\nusername:- @{reyplyed_user_username}\nChat ID :- {chat_id}\nChat type :- {type}\nGroup :- {group_name}\nlanguage:-{reyplyed_user_user_language}\n\n———————————————————\n<b>Message sent by user: 👇</b>\n\n❌  <i>{text}</i>\n———————————————————\n\nThere were {len(json_result['corrections'])} mistakes to correct\n\n{all_mistakes}\n\n———————————————————\n<b>Corrected Sentence: 👇</b>\n\n✅   <i>{result}</i>\n\n———————————————————\n\n<code>{datetime.datetime.now().strftime("%Y/%m/%d")}\n{datetime.datetime.now().strftime("%A")}\n{datetime.datetime.now().strftime("%H:%m %p")}</code>''', parse_mode=ParseMode.HTML)


    else:
        update.message.reply_text(f"<b>You have no mistakes  ✅ </b>",parse_mode= ParseMode.HTML)

        #sending report to Admins
        context.bot.send_message(chat_id=378984038, text =f'''<u><b>Report released - User used the bot</b></u>\n\n<b>Status :- User used the bot</b>\n<i>(A user used the bot for check grammar error of a sentence)</i>\n\nName :- {reyplyed_user_fristName}\nusername:- @{reyplyed_user_username}\nChat ID :- {chat_id}\nChat type :- {type}\nGroup :- {group_name}\nlanguage:-{reyplyed_user_user_language}\n\n———————————————————\n<b>Message sent by user: 👇</b>\n\n✅ <i>{text}</i>\n———————————————————\n\nThere wasn't any mistakes to correct\n\n<code>{datetime.datetime.now().strftime("%Y/%m/%d")}\n{datetime.datetime.now().strftime("%A")}\n{datetime.datetime.now().strftime("%H:%m %p")}</code>''', parse_mode=ParseMode.HTML)
        context.bot.send_message(chat_id=541256326, text =f'''<u><b>Report released - User used the bot</b></u>\n\n<b>Status :- User used the bot</b>\n<i>(A user used the bot for check grammar error of a sentence)</i>\n\nName :- {reyplyed_user_fristName}\nusername:- @{reyplyed_user_username}\nChat ID :- {chat_id}\nChat type :- {type}\nGroup :- {group_name}\nlanguage:-{reyplyed_user_user_language}\n\n———————————————————\n<b>Message sent by user: 👇</b>\n\n✅ <i>{text}</i>\n———————————————————\n\nThere wasn't any mistakes to correct\n\n<code>{datetime.datetime.now().strftime("%Y/%m/%d")}\n{datetime.datetime.now().strftime("%A")}\n{datetime.datetime.now().strftime("%H:%m %p")}</code>''', parse_mode=ParseMode.HTML)
        context.bot.send_message(chat_id=942664387, text =f'''<u><b>Report released - User used the bot</b></u>\n\n<b>Status :- User used the bot</b>\n<i>(A user used the bot for check grammar error of a sentence)</i>\n\nName :- {reyplyed_user_fristName}\nusername:- @{reyplyed_user_username}\nChat ID :- {chat_id}\nChat type :- {type}\nGroup :- {group_name}\nlanguage:-{reyplyed_user_user_language}\n\n———————————————————\n<b>Message sent by user: 👇</b>\n\n✅ <i>{text}</i>\n———————————————————\n\nThere wasn't any mistakes to correct\n\n<code>{datetime.datetime.now().strftime("%Y/%m/%d")}\n{datetime.datetime.now().strftime("%A")}\n{datetime.datetime.now().strftime("%H:%m %p")}</code>''', parse_mode=ParseMode.HTML)



def main() -> None:
    """Start the bot."""
    # Create the Updater and pass it your bot's token.
    updater = Updater(api_key)

    # Get the dispatcher to register handlers
    dispatcher = updater.dispatcher

    # on different commands - answer in Telegram
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("help", help_command))

    # on non command i.e message - echo the message on Telegram
    dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, echo))

    # Start the Bot
    updater.start_polling()

    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()

    #setting up the webhook - place this code under the def main()-> none
    updater.start_webhook(listen="0.0.0.0",
                          port=int(PORT),
                          url_path=api_key)
    updater.bot.setWebhook(server_url_with_https,api_key)


if __name__ == '__main__':
    main()