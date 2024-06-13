import mechanicalsoup
import pandas as pd
import sqlite3

URL = "https://www.theregister.com/offbeat/bofh/"
domain = "https://www.theregister.com"

# create browser object & open URL
browser = mechanicalsoup.StatefulBrowser()
browser.open(URL)

# extract all table headers (entire "Distribution" column)
#linkPart = [browser.page.find_all("href", attrs={"class": "story_link"})]
linkPart = [browser.page.find_all("a", href=True)]

print(len(linkPart))