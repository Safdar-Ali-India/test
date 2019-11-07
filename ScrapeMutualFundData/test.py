import pandas as pd
from bs4 import BeautifulSoup
import requests
import csv
import time

print('Data Downloading Started.....')
NoData = []  # In this list store NoData URLs
col_name = []
col_nameH = []
# url='https://www.valueresearchonline.com/funds/portfoliovr.asp?schemecode=15739'
urls = pd.read_csv('AllMutualFundPortfolioLinks.csv')  # Links file, 3952 in this file
count = 1
count1 = 1
for url in urls['links']:
    # create request for get data from url
    page = requests.get(url).text
    # parse data using BeautifulSoup for html view
    soup = BeautifulSoup(page, 'html.parser')

    ############################################# ---EQUITY-- ###########################################################
    data = soup.find('table', {'class': 'fund-snapshot-port-holdings-equity'})
    try:
        # Get the name of Mutual fund
        file_name = soup.title.text.split(soup.title.text[soup.title.text.index(':'):])[0].rstrip()
    except:
        file_name = soup.title.text.split(soup.title.text[soup.title.text.index('-'):])[0].rstrip()
        # table = []# append columns name for DataFrame
    if data is not None:
        if len(col_name) <= 2:
            # find all columns name
            for th in data.find_all('tr'):
                name = th.find_all('th')
                if len(name) == 7:
                    for i in range(len(name)):
                        if i == 0:
                            continue
                        col_name.append(name[i].text.strip())
    try:
        with open('EquityTest.csv', 'r') as readFile:
            reader = csv.reader(readFile)
            lines = list(reader)
    except:
        lines = str(1)
    if len(lines[0]) <= 1 and len(col_name) >= 5:
        with open('EquityTest.csv', 'a') as csvFile:
            writer = csv.writer(csvFile)
            writer.writerow(col_name)
        csvFile.close()
    if data is not None:
        tab = [str(count) + '.' + file_name]
        with open('EquityTest.csv', 'a') as csvFile:
            writer = csv.writer(csvFile)
            writer.writerow(tab)
        for rows in data.find_all('tr'):
            cols = rows.find_all('td')
            if len(cols) >= 6:
                col = []
                for i in range(len(cols)):
                    if i == 0:
                        continue
                    col.append(cols[i].text.strip())
                with open('EquityTest.csv', 'a') as csvFile:
                    writer = csv.writer(csvFile)
                    writer.writerow(col)
        count += 1

    ####################################----HYBRID-----##########################################################################
    data1 = soup.find('table', {'class': 'fund-snapshot-port-holdings-other'})
    if data1 is not None and len(col_nameH) <= 1:
        for th in data1.find_all('tr'):
            name = th.find_all('th')
            if len(name) == 6:
                for i in range(len(name)):
                    if i == 0:
                        continue
                    col_nameH.append(name[i].text.strip())
    try:
        with open('DebtTest.csv', 'r') as readFile:
            reader = csv.reader(readFile)
            line1 = list(reader)
    except:
        line1 = str(1)
    try:
        with open('HybridTest.csv', 'r') as readFile:
            reader = csv.reader(readFile)
            line = list(reader)
    except:
        line = str(1)

    if data1 is not None and len(line1[0]) <= 1 and len(col_nameH) >= 5 and data1.th.text.split()[1] == 'Debt':
        with open('DebtTest.csv', 'a') as csvFile:
            writer = csv.writer(csvFile)
            writer.writerow(col_nameH)
        csvFile.close()
    if data1 is not None and len(line[0]) <= 1 and len(col_nameH) >= 5 and data1.th.text.split()[1] != 'Debt':
        with open('HybridTest.csv', 'a') as csvFile:
            writer = csv.writer(csvFile)
            writer.writerow(col_nameH)
        csvFile.close()
    try:
        with open('HybridTest.csv', 'r') as readFile:
            reader = csv.reader(readFile)
            line = list(reader)
    except:
        pass
    try:
        with open('DebtTest.csv', 'r') as readFile:
            reader = csv.reader(readFile)
            line1 = list(reader)
    except:
        pass
    if data1 is not None and len(line1[0]) >= 4 and len(data1) >= 15:
        tabH = [str(count1) + '.' + file_name]
        if data1.th.text.split()[1] == 'Debt':
            with open('DebtTest.csv', 'a') as csvFile:
                writer = csv.writer(csvFile)
                writer.writerow(tabH)
        else:
            with open('HybridTest.csv', 'a') as csvFile:
                writer = csv.writer(csvFile)
                writer.writerow(tabH)
        for rows in data1.find_all('tr'):
            cols = rows.find_all('td')
            if len(cols) >= 6:
                dat = []
                for i in range(len(cols)):
                    if i == 0:
                        continue
                    dat.append(cols[i].text.strip())
                if data1.th.text.split()[1] == 'Debt':
                    with open('DebtTest.csv', 'a') as csvFile:
                        writer = csv.writer(csvFile)
                        writer.writerow(dat)
                elif data1.th.text.split()[1] != 'Debt':
                    with open('HybridTest.csv', 'a') as csvFile:
                        writer = csv.writer(csvFile)
                        writer.writerow(dat)
        count1 += 1

print('Completed')

print(url)