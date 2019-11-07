import pandas as pd
from bs4 import BeautifulSoup
import requests


print('Data Downloading Started.....')

NoData = []  # In this list store NoData URLs
urls = pd.read_csv('AllMutualFundPortfolioLinks.csv')  # Links file, 3952 in this file
count = 1
for url in urls['links']:
    # create request for get data from url
    page = requests.get(url).text
    # parse data using BeautifulSoup for html view
    soup = BeautifulSoup(page, 'html.parser')

############################################# ---EQUITY-- ###########################################################
    # find the table in data using tag name and tag class name
    data = soup.find('table', {'class': 'fund-snapshot-port-holdings-equity'})
    try:
        # Get the name of Mutual fund
        file_name = soup.title.text.split(soup.title.text[soup.title.text.index(':'):])[0].rstrip()
    except:
        file_name = soup.title.text.split(soup.title.text[soup.title.text.index('-'):])[0].rstrip()
    # file_name = soup.title.text.split(soup.title.text[soup.title.text.index(':'):])[0].rstrip()
    table = []  # append table data in list for create DataFrame
    col_name = []  # append columns name for DataFrame
    if data is not None:
        # find all table data row and columns
        for rows in data.find_all('tr'):
            cols = rows.find_all('td')
            if len(cols) >= 5:
                col = []
                table.append(col)
                for i in range(len(cols)):
                    if i == 0:
                        continue
                    col.append(cols[i].text.strip())
        # find all columns name
        for th in data.find_all('tr'):
            name = th.find_all('th')
            if len(name) >= 5:
                for i in range(len(name)):
                    if i == 0:
                        continue
                    col_name.append(name[i].text.strip())
        # create DataFrame using Pandas
        df = pd.DataFrame(table, columns=col_name)
        # Save the Data file in csv format
        df.to_csv('~/PycharmProjects/ScrapeMutualFundData/Downloads/'+str(count) + file_name + 'Equity.csv')

###############################################---HYBRID---#########################################################

    data1 = soup.find('table', {'class': 'fund-snapshot-port-holdings-other'})
    # file_name = soup.title.text.split(soup.title.text[soup.title.text.index(':'):])[0].rstrip()
    tableH = []
    col_nameH = []
    if data1 is not None:
        for rows in data1.find_all('tr'):
            cols = rows.find_all('td')
            if len(cols) >= 6:
                dat = []
                tableH.append(dat)
                for i in range(len(cols)):
                    if i == 0:
                        continue
                    dat.append(cols[i].text.strip())
        for th in data1.find_all('tr'):
            name = th.find_all('th')
            if len(name) == 6:
                for i in range(len(name)):
                    if i == 0:
                        continue
                    col_nameH.append(name[i].text.strip())
        if data is None:
            df1 = pd.DataFrame(tableH, columns=col_nameH)
            df1.to_csv('~/PycharmProjects/ScrapeMutualFundData/Downloads/'+file_name + '.csv')
        else:
            df1 = pd.DataFrame(tableH, columns=col_nameH)
            df1.to_csv('~/PycharmProjects/ScrapeMutualFundData/Downloads/'+str(count) + file_name + 'hybrid.csv')
    else:
        NoData.append([url, file_name])  # Append NoData Urls
        #print(f"No mutual fund found in {file_name}")
    count += 1
df = pd.DataFrame(NoData, columns=["Urls", "Mutual_Fund_Name"])
df.to_csv('~/PycharmProjects/ScrapeMutualFundData/Downloads/Blank Url Data/NoDataUrls.csv')
print(f"{len(NoData)} blank URLs")
