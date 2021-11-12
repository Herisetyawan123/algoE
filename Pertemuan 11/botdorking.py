import requests, re

url = "https://www.google.co.id/search?q="
dork = "inurl /news.php id= site.co.il"


# returns = '<div class="yuRUbf" original_target="http://www.abbaruna.com/news.php?id=1" waprocessedid="5j3z1f"  style="display: inline-block;"><a href="http://www.abbaruna.com/news.php?id=1"'
print(requests.get(url+dork).text)
print(re.findall('original_target="(.*)" waprocessedid', requests.get(url+dork).text))