# Caylee Chan
# Created 23 May 2026
# Updated 23 May 2026

## Modules
import pandas as pd
import geopandas as gpd
import numpy as np

## Read in elections data
all_elections = pd.read_csv('./data/elections/countypres_2000-2024.csv')

# Initial data summaries
print(f'rows: {all_elections.shape[0]}')
print(f'col names & data types: \n{all_elections.dtypes}') 
print(f'years: {sorted(all_elections['year'].unique())}')
print(f'states: {all_elections['state'].unique()}')

## Data validation
# Check for NAs in candidatevotes - only an issue in 37 New Mexico counties
print(sum(all_elections['candidatevotes'].isna()))
print(all_elections[all_elections['candidatevotes'].isna()])

# Unique Florida counties number
raw_fl = all_elections[all_elections['state'] == 'FLORIDA']
print(f'unique fl counties in raw data: {raw_fl['county_name'].nunique()}')

## Select party winner for each unique county and election year for Florida
fl_elections = raw_fl.loc[raw_fl.groupby(['year', 'county_fips'])['candidatevotes'].idxmax()].reset_index(drop = True)
print(fl_elections.head())
print(f'fl rows: {fl_elections.shape[0]}')
print(f'fl col names & data types: \n{fl_elections.dtypes}')
print(f'fl years: {sorted(fl_elections['year'].unique())}')
print(f'fl unique counties: {fl_elections['county_name'].nunique()}')

#### NOTE: multiple states have the same county names!! calculating winners for entire us using county_name will cause issues - use fips!!!

