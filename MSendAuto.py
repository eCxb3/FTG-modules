from .. import loader, utils
from telethon.tl.types import Message

@loader.tds
class MusicsendMod(loader.Module):
  """Отправляет песню в группу"""
  strings = {"name": "MSend"}
  
  async def client_ready(self, client, db):
    self._db = db
    self._client = client

  async def watcher(self, message: Message):
    if message.from_id == 5552353032:
      assert message.document
      reply = await message.get_reply_message()
      await self._client.send_file(
        1632497562,
        message,
        caption=f'<a href="{reply.entities[0].url}">song.link</a> | <a href="{reply.entities[3].url}">via</a>',
        parse_mode='HTML',
        reply_to=getattr(message, "reply_to_msg_id", None),
      )
