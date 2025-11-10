import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import yfinance as yf
import requests
import io

class MortgageDataLoader:
    def __init__(self):
        self.macro_indicators = {}
    
    def load_hmda_data(self, years=range(2018, 2024), states=None):
        """
        Load HMDA data - you'll need to download this from CFPB
        Returns both macro and micro level data
        """
        # HMDA data needs to be downloaded from:
        # https://ffiec.cfpb.gov/data-browser/
        # This is a placeholder for the actual data loading
        pass
    
    def load_fred_data(self, series_list):
        """Load economic data from FRED (Federal Reserve)"""
        import pandas_datareader as pdr
        
        data = {}
        for series in series_list:
            try:
                data[series] = pdr.get_data_fred(series, start='2010-01-01')
            except:
                print(f"Failed to load {series}")
        
        return pd.DataFrame(data)
    
    def get_macro_indicators(self):
        """Get key macroeconomic indicators"""
        indicators = {
            'GDP': 'GDP',  # Real GDP
            'UNRATE': 'UNRATE',  # Unemployment Rate
            'PCE': 'PCE',  # Personal Consumption Expenditures
            'HOUST': 'HOUST',  # Housing Starts
            'CSUSHPINSA': 'CSUSHPINSA',  # Case-Shiller Home Price Index
            'MORTGAGE30US': 'MORTGAGE30US'  # 30-Year Fixed Mortgage Rate
        }
        
        return self.load_fred_data(indicators)
