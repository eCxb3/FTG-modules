# meta developer: @ecXbe

from .. import loader, utils
from telethon.tl.types import Message

@loader.tds
class MusicSendMod(loader.Module):
  
  strings = {"name": "MusicSender"}
  
  async def client_ready(self, client, db):
    self._db = db
      self._client = client
      await utils.dnd(client, "@audio_storm_bot", archive=True)
  
  async def msendcmd(self, message: Message):
    
    args = utils.get_args_raw(message)
    if not args:
      return await message.edit('❌ Нет аргумента')
    
    async with self._client.conversation("@audio_storm_bot") as conv:
      try:
        m = await conv.send_message(args)
        r = await conv.get_response()
        await m.delete()

        assert "Извините, по данному запросу не найдено аудиозаписей" not in r.raw_text

        await r.click(0)
        await r.delete()
        r = await conv.get_response()

        assert r.document

        await self._client.send_file(
            message.peer_id,
            r.document,
            reply_to=getattr(message, "reply_to_msg_id", None),
        )
        await r.delete()
        await message.delete()
      except Exception:
        await utils.answer(message, f'❌ Песня: «{args}» не найдена')
      
      await self._client.delete_dialog("@audio_storm_bot")
