import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import textwrap
import requests

graphs_out = "./out/trends/"

def main():
    # Fetch the data from the API
    response = requests.get(
        url = "https://asx.api.markitdigital.com/asx-research/1.0/companies/directory"
    )

    # Load the JSON data into a Pandas DataFrame
    if response.status_code == 200:
        df = pd.DataFrame(response.json()['data']['items'])
    else: 
        raise Exception(f"Request to ASX Company Directory failed with Status Code: {response.status_code}")

    # Ensure correct data types
    df['marketCap']                     = pd.to_numeric(df['marketCap'], errors='coerce')
    df['priceChangeFiveDayPercent']     = pd.to_numeric(df['priceChangeFiveDayPercent'], errors='coerce')
    df['industry']                      = df['industry'].astype(str)
    df['symbol']                        = df['symbol'].astype(str)

    # Market Cap by Industry
    mc_ind = df.groupby('industry')['marketCap'].sum().reset_index().sort_values(by='marketCap', ascending=True)
    mc_stk = df.sort_values(by='marketCap', ascending=True)

    # Price Change by Industry
    pc_ind = df.groupby('industry')['priceChangeFiveDayPercent'].sum().reset_index().sort_values(by='priceChangeFiveDayPercent', ascending=True)
    pc_stk = df.sort_values(by='priceChangeFiveDayPercent', ascending=True)

    # Market Cap by Industry Bar Chart
    labels = [textwrap.fill(label, 15) for label in mc_ind['industry']] 
    plt.figure(figsize=(16,14)) 
    plt.barh(mc_ind['industry'], mc_ind['marketCap'] / 1000000)
    plt.ylabel('Industry')
    plt.yticks(range(len(labels)), labels)  # Set wrapped labels
    plt.xlabel('Market Cap (millions)')
    start, end = plt.gca().get_xlim()
    plt.gca().xaxis.set_ticks(np.arange(start, end, 200))
    plt.title('Market Cap by Industry')
    plt.savefig(graphs_out + 'market-cap-by-industry.png')

    # Market Cap by Stock Horizontal Bar Chart
    plt.figure(figsize=(16,8))
    plt.barh(mc_stk['symbol'], mc_stk['marketCap'] / 1000000)
    plt.xlabel('Market Cap (millions)')
    start, end = plt.gca().get_xlim()
    plt.gca().xaxis.set_ticks(np.arange(start, end, 200))
    plt.ylabel('Stock Symbol')
    plt.title('Market Cap by Stock')
    plt.savefig(graphs_out + 'market-cap-by-stock.png')

    # Price Change by Industry Bar Chart
    labels = [textwrap.fill(label, 15) for label in pc_ind['industry']] 
    plt.figure(figsize=(16,14))
    plt.barh(pc_ind['industry'], pc_ind['priceChangeFiveDayPercent'])
    plt.xlabel('Industry')
    plt.yticks(range(len(labels)), labels)  # Set wrapped labels
    plt.ylabel('Price Change (5-Day %)')
    plt.title('Price Change (5-Day %) by Industry')
    plt.savefig(graphs_out + 'price-change-5-day-percent-by-industry.png')

    # Price Change by Stock Horizontal Bar Chart
    plt.figure(figsize=(16,8)) 
    plt.barh(pc_stk['symbol'], pc_stk['priceChangeFiveDayPercent'])
    plt.xlabel('Price Change (5-Day %)')
    plt.ylabel('Stock Symbol')
    plt.title('Price Change (5-Day %) by Stock')
    plt.savefig(graphs_out + 'price-change-5-day-percent-by-stock.png')

    # Show all charts
    plt.show()

if __name__ == "__main__":
    main()
