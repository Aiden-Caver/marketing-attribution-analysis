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

print(f"Campaigns: {campaigns.shape} -> {camp_clean.shape} cleaned")
print(f"Signups: {signups.shape} -> {sign_clean.shape} cleaned")
print(f"Purchases: {purchases.shape} -> {purch_clean.shape} cleaned")

# Merge the cleaned dataframes
def merge_campaign_data (camp_clean, sign_clean, purch_clean):
    '''Function to merge cleaned campaigns with signups using left join, then merge purchases also with left join.'''
    merged_df1 = pd.merge(camp_clean, sign_clean, on='campaign_id', how='left') # Merge campaigns and signups on campaign_id with left join
    print(f"Merged DataFrame shape after merging campaigns and signups: {merged_df1.shape}")
    merged_df = pd.merge(merged_df1, purch_clean, on='customer_id', how='left') # Merge the result with purchases on customer_id with left join
    return merged_df

print(f"Merged DataFrame shape: {merge_campaign_data(camp_clean, sign_clean, purch_clean).shape}")