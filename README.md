# DAX_stock_prices
# DAX Historical Data Analysis (Python + yfinance)

This project downloads and inspects the historical data of the **DAX Index (^GDAXI)** from Yahoo Finance using the `yfinance` library.  
It demonstrates how to build a reliable data acquisition pipeline with cache management and initial exploratory analysis.

---

##  Overview

- **Index:** DAX (^GDAXI)
- **Data Source:** Yahoo Finance via `yfinance`
- **Period:** 2000–Present
- **Language:** Python 3
- **Libraries:** `pandas`, `yfinance`

---

##  Environment Setup

```bash
# Clone the repository
git clone https://github.com/<your-username>/dax-data-analysis.git
cd dax-data-analysis

# Create and activate virtual environment
python3 -m venv .venv
source .venv/bin/activate

# Install dependencies
pip install yfinance pandas
