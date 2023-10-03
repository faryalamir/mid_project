import pandas as pd
from pandas import DataFrame
from os.path import dirname, join
import matplotlib.pyplot as plt

data_path = join(dirname(__file__), "data/raw/companies.xlsx")
pd.set_option("display.max_columns", None)
pd.set_option("display.max_rows", None)


def normalize_column_names(df: DataFrame) -> DataFrame:
    df.columns = (
        df.columns.str.strip()
        .str.lower()
        .str.replace(" ", "_")
        .str.replace("(", "")
        .str.replace(")", "")
        .str.replace(".", "")
    )
    return df


def q1(df: DataFrame) -> None:
    # Create a new dataframe with filtered columns
    df_filtered = pd.DataFrame(
        df,
        columns=[
            "ticker_symbol",
            "years",
            "period_ending",
            "research_and_development",
            "gics_sector",
        ],
    )
    # Make sure we only have the health care sector companies
    df_filtered = df_filtered.loc[df_filtered["gics_sector"] == "Health Care"]
    # Sort by ticket symbol and years early on
    df_filtered = df_filtered.sort_values(["ticker_symbol", "years"], ascending=True)
    print(df_filtered.dtypes)
    # Aggregated yearly spending change across the companies
    yearly_spending = (
        df_filtered.groupby("years")["research_and_development"].sum().reset_index()
    )
    # Calculate percentage change across years
    yearly_spending["spending_change"] = yearly_spending[
        "research_and_development"
    ].pct_change()
    # Fix NaN in the first year record as the pct_change needs a previous record to calculate change and there is none
    yearly_spending = yearly_spending.fillna(0)
    # Round off change
    yearly_spending["spending_change"] = yearly_spending["spending_change"].round(4)
    # Show records of the data
    print(yearly_spending)
    # Plotting YoY R&D spending change in the health sector
    plt.figure(figsize=(10, 6))
    plt.plot(
        yearly_spending["years"],
        yearly_spending["spending_change"],
        marker="o",
        linestyle="-",
    )
    plt.xlabel("Year")
    plt.ylabel("Spending Change")
    plt.grid(True)
    plt.show()


def main():
    # Load data
    df = pd.read_excel(data_path, engine="openpyxl")
    # Normalize data
    df_cleaned = normalize_column_names(df)
    # Clean years
    df_cleaned["years"] = df_cleaned["years"].replace("Year ", "", regex=True)
    df_cleaned["years"] = df_cleaned["years"].astype("int")

    print(df_cleaned.head())
    print(df_cleaned.dtypes)

    # Question 1
    q1(df_cleaned)


if __name__ == "__main__":
    main()
