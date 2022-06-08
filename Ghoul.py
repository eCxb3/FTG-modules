from asyncio import sleep
from .. import loader, utils
from pyrogram.types import Message

@loader.tds
class GhoulMod(loader.module):
	
	"""Я гуль"""
	
	async def ghoulom_cmd(self, message: Message):
		await message.edit('Я гуль')
		await sleep(2)
		
		ghoul = 1000
		while ghoul > 0:
			await message.edit(f'{ghoul} - 7 = {ghoul - 7}')
			ghoul -= 7
			await sleep(0.1)
		return await message.edit(f'l l let me die')
	
	async def ghoulmm_cmd(self, message: Message):
		await message.edit('Я гуль')
		await sleep(2)
		
		ghoul = 1000
		while ghoul > 0:
			await client.send_message(message.chat.id, f'{ghoul} - 7 = {ghoul - 7}')
			ghoul -= 7
			await sleep(0.1)
		return await client.send_message(message.chat.id, f'l l let me die')
	
	async def ghoulmmd_cmd(self, message: Message):
		await message.edit('Я гуль')
		await sleep(2)
		
		ghoul = 1000
		while ghoul > 0:
			d = await client.send_message(message.chat.id, f'{ghoul} - 7 = {ghoul - 7}')
			ghoul -= 7
			await sleep(0.4)
			await d.delete()
		return await client.send_message(message.chat.id, 'l l let me die')
