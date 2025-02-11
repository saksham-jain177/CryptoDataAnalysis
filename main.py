import requests
import pandas as pd
import schedule
import time
import config  # This imports your API_KEY and API_URL from config.py

def fetch_data():
    """
    Fetch live data for the top 50 cryptocurrencies using CoinMarketCap API.
    """
    url = config.API_URL
    parameters = {
        'start': '1',
        'limit': '50',
        'convert': 'USD'
    }
    headers = {
        'Accepts': 'application/json',
        'X-CMC_PRO_API_KEY': config.API_KEY,
    }
    try:
        response = requests.get(url, params=parameters, headers=headers)
        response.raise_for_status()  # Raise an error for bad status codes
        data = response.json()['data']
        return data
    except Exception as e:
        print("Error fetching data:", e)
        return None

def process_data(data):
    """
    Process the fetched JSON data and convert it into a Pandas DataFrame.
    """
    if data is None:
        return None

    rows = []
    for coin in data:
        # Extract required fields from each cryptocurrency data item.
        name = coin.get('name')
        symbol = coin.get('symbol')
        quote = coin.get('quote', {}).get('USD', {})
        price = quote.get('price')
        market_cap = quote.get('market_cap')
        volume_24h = quote.get('volume_24h')
        percent_change_24h = quote.get('percent_change_24h')
        
        rows.append({
            'Name': name,
            'Symbol': symbol,
            'Price (USD)': price,
            'Market Cap': market_cap,
            'Volume 24h': volume_24h,
            'Percent Change 24h': percent_change_24h
        })
    
    df = pd.DataFrame(rows)
    return df

def analyze_data(df):
    """
    Perform basic analysis on the DataFrame and print the results.
    - Top 5 cryptocurrencies by market cap.
    - Average price of the top 50 cryptocurrencies.
    - Highest and lowest 24h % price change.
    """
    if df is None or df.empty:
        print("No data available for analysis.")
        return
    
    # Identify the top 5 cryptocurrencies by Market Cap
    top5 = df.nlargest(5, 'Market Cap')
    avg_price = df['Price (USD)'].mean()
    highest_change = df['Percent Change 24h'].max()
    lowest_change = df['Percent Change 24h'].min()
    
    print("\n===== Analysis =====")
    print("Top 5 Cryptocurrencies by Market Cap:")
    print(top5[['Name', 'Symbol', 'Market Cap']])
    print("\nAverage Price of Top 50 Cryptocurrencies: ${:.2f}".format(avg_price))
    print("Highest 24h % Price Change: {:.2f}%".format(highest_change))
    print("Lowest 24h % Price Change: {:.2f}%".format(lowest_change))
    print("====================\n")

def update_excel(df):
    """
    Update the live Excel sheet with the latest data and analysis.
    The Excel workbook will have three sheets:
    - 'Crypto Data' with the full dataset.
    - 'Analysis Summary' with average price and 24h change stats.
    - 'Top 5' listing the top 5 cryptocurrencies by market cap.
    """
    if df is None or df.empty:
        print("No data available to update Excel file.")
        return

    file_path = 'excel/live_data.xlsx'
    try:
        # Create an Excel writer using openpyxl as the engine.
        with pd.ExcelWriter(file_path, engine='openpyxl') as writer:
            # Write the complete cryptocurrency data to the first sheet.
            df.to_excel(writer, sheet_name='Crypto Data', index=False)
            
            # Create an analysis summary.
            avg_price = df['Price (USD)'].mean()
            highest_change = df['Percent Change 24h'].max()
            lowest_change = df['Percent Change 24h'].min()
            analysis_summary = pd.DataFrame({
                'Metric': ['Average Price (USD)', 'Highest 24h % Change', 'Lowest 24h % Change'],
                'Value': [avg_price, highest_change, lowest_change]
            })
            analysis_summary.to_excel(writer, sheet_name='Analysis Summary', index=False)
            
            # Write the Top 5 cryptocurrencies by market cap to a separate sheet.
            top5 = df.nlargest(5, 'Market Cap')
            top5.to_excel(writer, sheet_name='Top 5', index=False)
        
        print("Excel file updated successfully at 'excel/live_data.xlsx'.")
    except Exception as e:
        print("Error updating Excel file:", e)

def job():
    """
    The main job to be scheduled:
    1. Fetch data.
    2. Process the data.
    3. Analyze the data.
    4. Update the Excel sheet.
    """
    print("Starting job at", time.strftime("%Y-%m-%d %H:%M:%S"))
    data = fetch_data()
    if data is not None:
        df = process_data(data)
        if df is not None:
            analyze_data(df)
            update_excel(df)
    print("Job completed.\n")

if __name__ == "__main__":
    # Run the job once immediately.
    job()
    
    # Schedule the job to run every 5 minutes.
    schedule.every(5).minutes.do(job)
    print("Scheduler started. The job will run every 5 minutes. Press Ctrl+C to stop.")
    
    try:
        while True:
            schedule.run_pending()
            time.sleep(1)
    except KeyboardInterrupt:
        print("Scheduler stopped by user.")
