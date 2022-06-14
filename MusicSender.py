# meta developer: @ecXbe

from .. import loader, utils
from telethon.tl.types import Message
from telethon.hints import Entity
from telethon.tl.functions.account import UpdateNotifySettingsRequest
from telethon.tl.types import (
    Channel,
    InputPeerNotifySettings
)

@loader.tds
class MusicSendMod(loader.Module):
  """Отправляет песню"""
  strings = {"name": "MusicSender"}
  
  async def dnd(
    client: "TelegramClient",  # type: ignore
    peer: Entity,
    archive: Optional[bool] = True,
  ) -> bool:
    """
    Mutes and optionally archives peer
    :param peer: Anything entity-link
    :param archive: Archive peer, or just mute?
    :returns: `True` on success, otherwise `False`
    """
    try:
        await client(
            UpdateNotifySettingsRequest(
                peer=peer,
                settings=InputPeerNotifySettings(
                    show_previews=False,
                    silent=True,
                    mute_until=2**31 - 1,
                ),
            )
        )

        if archive:
            await client.edit_folder(peer, 1)
    except Exception:
        return False

    return True
  
  async def client_ready(self, client, db):
    self._db = db
    self._client = client
    await dnd(client, "@audio_storm_bot", archive=True)
  
  async def msendcmd(self, message: Message):
    """Отправить песнб по названию. Использование msend <название песни>"""
    args = utils.get_args_raw(message)
    if not args:
      return await message.edit('❌ Нет аргумента')
    local = message.chat.id


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

        await self._client.send_file(local, r.document)
        await message.delete()
      except Exception:
        await message.edit(f'❌ Песня: «{args}» не найдена')

      await self._client.delete_dialog("@audio_storm_bot")
