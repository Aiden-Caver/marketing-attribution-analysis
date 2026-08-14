Cleaning Findings:
File: campaigns.csv
Issue: 1 exact duplicate row (CMP001 appears twice)
Check used: campaigns.duplicated().sum()

File: campaigns.csv
Issue: Inconsistent capitalization/whitespace in `channel` column
Values: 'Facebook', 'facebook ' (trailing space) treated as 2 distinct channels
Check used: campaigns['channel'].unique()

File: signups.csv
Issue: 2 exact duplicate rows
Check used: signups.duplicated().sum()

File: signups.csv
Issue: 2 rows reference a campaign_id that doesn't exist in campaigns.csv
Values: C1036 -> CMP999, C1037 -> CMP998
Check used: signups[~signups['campaign_id'].isin(campaigns['campaign_id'])]

File: signups.csv
Issue: 1 row has leading/trailing whitespace in customer_id
Check used: (signups['customer_id'] != signups['customer_id'].str.strip()).sum()

File: signups.csv
Issue: 24 of 40 rows fail to parse with naive pd.to_datetime() due to 3 mixed date formats (ISO, MM/DD/YYYY, D-Mon-YYYY) — fixed via format='mixed'
Check used: pd.to_datetime(signups['signup_date'], errors='coerce').isna().sum()

File: purchases.csv
Issue: 1 exact duplicate row
Check used: purchases.duplicated().sum()

File: purchases.csv
Issue: 2 rows reference a customer_id that doesn't exist in signups.csv (purchased without ever signing up)
Values: C2050 ($89.99), C2051 ($45.50)
Check used: purchases[~purchases['customer_id'].isin(signups['customer_id'].str.strip())]

File: purchases.csv
Issue: 18 of 25 rows fail to parse with naive pd.to_datetime() due to same 3 mixed date formats — fixed via format='mixed'
Check used: pd.to_datetime(purchases['purchase_date'], errors='coerce').isna().sum()

