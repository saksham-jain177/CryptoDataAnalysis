# 🚀 Cryptocurrency Data Analysis

This project fetches live cryptocurrency data for the **top 50 cryptocurrencies** using the **CoinMarketCap API**, analyzes it, and updates a **live Excel sheet** every 5 minutes.  

## 📌 Features
- ✅ **Fetch real-time cryptocurrency data** (Name, Symbol, Price, Market Cap, 24h Volume, Price Change %)
- ✅ **Analyze the data** (Top 5 cryptos by market cap, average price, highest/lowest 24h % change)
- ✅ **Live-updating Excel sheet** with automatic updates every 5 minutes


---

## 📂 Project Structure
```
CryptoDataAnalysis/ 
├── README.md 
├── requirements.txt 
├── config.py  
├── main.py # Main script to fetch, analyze, and update Excel  
├── docs/
│ └── analysis_report.docx 
├── excel/
│ └── live_data.xlsx 
```

---

## 🛠️ Setup Instructions

### 1️⃣ Install Dependencies  
Ensure you have **Python 3.8+** installed, then install the required packages:  
```
pip install -r requirements.txt
```
### 2️⃣ Set Up Your API Key
You need a **CoinMarketCap API** Key or an alternative  to fetch live data.

#### ✅ Using Environment Variables (Recommended)
**Windows (Command Prompt):**
```
set CMC_API_KEY=your_actual_api_key_here
```
#### ✅ Using a .env File (Alternative)
**Create a .env file in the project root:**
```
CMC_API_KEY=your_actual_api_key_here
```
The script will automatically load the API key from .env.

---

## 🚀 Running the Project  
To start fetching live cryptocurrency data and updating the Excel sheet:  
```bash
python main.py
```
This will:  
✔ Fetch and analyze the top 50 cryptocurrencies  
✔ Update the **`excel/live_data.xlsx`** file  
✔ Repeat every **5 minutes**  

To **stop** the script, press `Ctrl + C`.

---

## 📊 Understanding the Output  
### 🔹 **Live-Updated Excel Sheets**
- **Sheet 1: `Crypto Data`** → Full dataset of top 50 cryptos  
- **Sheet 2: `Analysis Summary`** → Avg price, highest & lowest 24h % change  
- **Sheet 3: `Top 5`** → The top 5 cryptocurrencies by market cap  

### 🔹 **Analysis Report**
- The **`docs/analysis_report.docx`** contains a summary of key insights.

---

## 🔒 Security Best Practices
- ❌ **DO NOT hardcode your API key in `config.py`**  
- ✅ Use **environment variables** or **`.env`** to store API keys  
- ✅ Add `.env` to `.gitignore` to prevent accidental commits  

---

## 📝 Contributing  
Feel free to open **issues** or **pull requests** if you'd like to improve the project!

---

## 📜 License  
This project is open-source and licensed under the **MIT License**.

---

## 📬 Contact  
For any questions, feel free to reach out or open a GitHub issue.

---


