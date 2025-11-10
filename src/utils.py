import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime

def create_economic_interpretation(feature_name):
    """Provide business context for economic indicators"""
    interpretations = {
        'Unemployment': "Higher unemployment increases lender risk aversion",
        'GDP_Growth': "Strong economic growth signals borrower capacity improvement", 
        'Case_Shiller': "Rising home prices improve collateral value for lenders",
        'Mortgage_Rate': "Higher rates reduce affordability and increase default risk",
        'Income': "Higher incomes improve debt-to-income ratios and repayment capacity"
    }
    
    for key, interpretation in interpretations.items():
        if key in feature_name:
            return interpretation
    return "General economic indicator affecting lender risk assessment"

def plot_feature_importance(feature_names, coefficients, top_n=10):
    """Plot feature importance from model coefficients"""
    importance_df = pd.DataFrame({
        'feature': feature_names,
        'importance': np.abs(coefficients)
    }).sort_values('importance', ascending=False).head(top_n)
    
    plt.figure(figsize=(10, 6))
    sns.barplot(data=importance_df, y='feature', x='importance')
    plt.title(f'Top {top_n} Feature Importance for Mortgage Approval Prediction')
    plt.xlabel('Absolute Coefficient Value')
    plt.tight_layout()
    return plt.gcf()

def calculate_business_metrics(y_true, y_pred, model_name):
    """Calculate business-oriented performance metrics"""
    from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
    
    mae = mean_absolute_error(y_true, y_pred)
    rmse = np.sqrt(mean_squared_error(y_true, y_pred))
    r2 = r2_score(y_true, y_pred)
    
    # Business context metrics
    mean_approval = y_true.mean()
    mae_pct = (mae / mean_approval) * 100
    
    return {
        'model': model_name,
        'mae': mae,
        'rmse': rmse, 
        'r2': r2,
        'mae_percentage': mae_pct,
        'interpretation': f"Model predicts approval rates within ±{mae:.2f} percentage points"
    }
