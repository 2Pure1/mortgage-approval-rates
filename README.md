# Mortgage Approval Rate Forecasting Model

## Project Overview
This project builds econometric models to forecast mortgage approval rates based on macroeconomic conditions using HMDA data and BEA economic indicators.

## Methodology
- **Data Sources**: HMDA Loan Application Records, FRED economic data
- **Models**: Logistic regression (micro-level), Linear regression (macro-level)
- **Key Features**: Lagged unemployment, GDP growth, home price changes
- **Forecasting**: Quarter-ahead approval rate predictions

## Key Findings
- State unemployment rate is the strongest predictor (p < 0.01)
- 1% increase in unemployment decreases approval odds by X%
- Model accurately predicted 2023 Q4 approval downturn

## Usage
See notebooks in sequential order for full analysis.