#Brendan Palkowski // SI 206 // Final Project : Financial Analysis

from iexfinance.stocks import Stock
from datetime import datetime
from iexfinance.stocks import get_historical_data
import matplotlib.pyplot as plt
import pandas as pdr
import quandl
import numpy as np
import sqlite3
import csv
import json

quandl.ApiConfig.api_key = "T_LihEBgMTf1thjymFKP"

cache_file = "stocks.json"  #Initiate json cache
cacheDict = {}

def cache_stock():
	"""Cache stock ticker data based on input.
	
	Specifically looks for 1 of 5 tickers. It will pull based on historic data.
	If and else will either return cache if already exist, or do a API pull.
	"""
	start = datetime(2017, 1, 1)
	end = datetime(2018, 1, 1)
	searchTerm = input("Input either MU, S, XOM, MSFT, SIRI ")
	if searchTerm in cacheDict:
		print("Using data from cache")
		return cacheDict[searchTerm]

	else:
		result_found = get_historical_data(searchTerm, start, end)
		cacheDict[searchTerm] = result_found
		file_updater = open(cache_file, 'w')
		file_updater.write(json.dumps(cacheDict))
		file_updater.close()
		return cacheDict[searchTerm]

cache_stock()  #Cache function call

##### MU #####
""" This pulls historic data for MU ticker. This uses IEX API for data.

This will also place the dictionary data into the specific table for MU
"""
start = datetime(2017, 1, 1)
end = datetime(2018, 1, 1)
df_MU = get_historical_data("MU", start, end)
conn = sqlite3.connect('stocks.sqlite')
cur = conn.cursor()
cur.execute('DROP TABLE IF EXISTS Portfolio_MU')
conn.commit()
try:
	cur.execute("""CREATE TABLE Portfolio_MU (open REAL, high REAL, low REAL, close REAL, volume REAL)""")
except:
	print("f")


for tick in df_MU.keys():
		cur.execute('INSERT INTO Portfolio_MU (open, high, low, close, volume) VALUES (?, ?, ?, ?, ?)', [float(df_MU[tick]['open']),float(df_MU[tick]['high']), float(df_MU[tick]['low']), float(df_MU[tick]['close']), float(df_MU[tick]['volume'])])
		conn.commit()


# ##### S #####
""" This pulls historic data for S ticker. This uses IEX API for data.

This will also place the dictionary data into the specific table for S
"""
start = datetime(2017, 1, 1)
end = datetime(2018, 1, 1)
df_S = get_historical_data("S", start, end)
conn = sqlite3.connect('stocks.sqlite')
cur = conn.cursor()
cur.execute('DROP TABLE IF EXISTS Portfolio_S')
conn.commit()
try:
	cur.execute("""CREATE TABLE Portfolio_S (open REAL, high REAL, low REAL, close REAL, volume REAL)""")
except:
	print("f")


for tick in df_S.keys():
		cur.execute('INSERT INTO Portfolio_S (open, high, low, close, volume) VALUES (?, ?, ?, ?, ?)', [float(df_S[tick]['open']),float(df_S[tick]['high']), float(df_S[tick]['low']), float(df_S[tick]['close']), float(df_S[tick]['volume'])])
		conn.commit()


##### MSFT #####
""" This pulls historic data for MSFT ticker. This uses IEX API for data.

This will also place the dictionary data into the specific table for MSFT
"""
start = datetime(2017, 1, 1)
end = datetime(2018, 1, 1)
df_MSFT = get_historical_data("MSFT", start, end)
conn = sqlite3.connect('stocks.sqlite')
cur = conn.cursor()
cur.execute('DROP TABLE IF EXISTS Portfolio_MSFT')
conn.commit()
try:
	cur.execute("""CREATE TABLE Portfolio_MSFT (open REAL, high REAL, low REAL, close REAL, volume REAL)""")
except:
	print("f")


for tick in df_MSFT.keys():
		cur.execute('INSERT INTO Portfolio_MSFT (open, high, low, close, volume) VALUES (?, ?, ?, ?, ?)', [float(df_MSFT[tick]['open']),float(df_MSFT[tick]['high']), float(df_MSFT[tick]['low']), float(df_MSFT[tick]['close']), float(df_MSFT[tick]['volume'])])
		conn.commit()


