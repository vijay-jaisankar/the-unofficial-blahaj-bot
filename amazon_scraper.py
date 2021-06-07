from bs4 import BeautifulSoup
from urllib.request import urlopen
import urllib.request
from random import *
import copy
import requests

headers = {"User-Agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.66 Safari/537.36"}


def getAmazonLink(budget):
	return "https://www.amazon.in/s?k=gift&rh=p_36%3A-"+str(budget)+"00&s=review-rank"



def getLinks(n,budget):
	link = getAmazonLink(budget)
	r = requests.get(link, headers=headers)
	soup = BeautifulSoup(r.text,'lxml')
	links = soup.find_all("a", attrs={'class':'a-link-normal a-text-normal'})
	

	links_list = []
	for link in links:
		links_list.append(link.get('href'))
	
	return links_list[:n]

def getImages(n,budget):
	link = getAmazonLink(budget)
	r = requests.get(link,headers=headers)
	soup = BeautifulSoup(r.text,'lxml')
	image_paths = soup.find_all("img",attrs={'class':'s-image'})
	links = image_paths[:n]

	images_list = []
	for link in links:
		images_list.append(link.get("src"))
	return images_list[:n]
