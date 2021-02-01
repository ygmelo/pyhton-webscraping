import pandas as pd
import requests
from bs4 import BeautifulSoup
import io

class WebScraping:
		def __init__(self, headers, url, idSearch):
			self.headers = headers
			self.url = url
			self.id  = idSearch

		def scraping(self):
			req = requests.get(self.url, self.headers)

			if(req.status_code == 200):
				content = req.content
				soup    = BeautifulSoup(content, 'html.parser')
				texto   = soup.find(id = self.id).findAll("p")[1].getText()

			print(texto)

			with io.open('texto.txt', "w", encoding="utf-8") as f:
	 			f.write(str(texto))


header = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.87 Safari/537.36'}
https  = "https://pt.wikipedia.org/wiki/Lindernia_cambodgiana"
target = "mw-content-text"

search = WebScraping(header, https, target)
search.scraping();