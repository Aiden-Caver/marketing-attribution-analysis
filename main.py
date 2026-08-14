import pandas as pd
from pathlib import Path
from src.analysis import clean_campaigns, clean_signups, clean_purchases


BASE_DIR = Path(__file__).resolve().parent
campaigns = pd.read_csv(BASE_DIR / "data" / "campaigns.csv")
signups = pd.read_csv(BASE_DIR / "data" / "signups.csv")
purchases = pd.read_csv(BASE_DIR / "data" / "purchases.csv")


# Create copies of the original dataframes to preserve the raw data
camp_clean = campaigns.copy()
purch_clean = purchases.copy()
sign_clean = signups.copy()

# Clean the dataframes using the cleaning functions from analysis.py
camp_clean = clean_campaigns(camp_clean)
sign_clean = clean_signups(sign_clean)
purch_clean = clean_purchases(purch_clean)

print(f"Campaigns: {campaigns.shape[0]} -> {camp_clean.shape[0]} rows")
print(f"Signups: {signups.shape[0]} -> {sign_clean.shape[0]} rows")
print(f"Purchases: {purchases.shape[0]} -> {purch_clean.shape[0]} rows")