
from urllib.request import urlopen
from bs4 import BeautifulSoup
import openpyxl as xl
from openpyxl.styles import Font





#webpage = 'https://www.boxofficemojo.com/weekend/chart/'
webpage = 'https://www.boxofficemojo.com/year/2022/'

page = urlopen(webpage)			

soup = BeautifulSoup(page, 'html.parser')

title = soup.title

print(title.text)

movie_rows = soup.findAll('tr')
#print(movie_rows)

for x in range(1,6):
    td = movie_rows[x].findAll('td')
    print(td[1].text)
    input()

    
##
##
##
##

