from datetime import datetime
from datetime import timedelta

import pandas as pd


# import requests
# import numpy as np


# Test whether Excel updated on selected date is available:
def is_empty(entry):
    if len(entry) < 2:
        return True
    return False


print(datetime.today().strftime('%Y%m%d'))

# Check for weights updated today
date_avail = datetime.today().strftime('%Y%m%d')

url = ("https://www.ishares.com/de/privatanleger/de/produkte/251918/ishares-listed-private-equity-ucits-etf"
       "/1478358465952.ajax?fileType=csv&fileName=IQQL_holdings&dataType=fund&asOfDate=") + str(date_avail)
df_download_values = pd.read_csv(url, skiprows=2)

if is_empty(df_download_values):
    i = 0
    while is_empty(df_download_values):
        i += 1
        date_avail = datetime.today() - timedelta(days=i)
        date_avail = date_avail.strftime('%Y%m%d')
        url = ("https://www.ishares.com/de/privatanleger/de/produkte/251918/ishares-listed-private-equity-ucits-etf"
               "/1478358465952.ajax?fileType=csv&fileName=IQQL_holdings&dataType=fund&asOfDate=") + str(date_avail)
        df_download_values = pd.read_csv(url, skiprows=2)

df_iShares = df_download_values[['Emittententicker', 'Name', 'Standort', 'Marktwert', 'Gewichtung (%)']]

df_iShares.head()

df_iShares.to_excel("iShares_output.xlsx", index=False)
