import pandas as pd


# Data Cleaning, create functions to clean each dataframe
def clean_campaigns(camp_clean):
    '''Function to clean campaigns dataframe. Removes duplicate rows and normalizes channel column to lowercase while removing whitespace.'''
    camp_clean = camp_clean.drop_duplicates() # Remove duplicate rows
    camp_clean['channel'] = camp_clean['channel'].str.lower().str.strip() # Normalize channel column to lowercase and remove whitespace
    return camp_clean


def clean_signups(sign_clean):
    '''Function to clean signups dataframe. Removes duplicate rows, converts signup_date to datetime using `mixed` format, and removes extra spaces from customer_id.'''
    sign_clean = sign_clean.drop_duplicates() # remove duplicate rows
    sign_clean['signup_date'] = pd.to_datetime(sign_clean['signup_date'], format = 'mixed', errors='coerce') # convert signup_date to datetime, coerce errors to NaT
    sign_clean['customer_id'] = sign_clean['customer_id'].str.strip() # remove extra spaces from customer_id
    return sign_clean


def clean_purchases(purch_clean):
    '''Function to clean purchases dataframe. Removes duplicate rows, converts purchase_date to datetime using `mixed` format, and removes extra spaces from customer_id.'''
    purch_clean = purch_clean.drop_duplicates() # remove duplicate rows
    purch_clean['purchase_date'] = pd.to_datetime(purch_clean['purchase_date'], format = 'mixed', errors='coerce') # convert purchase_date to datetime, coerce errors to NaT
    purch_clean['customer_id'] = purch_clean['customer_id'].str.strip() # remove extra spaces from customer_id
    return purch_clean
