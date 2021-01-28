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
    out_df.columns = out_df.columns.str.strip()
    out_df = out_df.dropna(subset=['FIRST_NAME','LAST_NAME','F_NUM','TITLE'])
    out_df = out_df.loc[out_df['LAST_NAME'] != ' ']

    return out_df


def check_change(df):
    df.sort_values('YEAR').reset_index()
    df['CHANGE'] = 0

    change_df = df.drop_duplicates(subset=['FIRST_NAME','LAST_NAME','F_NUM','TITLE'])
    change_df = change_df.loc[change_df['YEAR'] != 2000]
    
    df.loc[df.index.isin(change_df.index),'CHANGE'] = 1

    return df



def main():
    path = os.getcwd() + '/data/MainArchive'
    years = os.listdir(path)
    out_df = []
    for year in years:
        if year == '.DS_Store':
            continue
        else:
            df = fetch_year_data(path, year)
            out_df.append(df)
    out_df = pd.concat(out_df, ignore_index=True)

    out_df['YEAR'] = out_df['YEAR'].astype('int')
    out_df = out_df.sort_values('LAST_NAME')
    out_df = check_change(out_df)
    out_df.to_csv('raw_data.csv')


if __name__ == '__main__':
    main()