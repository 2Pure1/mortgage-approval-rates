import pandas as pd
import numpy as np
from datetime import datetime

class DataValidator:
    def __init__(self):
        self.expected_start = '2018-01-01'
        self.expected_end = '2024-12-31'
        
    def validate_time_range(self, data):
        """Validate data covers expected 2018-2024 range"""
        actual_start = data.index.min().strftime('%Y-%m-%d')
        actual_end = data.index.max().strftime('%Y-%m-%d')
        
        validation_results = {
            'expected_period': f'{self.expected_start} to {self.expected_end}',
            'actual_period': f'{actual_start} to {actual_end}',
            'quarters_expected': 28,  # 2018-2024 inclusive = 7 years * 4 quarters
            'quarters_actual': len(data),
            'coverage_score': len(data) / 28
        }
        
        print("📅 TIME RANGE VALIDATION RESULTS:")
        print(f"   • Expected: {validation_results['expected_period']}")
        print(f"   • Actual: {validation_results['actual_period']}")
        print(f"   • Quarters: {validation_results['quarters_actual']}/28")
        print(f"   • Coverage: {validation_results['coverage_score']:.1%}")
        
        return validation_results
    
    def validate_hmda_simulation(self, hmda_data):
        """Validate simulated HMDA data for 2018-2024"""
        validation = {
            'has_2018_data': '2018' in hmda_data.index.strftime('%Y').values,
            'has_2024_data': '2024' in hmda_data.index.strftime('%Y').values,
            'approval_rate_range': (
                hmda_data['approval_rate'].min() >= 50 and 
                hmda_data['approval_rate'].max() <= 85
            ),
            'covid_period_present': any(
                (hmda_data.index >= '2020-03-01') & (hmda_data.index <= '2021-12-31')
            )
        }
        
        print("🏦 HMDA DATA VALIDATION RESULTS:")
        for check, result in validation.items():
            status = "✅" if result else "❌"
            print(f"   • {check}: {status}")
        
        return validation
