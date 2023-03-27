import requests
from bs4 import BeautifulSoup
import yfinance as yf
import concurrent.futures
import time

start_time = time.time()

url = "https://finance.yahoo.com/lookup/"

response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')

tickers = []
for tr in soup.find_all('tr'):
    td = tr.find_all('td')
    if len(td) > 0:
        ticker = td[0].text
        ativo = ticker.split()[0]
        tickers.append(ativo)

def calculate_total_dividends(ticker):
    dividend_series = yf.Ticker(ticker).dividends
    if len(dividend_series) == 0:
        return (ticker, 0)
    total_dividends = sum(dividend_series)
    market_price = yf.Ticker(ticker).info['regularMarketPrice']
    dividend_yield = total_dividends / market_price if market_price else 0
    return (ticker, dividend_yield)

with concurrent.futures.ThreadPoolExecutor() as executor:
    future_to_ticker = {executor.submit(calculate_total_dividends, ticker): ticker for ticker in tickers}
    total_dividends_list = [result.result() for result in concurrent.futures.as_completed(future_to_ticker)]

sorted_total_dividends_list = sorted(total_dividends_list, key=lambda x: x[1], reverse=True)

print("As ações com os maiores dividend yields são:")
for ticker, total_dividends in sorted_total_dividends_list[:10]:
    print(f"{ticker}: {total_dividends}")

end_time = time.time()

print("Tempo de execução: {:.2f} segundos".format(end_time - start_time))