# meta developer: @ecXbe

from .. import loader, utils
from telethon.tl.types import Message
from random import choice 

@loader.tds
class ChallengeMod(loader.Module):
  """Отправляет испытание. Ввбирает рандонмное исрюпытание из списка, отправляет его и сразу удаляет только для вас."""
  strings = {"name": "ChallengeSend"}
  
  async def client_ready(self, client, db):
    self._db = db
    self._client = client

  async def chsendcmd(self, message: Message):
    """-chsend 1 испытание ^^ 2 испытание ^^ ... ^^ n испытание"""
    await message.delete()
    args = utils.get_args_raw(message)
    if not args:
      return message.edit('Нет списка испытаний')

    list = args.split('^^')
    for x in range(len(list)):
      list[x] = list[x].strip()
    message_challenge = await self._client.send_message(message.peer_id, f'||{choice(list)}||', parse_mode='md')
    await message_challenge.delete(revoke=False)
