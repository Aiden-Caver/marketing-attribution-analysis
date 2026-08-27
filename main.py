import pandas as pd
import numpy as np
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

# Merge the cleaned dataframes
def merge_campaign_data (camp_clean, sign_clean, purch_clean, type='inner'):
    '''Function to merge cleaned campaigns with signups using left join, then merge purchases also with left join.'''
    merged_df1 = pd.merge(camp_clean, sign_clean, on='campaign_id', how=type) # Merge campaigns and signups on campaign_id with left join
    # print(f"Merged DataFrame shape after merging campaigns and signups: {merged_df1.shape}")
    merged_df = pd.merge(merged_df1, purch_clean, on='customer_id', how=type) # Merge the result with purchases on customer_id with left join
    return merged_df

merged = merge_campaign_data(camp_clean, sign_clean, purch_clean, type='left')

sign_clean_valid = sign_clean[sign_clean['campaign_id'].isin(camp_clean['campaign_id'])]
signup_counts = sign_clean_valid.groupby('campaign_id')['customer_id'].count().rename('signup_count').reset_index()
campaign_revenue = merged.groupby('campaign_id')['purchase_amount'].sum().rename('revenue').reset_index()
campaign_spend = camp_clean[['campaign_id', 'spend']]

campaign_merge = pd.merge(campaign_revenue, signup_counts, on='campaign_id', how='left')
campaign_table = pd.merge(campaign_merge, campaign_spend, on='campaign_id', how='left')

campaign_table['cost_per_signup'] = np.where(campaign_table['signup_count'] == 0, np.nan, campaign_table['spend'] / campaign_table['signup_count'])

pd.options.display.float_format = '{:.2f}'.format
print(campaign_table)