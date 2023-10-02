import pandas as pd
from pandas import DataFrame
from os.path import abspath, dirname, join

base_path = dirname(__file__)
print(base_path)
data_path = join(base_path, "data/raw/companies.xlsx")
pd.set_option('display.max_columns', None)
pd.set_option("display.max_rows", None)

def normalize(df):
    df.columns = df.columns.str.strip().str.lower().str.replace(' ', '_').str.replace('(', '').str.replace(')', '').str.replace('.', '')
    return df


def main():
    df = pd.read_excel(data_path)
    df_cleaned = normalize(df)
    df_filtered = pd.DataFrame(df_cleaned, columns=['ticker_symbol', 'years', 'period_ending', 'research_and_development', 'gics_sector'])
    df_filtered = df_filtered[df_filtered['gics_sector'] == 'Health Care']
    print(df_filtered)
    print(df_filtered['period_ending'].drop_duplicates().sort_values())


if __name__ == "__main__":
    main()