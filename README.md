# Marketing Attribution Analysis
A mock project working with marketing data to clean and merge three data sets, then derive meaningful insights to support future business decisions.

## How to Run
``` bash
pip install -r requirements.txt
```

## Skills Practiced
- Counted number of date inconsistencies by using `coerce` to mark broken dates with `NaT` to then be counted by using `.isna().sum()`.
- Copied the original csv files with `.copy()` to preserve the raw data.
- Created functions to clean each csv file to be called in `main.py`, then used the functions to clean the datasets before merging them.


## Data Cleaning Decisions
- Not assigning a format for `pd.to_datetime` caused the `.isna().sum()` to mark valid dates as `NaT` if they didn't match its inferred format since I used `errors = 'coerce'`. I used `format = 'mixed'` to consistently format all dates the same, while also handling all `NaT` values. While this resolved the per-row inference across three diferent date formats, it carries a risk on formats like DD/MM vs MM/DD that can't be resolved from the string alone.
- Dropped rows from `signups.csv` that reference campaigns not listed in `campaigns.csv`, since these include data that shouldn't exist in this scenario.

## Lessions Learned
- Cleaning an merge logic were committed directly to `main` before catching that a feature branch was never created; corrected workflow for remaining tasks.

## Sample Output


## Files
