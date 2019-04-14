import discord
from datetime import datetime
import time
import os

from apscheduler.schedulers.asyncio import AsyncIOScheduler	

try:
    import asyncio
except ImportError:
	import trollius as asyncio

TOKEN = 'тут токен'

client = discord.Client()
channel = discord.Object(id='тут id канала')
boss_list = ['Кзарка', 'Каранда', 'Офин', 'Кутум', 'Нубер', 'Квинт', 'Мурака', 'Велл', 'все', 'Камос']



@client.event
async def on_message(message):
		# we do not want the bot to reply to itself
	if message.author == client.user:
		return
		
	if message.content.startswith('!hello'):
		channel = discord.Object(id='456714454269427725')
		msg = 'Это тестовое сообщение о появлении  ' + boss_list[args(0)] + ' и ' + boss_list[args(1)].format(message)
		await client.send_message(channel, msg)


@client.event		
async def boss_scheduler(b1=1, b2=2):
		msg = '@everyone Через 20 минут появятся  ' + boss_list[b1] + ' и ' + boss_list[b2]
		print(msg)
		await client.send_message(channel, msg)
		
@client.event		
async def telega():
		msg = '@everyone Через 30 минут на каналах Баленос-1 и Серендия-1 отправляются телеги '
		print(msg)
		await client.send_message(channel, msg)
		
#scheduler.add_job(boss_scheduler, 'cron', day_of_week='mon, thu', hour=14, minute=40)

 #  Monday,Tuesday,Wednesday,Thursday,Friday,Saturday,Sunday

if __name__ == '__main__':
	scheduler = AsyncIOScheduler()
	#Кзарка Нубер
	scheduler.add_job(boss_scheduler, 'cron', (0, 4), day_of_week="sun", hour=17, minute=40)
	scheduler.add_job(boss_scheduler, 'cron', (0, 4), day_of_week="fri", hour=23, minute=40)
	#Кзарка Каранда
	scheduler.add_job(boss_scheduler, 'cron', (0, 1), day_of_week="sun", hour=23, minute=40)
	#Карaнда Нубер
	scheduler.add_job(boss_scheduler, 'cron', (1, 4), day_of_week="mon", hour=22, minute=40)
	#Каранда Кутум
	# scheduler.add_job(boss_scheduler, 'cron', (1, 3), day_of_week="sat", hour=00, minute=27)
	#Квинт Мурака
	scheduler.add_job(boss_scheduler, 'cron', (5, 6), day_of_week="sat", hour=13, minute=40)
	scheduler.add_job(boss_scheduler, 'cron', (5, 6), day_of_week="tue", hour=22, minute=40)
	#Офин
	scheduler.add_job(boss_scheduler, 'cron', (2, 8), day_of_week="wed, fri, sun", hour=22, minute=40)
	#Нубер
	scheduler.add_job(boss_scheduler, 'cron', (4, 8), day_of_week="mon, wed", hour=0, minute=40)
	scheduler.add_job(boss_scheduler, 'cron', (4, 8), day_of_week="sat", hour=9, minute=40)
	scheduler.add_job(boss_scheduler, 'cron', (4, 8), day_of_week="thu", hour=11, minute=40)
	scheduler.add_job(boss_scheduler, 'cron', (4, 8), day_of_week="mon", hour=13, minute=40)
	scheduler.add_job(boss_scheduler, 'cron', (4, 8), day_of_week="wed, thu, fri", hour=15, minute=40)
	scheduler.add_job(boss_scheduler, 'cron', (4, 8), day_of_week="thu", hour=23, minute=40)
	#Кутум
	scheduler.add_job(boss_scheduler, 'cron', (3, 8), day_of_week="thu, sat", hour=0, minute=40)
	scheduler.add_job(boss_scheduler, 'cron', (3, 8), day_of_week="sun", hour=9, minute=40)
	scheduler.add_job(boss_scheduler, 'cron', (3, 8), day_of_week="mon, sat", hour=11, minute=40)
	scheduler.add_job(boss_scheduler, 'cron', (3, 8), day_of_week="thu, fri, sun", hour=13, minute=40)
	scheduler.add_job(boss_scheduler, 'cron', (3, 8), day_of_week="tue", hour=15, minute=40)
	scheduler.add_job(boss_scheduler, 'cron', (3, 8), day_of_week="mon, sat", hour=17, minute=40)
	scheduler.add_job(boss_scheduler, 'cron', (3, 8), day_of_week="tue", hour=23, minute=40)
	#Каранда
	scheduler.add_job(boss_scheduler, 'cron', (1, 8), day_of_week="tue", hour=0, minute=40)
	scheduler.add_job(boss_scheduler, 'cron', (1, 8), day_of_week="sun", hour=7, minute=40)
	scheduler.add_job(boss_scheduler, 'cron', (1, 8), day_of_week="tue, fri", hour=11, minute=40)
	scheduler.add_job(boss_scheduler, 'cron', (1, 8), day_of_week="wed", hour=13, minute=40)
	scheduler.add_job(boss_scheduler, 'cron', (1, 8), day_of_week="mon, sat", hour=15, minute=40)
	scheduler.add_job(boss_scheduler, 'cron', (1, 8), day_of_week="tue", hour=17, minute=40)
	scheduler.add_job(boss_scheduler, 'cron', (1, 8), day_of_week="wed", hour=23, minute=40)
	#Кзарка
	scheduler.add_job(boss_scheduler, 'cron', (0, 8), day_of_week="fri, sun", hour=0, minute=40)
	scheduler.add_job(boss_scheduler, 'cron', (0, 8), day_of_week="sat", hour=7, minute=40)
	scheduler.add_job(boss_scheduler, 'cron', (0, 8), day_of_week="tue", hour=13, minute=40)
	scheduler.add_job(boss_scheduler, 'cron', (0, 8), day_of_week="wed, thu, fri", hour=17, minute=40)
	scheduler.add_job(boss_scheduler, 'cron', (0, 8), day_of_week="mon", hour=23, minute=40)
	#Велл
	scheduler.add_job(boss_scheduler, 'cron', (7, 8), day_of_week="sun", hour=15, minute=40)
	#Телега
	scheduler.add_job(telega, 'cron', day_of_week="sat", hour=16, minute=30)
	#Камос
	scheduler.add_job(boss_scheduler, 'cron', (9, 8), day_of_week="thu", hour=22, minute=40)
	scheduler.add_job(boss_scheduler, 'cron', (9, 8), day_of_week="sat", hour=23, minute=40)
	scheduler.add_job(boss_scheduler, 'cron', (9, 8), day_of_week="sun", hour=11, minute=40)
	scheduler.start()
		
@client.event
async def on_ready():
	print('Logged in as')
	print(client.user.name)
	print(client.user.id)
	print('------')
	
client.run(TOKEN)
