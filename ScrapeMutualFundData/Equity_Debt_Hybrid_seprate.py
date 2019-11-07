import pandas as pd
from bs4 import BeautifulSoup
import requests
import csv
import sys


# Processing bar
def update_progress(job_title, progress):
    length = 50  # modify this to change the length
    block = int(round(length * progress))
    msg = "\r{0}: [{1}] {2}%".format(job_title, "#" * block + "-" * (length - block), round(progress * 100))
    if progress >= 1: msg += " DONE\r\n"
    sys.stdout.write(msg)
    sys.stdout.flush()


print('Data Downloading Started.....')
NoData = []  # In this list store NoData URLs
col_name = []
col_nameH = []
urls = pd.read_csv('AllMutualFundPortfolioLinks.csv')  # Links file, 3952 in this file
count = 1
count1 = 1
attempt_count = 1
progress = len(urls['links'])
k = 0

# looping in CSV file.
for url in urls['links']:
    attempt_count = attempt_count + 1
    # call function for show processing
    update_progress("Downloading", k / progress)
    k += 1
    if type(url) == str:

        # create request for get data from url
        page = requests.get(url).text
        # parse data using BeautifulSoup for html view
        soup = BeautifulSoup(page, 'html.parser')

        ############################################# ---EQUITY-- ###########################################################
        # find the table in received data
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
        dt = soup.find('div', {'class': 'pull-left fund-detail'})
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

        if data1 is not None and len(line1[0]) <= 1 and len(col_nameH) >= 5 and dt.tr.text.replace('\n', '').split(':')[
            1] == 'Debt':
            with open('DebtTest.csv', 'a') as csvFile:
                writer = csv.writer(csvFile)
                writer.writerow(col_nameH)
            csvFile.close()
        if data1 is not None and len(line[0]) <= 1 and len(col_nameH) >= 5 and dt.tr.text.replace('\n', '').split(':')[
            1] != 'Debt':
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
            if dt.tr.text.replace('\n', '').split(':')[1] == 'Debt':
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
                    if dt.tr.text.replace('\n', '').split(':')[1] == 'Debt':
                        with open('DebtTest.csv', 'a') as csvFile:
                            writer = csv.writer(csvFile)
                            writer.writerow(dat)
                    elif dt.tr.text.replace('\n', '').split(':')[1] != 'Debt':
                        with open('HybridTest.csv', 'a') as csvFile:
                            writer = csv.writer(csvFile)
                            writer.writerow(dat)
            count1 += 1
    else:
        print('Invalid URL')
        break
