import requests
import pandas as pd
from bs4 import BeautifulSoup

print("Links Downloading Started....")
url_all = 'https://www.valueresearchonline.com/funds/fundSelector/risk.asp?amc=4%2C8799%2C5%2C312%2C332%2C8%2C181%2C339%2C8927%2C28%2C302%2C308%2C14%2C9023%2C298%2C9636%2C9655%2C319%2C12232%2C19%2C218%2C185%2C21%2C11141%2C327%2C9054%2C24%2C9055%2C10157%2C15%2C11%2C317%2C186%2C25%2C26%2C187%2C27%2C10%2C9521%2C311%2C12160&cat=equityAll%2CdebtsAll%2ChybridAll&exc=dir'
# Get Request from URL
page = requests.get(url_all).text
# Create HTML Parser to parse data in HTML Format
soup = BeautifulSoup(page, 'html.parser')
# Find Find Data from parse Data by Tag Name and Class name
data = soup.find('div', {'class': 'pull-left'})
# Store all links in list for Create DataFrame
links = []
for rows in data.find_all('tr'):
    cols = rows.find_all('td')
    if len(cols) == 9:
        for i in cols:
            c = i.find('a')
            try:
                if c.get('href')[0:4] != '/pdf':
                    links.append('https://www.valueresearchonline.com' + c.get('href'))
            except:
                break

df = pd.DataFrame(links, columns=['links'])
link = 'https://www.valueresearchonline.com/funds/portfoliovr.asp?schemecode='
Pf_links = []
for i in range(len(df['links'])):
    Pf_links.append(link + df['links'][i].split('=')[1])
PortfolioLinks = pd.DataFrame(Pf_links, columns=['links'])
df.to_csv('AllMutualFundSnapshotLinks.csv')
PortfolioLinks.to_csv('AllMutualFundPortfolioLinks.csv')
print('Links Downloading Completed..')
