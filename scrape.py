import requests
import pprint

url = 'https://www.monster.com/jobs/search/?q=Software-Developer&where=Australia'
page = requests.get(url)

pp = pprint.PrettyPrinter()

pp.pprint(page)