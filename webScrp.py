import requests
from bs4 import BeautifulSoup as bs
 

github_user = input("ur user name of github : ")
github_url = "https://github.com/"+github_user
r = requests.get(github_url)
print (r)
soup = bs(r.content , "html.parser")
profail_image = soup.find("img", {"alt","Avatar"} )["src"]
print(profail_image)