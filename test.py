import mechanicalsoup

browser = mechanicalsoup.StatefulBrowser()
#browser.open("www.example.com")
#browser.open("https://www.geeksforgeeks.org/print-lists-in-python-4-different-ways/")
browser.open("https://www.theregister.com/offbeat/bofh/")

""" links = browser.page.find_all("a", href=True)

for link in links:
    print(link["href"]) """

print(browser.page)