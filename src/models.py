import pandas as pd
import numpy as np
from sklearn.linear_model import LogisticRegression, LinearRegression
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier
from sklearn.metrics import accuracy_score, roc_auc_score, mean_squared_error
import statsmodels.api as sm
from statsmodels.tsa.arima.model import ARIMA
import xgboost as xgb

class MortgageModel:
    def __init__(self, model_type='logistic'):
        self.model_type = model_type
        self.model = None
        self.feature_names = None
    
    def fit_macro_model(self, X, y):
        """Macro-level model using linear regression or ARIMA"""
        if self.model_type == 'linear':
            self.model = LinearRegression()
            self.model.fit(X, y)
        elif self.model_type == 'arima':
            self.model = ARIMA(y, order=(1,1,1))
            self.model = self.model.fit()
        
        return self
    
    def fit_micro_model(self, X, y):
        """Micro-level model using logistic regression"""
        if self.model_type == 'logistic':
            self.model = LogisticRegression(random_state=42, max_iter=1000)
        elif self.model_type == 'random_forest':
            self.model = RandomForestClassifier(n_estimators=100, random_state=42)
        elif self.model_type == 'xgboost':
            self.model = xgb.XGBClassifier(random_state=42)
        
        self.model.fit(X, y)
        self.feature_names = X.columns.tolist()
        return self
    
    def predict(self, X):
        if self.model_type == 'arima':
            return self.model.forecast(steps=len(X))
        return self.model.predict(X)
    
    def predict_proba(self, X):
        if hasattr(self.model, 'predict_proba'):
            return self.model.predict_proba(X)[:, 1]
        return self.predict(X)

class AdvancedEconometricModel:
    """More advanced panel data models"""
    
    def fixed_effects_logit(self, data, entity_col, time_col):
        """Fixed effects logistic regression for panel data"""
        # Using statsmodels for more econometric rigor
        formula = "approved ~ applicant_income + loan_amount + debt_to_income_ratio + UNRATE_lag_1 + CSUSHPINSA_pct_change_lag_1"
        
        model = sm.Logit.from_formula(
            formula, 
            data
        )
        result = model.fit()
        return result
