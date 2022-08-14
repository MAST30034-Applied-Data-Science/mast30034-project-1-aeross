# A python script to scrape the twilight data from the website mentioned below.

# install dependencies (if they are not installed yet)
# lxml
# beautifulsoup4

# import libraries
from bs4 import BeautifulSoup
import requests
import pandas as pd
import os


# Note: I'm following the steps as outlined in 
# https://medium.com/analytics-vidhya/how-to-scrape-a-table-from-website-using-python-ce90d0cfb607
# So I'll attribute this code from that link


# create csv file for the data to be saved to
filename = "../data/raw/twilight.csv"
if os.path.exists(filename):
    os.remove(filename)


for month in range(1, 13):
    # note: the urls were accessed on 14/08/2022
    url = f"https://dateandtime.info/citysunrisesunset.php?id=5128581&month={month}&year=2019"
    page = requests.get(url)
    # page should be "<Response [200]>"

    soup = BeautifulSoup(page.text, "lxml")
    # Obtain information from table (there are a few tables in the website, 
    # I want only the 2nd one, where it shows the daily twilight times).
    table = soup.find_all("table", attrs={"class": "sunrise_table"})[2]

    # Obtain the name of every column headers, which are titled <thead>
    #headers = []
    #for i in table.find_all("thead"):
    #    title = i.text
    #    headers.append(title)
    #print(title)
    # It seems like the column headers are nested, so I'll pull it out manually
    headers = ["date", "begin_civ", "end_civ", "begin_nau", "end_nau", "begin_astro", "end_astro"]

    # create dataframe
    data = pd.DataFrame(columns = headers)

    # filling in the data
    for j in table.find_all("tr")[3:]:
        row_data = j.find_all("td")
        
        row = []
        count = 0
        for i in row_data:
            table_data = i.text
            # on the 1st column (date), there is an unnecessary "\n" at the beginning of 
            # the string, and the day is probably not needed as well
            if count == 0:
                table_data = table_data[6:]
                
            # on the 2nd to last column, there seems to be two time formats merged into one
            # the AM PM format and the 24-hour format, all separated by "\n"
            # I will take the AM PM format because they are more consistent in terms of spacing
            else:
                table_data = table_data[-8:-1]
            row.append(table_data)
            count += 1
        
        length = len(data)
        data.loc[length] = row

    # save to csv
    if month == 1:
        data.to_csv(filename, index=False, mode="a")
    else:
        data.to_csv(filename, header=False, index=False, mode="a")
        

# WEB SCRAPING IS SOOOOOO COOL!!!!!

# Note that there is a little bug where during the summer, the astronomical twilight ends at 
# 0:-- PM whereas it should be 10:-- PM. But it doesn't matter, it can easily be fixed later as long as 
# I'm aware, as the purpose of this script is just to scrape and download the datasets.