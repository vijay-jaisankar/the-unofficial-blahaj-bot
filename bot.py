import discord
from discord.ext import commands 
import random 
import requests
from datetime import date 
import json
from amazon_scraper import getAmazonLink, getLinks, getImages


from creds import bot_token, access_key, secret_key 


client = commands.Bot(command_prefix= '.')


def getLinkEnToSv(text):
	return "https://api.mymemory.translated.net/get?q={}&langpair=en|sv".format(text)

def getLinkSvToEn(text):
	return "https://api.mymemory.translated.net/get?q={}&langpair=sv|en".format(text)


@client.event
async def on_ready():
    print("Blahaj Bot is ready!")


@client.command()
async def ping(ctx):
    await ctx.send(f'Pong! Latency = {client.latency * 1000} ms')


@client.command()
async def blahajlang(ctx,engText):
	link = getLinkEnToSv(engText)
	r = requests.get(link)
	print(r.status_code)
	json_r = r.json()
	try:
		await ctx.send(json_r['responseData']['translatedText'])
	except Exception as e:
		print(e)
		await ctx.send("Beep Boop! There seems to be a disturbance in the BlahaFORCE")

@client.command()
async def blinglish(ctx,svText):
	link = getLinkSvToEn(svText)
	r = requests.get(link)
	json_r = r.json()
	print(r.status_code)
	try:
		await ctx.send(json_r['responseData']['translatedText'])
	except Exception as e:
		print(e)
		await ctx.send("Beep Boop! There seems to be a distraction in the BlahaFORCE")

    


@client.command()
#Helper function to enbed a random image
async def catimage(ctx):
   e = discord.Embed(title="Your title here", description="Your desc here")
   e.set_image(url="https://i.imgur.com/SJgskbM.jpg")
   # file = discord.File("https://images.unsplash.com/face-springmorning.jpg?q=80&fm=jpg&crop=faces&fit=crop&h=32&w=32")
   await ctx.send("Random Image",embed=e)
   
@client.command()
async def sharkimage(ctx): 
	r = requests.get(f"https://api.unsplash.com/photos/random/?client_id={access_key}&query=Shark")
	json_r = r.json()
	print(r.status_code)
	try:
		e = discord.Embed(title = "A Random Shark Image", description = "Yeet")
		e.set_image(url = json_r['urls']['regular'])
		await ctx.send(f"Here you go, {ctx.author.mention}",embed=e)
	except Exception as e:
		print(e)
		await ctx.send("Sorry about that! There seems to be an error!")


@client.command()
async def getgifts(ctx,priceString):
	priceList = priceString.split("-")
	budget = int(priceList[0])
	n = int(priceList[1])
	#linkList = getLinks(n,budget)
	imageList = getImages(n,budget)
	print(imageList)
	for i in range(len(imageList)):
		try:
			e = discord.Embed(title = f"Gift # {i+1}", desciption = "blahaj because why not")
			e.set_image(url = imageList[i])
			await ctx.send(f"Here's a lovely gift under the budget of {budget}, {ctx.author.mention}",embed = e)
		except Exception as e:
			print(e)
			await ctx.send("Not stonks moment here")

@client.command()
async def website(ctx):
	await ctx.send("Check this out! https://melon.blahajgang.lol/")


@client.command()
async def showcommands(ctx):
	await ctx.send("ping: Check the latency of the bot \n \n blahajlang: Convert English to Swedish \n \n blinglish: Convert Swedish to English \n \n catImage: A cute cat because why not \n \n sharkImage: Shows a random shark image \n \n 	getGifts: Gives you gift recommendations based on the specified budget \n \n website: Directs you to the best site ever!")


client.run(bot_token)