##### XOM ######
""" This pulls historic data for XOM ticker. This uses IEX API for data.

This will also place the dictionary data into the specific table for XOM
"""
start = datetime(2017, 1, 1)
end = datetime(2018, 1, 1)
df_XOM = get_historical_data("XOM", start, end)
conn = sqlite3.connect('stocks.sqlite')
cur = conn.cursor()
cur.execute('DROP TABLE IF EXISTS Portfolio_XOM')
conn.commit()
try:
	cur.execute("""CREATE TABLE Portfolio_XOM (open REAL, high REAL, low REAL, close REAL, volume REAL)""")
except:
	print("f")


for tick in df_XOM.keys():
		cur.execute('INSERT INTO Portfolio_XOM (open, high, low, close, volume) VALUES (?, ?, ?, ?, ?)', [float(df_XOM[tick]['open']),float(df_XOM[tick]['high']), float(df_XOM[tick]['low']), float(df_XOM[tick]['close']), float(df_XOM[tick]['volume'])])
		conn.commit()


##### SIRI #####
""" This pulls historic data for SIRI ticker. This uses IEX API for data.

This will also place the dictionary data into the specific table for SIRI
"""
start = datetime(2017, 1, 1)
end = datetime(2018, 1, 1)
df_SIRI = get_historical_data("SIRI", start, end)
conn = sqlite3.connect('stocks.sqlite')
cur = conn.cursor()
cur.execute('DROP TABLE IF EXISTS Portfolio_SIRI')
conn.commit()
try:
	cur.execute("""CREATE TABLE Portfolio_SIRI (open REAL, high REAL, low REAL, close REAL, volume REAL)""")
except:
	print("f")


for tick in df_SIRI.keys():
		cur.execute('INSERT INTO Portfolio_SIRI (open, high, low, close, volume) VALUES (?, ?, ?, ?, ?)', [float(df_SIRI[tick]['open']),float(df_SIRI[tick]['high']), float(df_SIRI[tick]['low']), float(df_SIRI[tick]['close']), float(df_SIRI[tick]['volume'])])
		conn.commit()



##### START MODELING #####
##########################
""" This uses QuandL API for historic data pull on the same stock tickers.

This is just initial pull to populate variables.
"""
SIRI = quandl.get("WIKI/SIRI", start_date = "2010-10-1", end_date = "2018-11-19")
MU = quandl.get("WIKI/MU", start_date = "2010-10-1", end_date = "2018-11-19")
Sprint = quandl.get("WIKI/S", start_date = "2010-10-1", end_date = "2018-11-19")
XOM = quandl.get("WIKI/XOM", start_date = "2010-10-1", end_date = "2018-11-19")
MSFT = quandl.get("WIKI/MSFT", start_date = "2010-10-1", end_date = "2018-11-19")

##### CALCULATIONS TO FORM FILE REPORT #####
""" API and mean function from np allows for calculation of mean for each section based on section of time.

Written to text file
Format is as follows:
TICKER : X
"""
reportcalc = "report.txt"
file_updater = open(reportcalc, 'w')
SIRI_mean = np.mean(SIRI['Open'])
MU_mean = np.mean(MU['Open'])
Sprint_mean = np.mean(Sprint['Open'])
XOM_mean = np.mean(XOM['Open'])
MSFT_mean = np.mean(MSFT['Open'])
file_updater.write("SIRI open prices mean: ")
file_updater.write(str(SIRI_mean))
file_updater.write("\n")
file_updater.write("Sprint open prices mean: ")
file_updater.write(str(Sprint_mean))
file_updater.write("\n")
file_updater.write("MU open prices mean: ")
file_updater.write(str(MU_mean))
file_updater.write("\n")
file_updater.write("XOM open prices mean: ")
file_updater.write(str(XOM_mean))
file_updater.write("\n")
file_updater.write("MSFT open prices mean: ")
file_updater.write(str(MSFT_mean))
file_updater.write("\n")


