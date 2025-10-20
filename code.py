import os
import yfinance as yf
import pandas as pd

os.environ["YFINANCE_CACHE_DIR"] = "./yf_cache"

df = yf.download("^GDAXI", start="2000-01-01", progress=False, threads=False)

print(df.info())
print(df.head())
