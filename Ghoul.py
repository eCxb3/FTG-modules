from asyncio import sleep
from .. import loader, utils
from telethon.tl.types import Message

@loader.tds
class GhoulMod(loader.Module):
	"""Я гуль"""
	strings = {
        	"name": "Ghoul"
	}
	
	async def ghoulomcmd(self, message: Message):	
		"""Гуль одним сообщением"""
		await utils.answer(message, 'Я гуль')
		await sleep(2)
		
		ghoul = 1000
		while ghoul > 0:
			await message.edit(f'{ghoul} - 7 = {ghoul - 7}')
			ghoul -= 7
			await sleep(0.1)
		return await utils.answer(message, f'l l let me die')
	
	async def ghoulmmcmd(self, message: Message):
		"""Гуль множеством сообщений"""	
		await utils.answer(message, 'Я гуль')
		await sleep(2)
		
		ghoul = 1000
		while ghoul > 0:
			await message.reply(f'{ghoul} - 7 = {ghoul - 7}')
			ghoul -= 7
			await sleep(0.1)
		return await message.reply(f'l l let me die')
	
	async def ghoulmmdcmd(self, message: Message):
		"""Гуль множеством сразу удаляемыемых сообщений"""	
		await utils.answer(message, 'Я гуль')
		await sleep(2)
		
		ghoul = 1000
		while ghoul > 0:
			d = await message.reply(f'{ghoul} - 7 = {ghoul - 7}')
			ghoul -= 7
			await sleep(0.4)
			await d.delete()
		return await message.reply(f'l l let me die')