##### OPEN PRICES PER TICKER #####
""" This will plot open prices for each ticker over time interval

Y axis holds valuation in US Dollars
X axis is time in years
Legend is color coded based on ticker
"""
SIRI['Open'].plot(grid=True, color= "r") 
MU['Open'].plot(grid=True, color = "g")
Sprint['Open'].plot(grid=True, color = "m")
XOM['Open'].plot(grid=True, color = "y")      #PLOTS OPEN PRICES + LEGEND
MSFT['Open'].plot(grid=True, color = "b")
plt.title("Open prices per ticker 2010-2018")
plt.xlabel("Date")
plt.ylabel("Dollar Value $")
plt.legend(["SIRI", "MU", "S", "XOM", "MSFT"])
plt.show()

##### ADJUSTED VOLUME PER TICKER #####
""" This will plot adjusted volume for each ticker over time interval

Y axis holds number of shares (volume)
X axis is time in years
Legend is color coded based on ticker
"""
SIRI['Adj. Volume'].plot(grid=True, color= "r") 
MU['Adj. Volume'].plot(grid=True, color = "g")
Sprint['Adj. Volume'].plot(grid=True, color = "m")
XOM['Adj. Volume'].plot(grid=True, color = "y")      
MSFT['Adj. Volume'].plot(grid=True, color = "b")
plt.title("Adj. Volume prices per ticker 2010-2018")
plt.xlabel("Date")
plt.ylabel("Amount of shares")
plt.legend(["SIRI", "MU", "S", "XOM", "MSFT"])
plt.show()

##### LONG/SHORT MOVING AVG #####
""" This will plot long and short moving averages along with upward/downward momentum

Long color is orange
Short color is blue
Red triangle means downward
Green triangle means upward
This also uses pandas dataframe
Keep in mind this is specifically set for SIRI
"""
# Initialize
signals = pdr.DataFrame(index=SIRI.index)
signals['signal'] = 0.0
signals['short_mavg'] = SIRI['Close'].rolling(window=40).mean()
signals['long_mavg'] = SIRI['Close'].rolling(window=100).mean()
signals['signal'][40:] = np.where(signals['short_mavg'][40:] > signals['long_mavg'][40:], 1.0, 0.0)   
signals['positions'] = signals['signal'].diff() #boolean check
fig = plt.figure()
ax1 = fig.add_subplot(111,  ylabel='Value in $')

# Plot the Close price
SIRI['Close'].plot(ax=ax1, color='m', lw=1.)

# Plot the short and long moving averages
signals[['short_mavg', 'long_mavg']].plot(ax=ax1, lw=2.)

# Plot the buy signals
ax1.plot(signals.loc[signals.positions == 1.0].index, 
         signals.short_mavg[signals.positions == 1.0],       #place up-arrow (positives)
         '^', markersize=12, color='g')
         
# Plot the sell signals
ax1.plot(signals.loc[signals.positions == -1.0].index, 
         signals.short_mavg[signals.positions == -1.0],      #place down-arrow (negatives)
         'v', markersize=12, color='r')

plt.show()

##### CONFIDENCE INTERVAL DOWJ INDEX #####
""" This will take data on DOWJ index fund, specifically Open and Close

It uses this data to allow me to take a standard deviation for 1000 days
The equation is just the standard statistic formula
Numpy has functions for mean, standard deviation, and log
log() --> natural logarithm
Tail(1000) --> last 1000 days within the table
1.96 standard represents 95%
Output is placed in same txt file as above.
"""
DOW_table = quandl.get('BCIW/_DOWI') #data grab
DOW_total = DOW_table[['Open','Close']] #table on open, and close price
DOW_log_return = np.log(DOW_total.Close).diff().dropna() #drop NA from tables while setting up boolean array.
bottom_1 = np.mean(DOW_log_return.tail(1000))-1.96*np.std(DOW_log_return.tail(10))/(np.sqrt(len((DOW_log_return.tail(1000)))))
upper_1 = np.mean(DOW_log_return.tail(1000))+1.96*np.std(DOW_log_return.tail(10))/(np.sqrt(len((DOW_log_return.tail(1000)))))

file_updater.write("\n")
file_updater.write("1000 days on 95 confidence interval for DOWJ Index: ")
file_updater.write("\n")
file_updater.write(str(bottom_1))
file_updater.write("\n")
file_updater.write(str(upper_1))
file_updater.write("\n")
file_updater.write("95% confidence that DOWJ returns will fall between in lower and upper bound confidence interval based on the last 1000 days.")
file_updater.close()
