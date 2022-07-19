import time
from .. import loader

@loader.tds
class SingletimerMod(loader.Module):
  """Время, сколько вам не писали"""
  strings = {'name': 'Single Timer'}
    
  async def client_ready(self, client, db):
    self.db = db
    if db.get('SingleTimer', 'status') == True: 
      self.start_time = time.time()
      return 
    
  async def stimercmd(self, message):
    """Врубить / вырубить таймер"""
    status = self.db.get('SingleTimer', 'status')
    if status == False:
      self.db.set('SingleTimer', 'status', True)
      await message.edit('Таймер одиночества включен')
      self.start_time = time.time()
      return
    self.db.set('SingleTimer', 'status', False)
    return await message.edit('Таймер одиночества выключен')
  
  async def watcher(self, message):
    if self.db.get('SingleTimer', 'status') == True:
      if message.is_private:
        end_time = time.time() - self.start_time
        return await message.reply(f'Пользователю не писали {end_time} секунд')
