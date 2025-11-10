import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import TimeSeriesSplit

class MortgagePreprocessor:
    def __init__(self):
        self.scaler = StandardScaler()
        self.lag_periods = 4  # 4 quarters for annual lags
    
    def create_macro_features(self, macro_data):
        """Create macroeconomic features with lags"""
        features = macro_data.copy()
        
        # Create percentage changes
        for col in features.columns:
            if col != 'UNRATE':  # Unemployment is already a rate
                features[f'{col}_pct_change'] = features[col].pct_change(4)  # YoY change
        
        # Create lagged features
        for lag in range(1, self.lag_periods + 1):
            for col in ['GDP_pct_change', 'UNRATE', 'CSUSHPINSA_pct_change']:
                features[f'{col}_lag_{lag}'] = features[col].shift(lag)
        
        # Create interaction terms
        features['unemployment_hpi_interaction'] = (
            features['UNRATE_lag_1'] * features['CSUSHPINSA_pct_change_lag_1']
        )
        
        return features.dropna()
    
    def prepare_micro_data(self, hmda_data, macro_features):
        """Prepare individual loan application data"""
        # Merge with macroeconomic conditions
        hmda_data['application_date'] = pd.to_datetime(hmda_data['action_taken_date'])
        hmda_data['quarter'] = hmda_data['application_date'].dt.to_period('Q')
        macro_features['quarter'] = macro_features.index.to_period('Q')
        
        merged_data = hmda_data.merge(
            macro_features, 
            on='quarter', 
            how='left'
        )
        
        # Create target variable
        merged_data['approved'] = (merged_data['action_taken'] == 1).astype(int)
        
        # Clean applicant features
        merged_data['debt_to_income_ratio'] = (
            merged_data['total_loan_costs'] / merged_data['applicant_income']
        )
        
        return merged_data
