from bs4 import BeautifulSoup as sp
import requests
url = "https://www.vulnerability-lab.com/list-of-bug-bounty-programs.php"
webpage = requests.get(url=url)
soup = sp(webpage.content,'html.parser')

print(soup.prettify())

tables = soup.find_all('table')
a_tags = soup.find_all('a')
sites_list = open("likh.txt","a")
for a in a_tags :
    sites_list.write(a.get('href')+"\n")
    
