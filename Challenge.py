from .. import loader, utils
from telethon.tl.types 
from random import choice
import Message 

@loader.tds
class ChallengeMod(loader.Module):
  """Отправляет испытание"""
  strings = {"name": "ChallengeSend"}
  
  async def client_ready(self, client, db):
    self._db = db
    self._client = client

  async def chsend(self, message: Message):
    await message.delete()
    args = utils.get_args_raw(message)
    if not args:
      return message.edit('Нет списка испытаний')

    list = args.split('^^')
    for x in range(len(list)):
      list[x] = list[x].strip()
    message_challenge = await self._client.send_message(message.peer_id, f'||{choice(list)}||', parse_mode='md')
    await message_challenge.delete(revoke=False)
