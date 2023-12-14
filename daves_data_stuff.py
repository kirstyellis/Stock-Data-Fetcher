# Importing the yfinance package
import yfinance as yf
import csv

file_name = '/home/kirstyellis/dave_ws/src/Stock-Data-Fetcher/list_tickers.txt'

ticker_strings = []
with open(file_name) as file:
    with open(file_name) as f:
        lines = f.read().splitlines()
        ticker_strings.append(lines[0].split(','))

tickers = {}

for i in ticker_strings[0]:
    try:
        tickers[i] = yf.Ticker(i).info
        market_price = tickers[i]['regularMarketDayLow']
        previous_close_price = tickers[i]['regularMarketPreviousClose']
        print('Ticker: ', i)
        print('Market Price:', market_price)
        print('Previous Close Price:', previous_close_price)
    except:
        continue

header_list = ['Ticker', 'regularMarketDayLow', 'regularMarketPreviousClose']

csv_file = "/home/kirstyellis/dave_ws/src/Stock-Data-Fetcher/ticker_output.csv"

data_i_want = ['regularMarketDayLow', 'regularMarketPreviousClose']

try:
    with open(csv_file, 'w') as csvfile:
        writer = csv.writer(csvfile)
        # writer.writeheader()
        writer.writerow(header_list)

        for data in tickers:
            # create an empty list for my output
            data_list = []
            # The first thing I want in my output list is the ticker name string
            data_list.append(data)
            # for each data item in the list that I want, I check if it exists in the ticker dictionary, if it doesn't exist, I put an empty string in that field
            for j in data_i_want:
                if j in tickers[data]:
                    data_list.append(tickers[data][j])
                else:
                    data_list.append('')

            writer.writerow(data_list)
except IOError:
    print("I/O error")


