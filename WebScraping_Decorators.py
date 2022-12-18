
# pip install requests
# pip install BeautifulSoup4

import requests
from bs4 import BeautifulSoup

response = requests.get("https://www.youtube.com/")
# specify url to get a response from

print(response) # <Response [200]> means we have a succesful response
# 404 means page not found

print(response.content) # entire html content 
print(response.status_code) # 200 means sucessful

soup = BeautifulSoup(response.content,"html.parser") # parse the response using html
print(soup.prettify()) # pretiffy for easy redability


# Beautiful Soup methods
# find('a') # searches for the first 'a' tag
# find_all("div") # returns all 'div' tags
# find_parent("a") 
# find_next_siblings("a")

cards = soup.find("div",attrs={"class":"flex-1"})
print(cards)

for card in cards:
	name = card.find("div",attrs={"class":"video-title"})
	print(name.text.strip("\n"))


## Decorators: send a function as a parameter and return a new function
# for scability

def deco(func):        # concat function passed as a parameter
	def new_func(val1,val2):
		if type(val1) == type(val2):
			return func(val1,val2)
		else:
			return func(str(val1),str(val2))    # additional step added before calling the concat function
	return new_func

@deco # transfers control to the decorator function
def concat(val1,val2):
	return val1 + val2

result = concat(10,10)
print(result)

result = concat("python","String")
print(result)

