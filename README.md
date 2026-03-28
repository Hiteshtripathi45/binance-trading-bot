# Binance Futures Testnet Trading Bot

## 📌 Overview

This is a simple Python-based trading bot that places MARKET and LIMIT orders on Binance Futures Testnet (USDT-M).

The application provides a command-line interface (CLI) for placing orders, along with input validation, logging, and structured code design.

---

## 🚀 Features

* Place MARKET orders
* Place LIMIT orders
* Supports BUY and SELL
* CLI-based input using argparse
* Input validation (type, side, quantity, price)
* Logging of requests, responses, and errors
* Clean and modular code structure

---

## 🛠️ Setup Instructions

### 1. Clone the repository

```bash
git clone <your-repo-link>
cd trading_bot
```

### 2. Create virtual environment

```bash
python -m venv venv
source venv/bin/activate   # Linux/Mac
venv\Scripts\activate      # Windows
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Add API keys

Create a `.env` file in the root directory:

```
API_KEY=your_api_key_here
API_SECRET=your_api_secret_here
```

> Note: Use Binance Futures Testnet API keys.

---

## ▶️ How to Run

### 🔹 MARKET Order Example

```bash
python cli.py --symbol BTCUSDT --side BUY --type MARKET --quantity 0.002
```

### 🔹 LIMIT Order Example

```bash
python cli.py --symbol BTCUSDT --side BUY --type LIMIT --quantity 0.002 --price 50000
```

---

## 📊 Output

The program prints:

* Order request summary
* Order response details:

  * Order ID
  * Status
  * Executed Quantity
  * Average Price

---

## 🧾 Logging

Logs are stored in:

```
bot.log
```

Logs include:

* API request details
* API response
* Errors (if any)

Separate log files provided:

* `market_order.log`
* `limit_order.log`

---

## ⚠️ Validation

The application validates:

* Order type (MARKET / LIMIT)
* Side (BUY / SELL)
* Quantity (> 0)
* Price required for LIMIT orders

---

## 📁 Project Structure

```
trading_bot/
│
├── bot/
│   ├── client.py
│   ├── orders.py
│   ├── validators.py
│   ├── logging_config.py
│
├── cli.py
├── .env
├── requirements.txt
├── README.md
```

---

## 📝 Assumptions

* Binance Futures Testnet is used (no real money involved)
* Minimum notional value (≥ 100 USDT) is respected
* User provides correct symbol format (e.g., BTCUSDT)

---

## ✅ Conclusion

This project demonstrates:

* API integration with Binance
* Clean CLI-based application design
* Input validation and error handling
* Logging for debugging and traceability
