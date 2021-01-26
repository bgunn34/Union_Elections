import pandas as pd 
import numpy as np 
import os 

def fetch_year_data(path, year):
    path = path + '/' + year
    print(year)
    lead_df = pd.read_csv(path + f'/ar_disbursements_emp_off_data_{year}.txt',sep='|')
    unions_df = pd.read_csv(path + f'/lm_data_data_{year}.txt',sep='|')

    unions_df_columns = [
    'UNION_NAME',
    'UNIT_NAME',
    'F_NUM',
    'AFF_ABBR',
    'NEXT_ELECTION',
    'FORM_TYPE',
    'RPT_ID'
    ]
    lead_df_columns = [
        'FIRST_NAME',
        'MIDDLE_NAME',
        'LAST_NAME',
        'TITLE',
        'RPT_ID',
    ]
    lead_df = lead_df.loc[:,lead_df_columns]
    unions_df = unions_df.loc[:,unions_df_columns]
    
    out_df = pd.merge(
    lead_df,
    unions_df,
    how='left',
    on='RPT_ID'
    )
    out_df['YEAR'] = year
    out_df = out_df.dropna(subset=['FIRST_NAME'])

    return out_df


def check_change(df):
    out_series = []
    df['YEAR'] = df['YEAR'].astype('Int')
    for row in df.itertuples():
        pass
    return out_series


def main():
    path = os.getcwd() + '/data/MainArchive'
    print(path)
    years = os.listdir(path)
    out_df = []
    for year in years:
        if year == '.DS_Store':
            continue
        else:
            df = fetch_year_data(path, year)
            out_df.append(df)

    out_df = pd.concat(out_df)
    print(out_df.dtypes)
    # out_df.to_csv('raw_data.csv')

    out_df['CHANGE'] = check_change(out_df)


if __name__ == '__main__':
    main()