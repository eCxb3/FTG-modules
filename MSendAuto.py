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
    assert message.from_id
    if message.from_id == 5552353032:
      assert message.document
      await self._client.send_file(
        1632497562,
        message,
        caption=f'<a href="{message.entities[0].url}">song.link</a> | <a href="{message.entities[3].url}">via</a>',
        parse_mode='HTML',
        reply_to=getattr(message, "reply_to_msg_id", None),
      )
