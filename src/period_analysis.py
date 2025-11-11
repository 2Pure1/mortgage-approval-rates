import pandas as pd
import matplotlib.pyplot as plt

class PeriodAnalysis:
    def __init__(self):
        self.periods = {
            'pre_covid': ('2018-01-01', '2020-02-29'),
            'covid_acute': ('2020-03-01', '2021-12-31'),
            'post_covid': ('2022-01-01', '2024-12-31')
        }
    
    def analyze_by_period(self, data, target_col='approval_rate'):
        """Analyze patterns across different economic periods"""
        results = {}
        
        for period_name, (start, end) in self.periods.items():
            period_data = data.loc[start:end]
            if len(period_data) > 0:
                results[period_name] = {
                    'mean_approval': period_data[target_col].mean(),
                    'std_approval': period_data[target_col].std(),
                    'quarters': len(period_data),
                    'economic_context': self.get_period_context(period_name)
                }
        
        return pd.DataFrame(results).T
    
    def get_period_context(self, period_name):
        """Provide economic context for each period"""
        contexts = {
            'pre_covid': 'Stable growth, low unemployment, moderate rates',
            'covid_acute': 'Pandemic volatility, stimulus, forbearance programs', 
            'post_covid': 'High inflation, rapid rate hikes, housing market adjustment'
        }
        return contexts.get(period_name, 'Unknown period')
