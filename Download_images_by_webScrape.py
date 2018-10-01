import requests
from bs4 import BeautifulSoup
import os
 

def main():

	os.mkdir("images")
	os.chdir("images")

	url = "https://www.analyticsvidhya.com/blog/2017/09/understaing-support-vector-machine-example-code/" 
	response = requests.get(url)
	data = response.text
	soup = BeautifulSoup(data, "lxml")


	for link in soup.find_all('img'):
		image = link.get("src")
		image_name = os.path.split(image)[1]
		if image.find("SVM") > -1:
			print(image)
			r2 = requests.get(image)
			with open(image_name, "wb") as f:
				f.write(r2.content)

main()