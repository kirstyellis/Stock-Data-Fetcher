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
try:
    with open(csv_file, 'w') as csvfile:
        writer = csv.writer(csvfile)
        # writer.writeheader()
        writer.writerow(header_list)
        for data in tickers:
            a = tickers[data]['regularMarketDayLow']
            b = tickers[data]['regularMarketPreviousClose']
            data = [data, a, b]
            writer.writerow(data)
except IOError:
    print("I/O error")



