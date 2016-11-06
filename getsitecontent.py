import requests
import nltk
from nltk.corpus import stopwords
from bs4 import BeautifulSoup
import re

headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
requests.packages.urllib3.disable_warnings()

def getSiteContent(site):
	try:
		response = requests.get(site, headers=headers)
		htmlSource = response.text
	except Exception as e: #Some websites are inaccesible
		return ''

	#Extracts data from html page
	soup = BeautifulSoup(htmlSource, 'html.parser')
	#Removes all the script/css tags
	for script in soup.find_all({'script' : True, 'style' : True}):
		script.extract()
		
	text = soup.get_text()
	engStopWords = set(stopwords.words('english'))
	
	# break into lines and remove leading and trailing space on each
	lines = (line.strip() for line in text.splitlines())
	# break multi-headlines into a line each
	chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
	# drop blank lines
	text = ' '.join(chunk for chunk in chunks if chunk)
	
	#Removing english stop words
	textList = text.split()
	for token in engStopWords.intersection(textList):
		while token in textList:
			textList.remove(token)

	text = ' '.join(word for word in textList if word)

	# Remove ',', '/', '%', ':'
	text = re.sub(r'([,/%:".\(\)\[\]\{\}\+\!])', '', text)
	# Remove digits
	text = re.sub(r'\d+', '', text)
	# Remove non-ASCII
	text = re.sub(r'[^\x00-\x7F]',' ', text)
	
	#Removing 1 to 3 character words
	text = re.sub(r'\b[\w]{1,3}\b', ' ', text)
	text = re.sub(r'\s{2,}', ' ', text)

	return text
