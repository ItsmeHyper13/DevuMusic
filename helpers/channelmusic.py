# Powered by @Dk_music_shayari | @Education_quiz_hub
# Dear Pero ppls Plish Don't remove this line from here🌚

from pyrogram.types import Chat


def get_chat_id(chat: Chat):
    if chat.title.startswith("Channel Music: ") and chat.title[16:].isnumeric():
        return int(chat.title[15:])
    return chat.id
