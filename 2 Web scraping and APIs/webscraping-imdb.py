"""
Web scraping of IMDb. Get movie title, rating, director and so on.

You might need some extra libraries for this one to work.
Install them via pip:

 	pip install BeautifulSoup4
 	pip install lxml

"""

import urllib.request
from lxml import html
from bs4 import BeautifulSoup 

# Scrape all HTML from webpage.
def scrapewebpage(url):
	# Open URL and get HTML.
	web = urllib.request.urlopen(url)

	# Make sure there wasn't any errors opening the URL.
	if (web.getcode() == 200):
		html = web.read()
		return(html)
	else:
		print("Error %s reading %s" % str(web.getcode()), url)

# Helper function that scrape the webpage and turn it into soup.
def makesoup(url):
	html = scrapewebpage(url)
	return(BeautifulSoup(html, "lxml"))

# Scrape Interstellar (2014) by using our own function "makesoup" we defined above.
soup = makesoup('http://www.imdb.com/title/tt0816692/')

# Get movie title.
title = soup.find(itemprop="name").get_text()
title = title.strip() # Remove whitespace before and after text

# Get movie year.
year = soup.find(id="titleYear").get_text()
year = year[1:5] # Remove parentheses, make (2014) into 2014.

# Get movie duration.
duration = soup.find(itemprop="duration").get_text()
duration = duration.strip() # Remove whitespace before and after text

# Get director.
director = soup.find(itemprop="director").get_text()
director = director.strip() # Remove whitespace before and after text

# Get movie rating.
rating = soup.find(itemprop="ratingValue").get_text()

# Get cast list.
actors = []
for castlist in soup.find_all("table", "cast_list"):
	for actor in castlist.find_all(itemprop="actor"):
		actors.append(actor.get_text().strip())

# Present the results.
print("Movie:    " + title)
print("Year:     " + year)
print("Director: " + director)
print("Duration: " + duration)
print("Rating:   " + rating)

# Present list of actors.
print()
print("Notable actors:")
for actor in actors:
	print("- " + actor)