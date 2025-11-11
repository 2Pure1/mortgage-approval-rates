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

## Project Structure
mortgage-approval-model/

├── data/ # Data directories

├── notebooks/ # Jupyter notebooks for analysis

├── src/ # Python source code

├── config/ # Configuration files

├── requirements.txt # Python dependencies

└── README.md # Project documentation


## Key Findings
- State unemployment rate is the strongest predictor (p < 0.01)
- 1% increase in unemployment decreases approval odds by X%
- Model accurately predicted 2023 Q4 approval downturn

## Usage
1. Install dependencies: `pip install -r requirements.txt`
2. Run notebooks in sequence:
   - `01_data_collection.ipynb`
   - `02_economic_data_cleaning.ipynb` 
   - `03_exploratory_analysis.ipynb`
   - `04_model_building.ipynb`
   - `05_forecasting.ipynb`

## Business Impact
This model helps lenders:
- Anticipate changes in mortgage approval rates
- Adjust underwriting standards based on economic forecasts
- Manage portfolio risk through scenario analysis
