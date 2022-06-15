# meta developer: @ecXbe

from .. import loader, utils
from telethon.tl.types import Message

@loader.tds
class MusicSendMod(loader.Module):
  """Отправляет песню"""
  strings = {"name": "MusicSender"}
  
  async def client_ready(self, client, db):
    self._db = db
    self._client = client
  
  async def msendcmd(self, message: Message):
    """Отправить песню по названию. Использование msend <название песни>"""
    local_id = message.chat.id
    args = utils.get_args_raw(message)
    if not args:
      return await message.edit('❌ Нет аргумента')

    async with self._client.conversation("@audio_storm_bot") as conv:
      await message.edit('🔍 Loading..')
      try:
        m = await conv.send_message(args)
        r = await conv.get_response()

        mm = await self._client.get_messages("@audio_storm_bot", limit=1)
        while 'Пожалуйста, подождите, идёт подготовка..' in mm[0].text:
          mm = await self._client.get_messages("@audio_storm_bot", limit=1)
        r = mm[0]

        assert "Извините, по данному запросу не найдено аудиозаписей" not in r.text

        await r.click(0)
        r = await conv.get_response()

        assert r.document

        await self._client.send_file(local_id, r.document)
        await message.delete()
      except Exception:
        await message.edit(f'❌ Песня: «{args}» не найдена')

      await self._client.delete_dialog("@audio_storm_bot")
