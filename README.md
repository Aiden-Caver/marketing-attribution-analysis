# Marketing Attribution Analysis
A mock project working with marketing data to clean and merge three data sets, then use the merged data to calculate cost-per-signup and total revenue for each campaign.

## How to Run
``` bash
pip install -r requirements.txt
```

## Skills Practiced
- Audited three messy datasets for duplicates, formatting inconsistencies, and referential integrity.
- Reasoned through join-type selections across a three-table merge chain, deciding which table's rows should be preserved and using the corresponding merge type.
- Utilized `groupby()` aggregation to build a campaign-level summary using row-level data from different dataframes. 
- Handled a divide-by-zero scenario using `np.where()` to instruct on how potential zeros should be handled.
- Counted number of date inconsistencies by using `coerce` to mark broken dates with `NaT` to then be counted by using `.isna().sum()`.
- Copied the original csv files with `.copy()` to keep the raw data unaltered.
- Created functions to clean each csv file to be called in `main.py`, then used the functions to clean the datasets before merging them.


## Data Cleaning Decisions
- Not assigning a format for `pd.to_datetime` caused the `.isna().sum()` to mark valid dates as `NaT` if they didn't match its inferred format since I used `errors = 'coerce'`. I used `format = 'mixed'` to consistently format all dates the same, while also handling all `NaT` values. While this resolved the per-row inference across three diferent date formats, it carries a risk on formats like DD/MM vs MM/DD that can't be resolved from the string alone.
- Created the cleaning functions to address formatting issues only (duplicates, casing, whitespace, and dates), while handling referential integrity issues (orphaned signups and purchases) separately during merge/aggregation. The implementation remained somewhat fragile, relying on explicit `.isin()` filtering in `signup_counts` and merge-order side effects elsewhere in `merged`.

## Known Limitations
- The second merge (campaigns+signups -> purchases) used a left join to preserve all signups, including the ones that never made a purchase. An inner join dropped 13 non-converting signups, which were still meaningful for cost-per-signup calculations.
- The `np.where` function was included to handle campaigns with zero signups. Since every campaign in `campaigns.csv` had at least one signup, I had to create a theoretical fourth campaign with zero signups to ensure this function worked as intended.

## Process Notes
- Verified that campaign-level calulations remain accurate even if a customer signs up for multiple campaigns, since `groupby('campaign_id')` counts each signup towards its own campaign rather than needing to split credit between campaigns.
- Verified no customer had multiple purchases before finalizing the merge logic using `.duplicated().sum()`. If a customer made several purchases, the merge would've created duplicate rows for that customer, falsely inflating the signup counts used in the cost-per-signup calculation.
- Cleaning and merge logic were committed directly to `main` before catching that a feature branch was never created; corrected workflow for remaining tasks.

## Sample Output
```
  campaign_id  revenue  signup_count  spend  cost_per_signup
0      CMP001   601.47            10   5000           500.00
1      CMP002  1760.42            15   3500           233.33
2      CMP003  1051.40            11   6200           563.64
```

## Files
- `data` - A folder containing three mock data files, one that lists the three campaigns, one for customer signups, and one for customer purchases.
- `analysis.py` - Creates three functions designed to clean each of the three mock csv files, using actions like `drop_duplicates()`, `str.lower()`, `str.strip()`, and a `to_datetime` that converts date errors to `NaT`.
- `main.py` - Contains the main code that imports the csv files, creates copies of them to keep the raw data unaltered, cleans the files by calling the functions from `analysis.py`, creating a function that merges the data sets, and create a separate campaign table that shows each campaign, its revenue, signup count, spending, and cost-per-signup.