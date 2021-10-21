import requests
import bs4
import sys
from tp_pkg import voice_to_text
from tp_pkg import print_say
# Define the news_teaser() function


def news_teaser():
    res = requests.get('https://www.npr.org/sections/news/')
    res.raise_for_status()
    # Use beautiful soup to parse the code
    soup = bs4.BeautifulSoup(res.text, 'html.parser')
    # Get the div tags that contain titles and teasers
    div_tags = soup.find_all('div', class_="item-info")
    news_index = 1
    for div_tag in div_tags:
        print_say(f'News Summary {news_index}')
        h2tag = div_tag.find('h2', class_="title")
        print_say(h2tag.text)
        ptag = div_tag.find('p', class_="teaser")
        print_say(ptag.text)
        news_index+=1


# Print and ask you if you like to hear the news summary
print_say("Would you like to hear the NPR news summary?")
# Capture your voice command
inp = voice_to_text().lower()
# If you answer yes, activate the newscast
if inp == "yes":
    news_teaser()
# Otherwise, exit the script
else:
    sys.exit