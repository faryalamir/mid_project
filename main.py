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
    # Sort by ticker symbol and years early on
    df_filtered = df_filtered.sort_values(["ticker_symbol", "years"], ascending=True)
    print(df_filtered.dtypes)
    # Aggregated yearly spending change across the companies
    yearly_spending = (
        df_filtered.groupby("years")["research_and_development"].sum(numeric_only=True).reset_index()
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


def q2(df: DataFrame) -> None:
    # Filter specific columns
    df_l = pd.DataFrame(df, columns=['ticker_symbol', 'years', 'period_ending', 'research_and_development', 'gics_sector'])

    # Get data for healthcare and IT sectors for year 1
    healthcare_df = df_l[(df_l['gics_sector'] == 'Health Care') & (df_l['years'] == 1)]
    it_df = df_l[(df_l['gics_sector'] == 'Information Technology') & (df_l['years'] == 1)]

    print(healthcare_df.head())
    print(it_df.head())

    mean_hc, mean_it = round(healthcare_df["research_and_development"].mean()), round(it_df["research_and_development"].mean())
    median_hc, median_it = round(healthcare_df["research_and_development"].median()), round(it_df["research_and_development"].median())
    std_hc, std_it = round(healthcare_df["research_and_development"].std()), round(it_df["research_and_development"].std())

    print(f"Health Care Mean {mean_hc} Median {median_hc} Std {std_hc}")
    print(f"IT Mean {mean_it} Median {median_it} Std {std_it}")

    fig, ax = plt.subplots(2, 1, figsize=(12, 10))

    # Plot histogram for the IT sector
    ax[0].hist(it_df['research_and_development'], bins=30, alpha=0.5)
    ax[0].ticklabel_format(axis='x', scilimits=[0, 0])
    ax[0].set_xlabel('Annual R&D Expenses')
    ax[0].set_ylabel('Frequency')
    ax[0].set_title('IT Sector R&D Expenses in Year 1')

    # Plot histogram for the healthcare sector
    ax[1].hist(healthcare_df['research_and_development'], bins=30, alpha=0.5)
    ax[1].ticklabel_format(axis='x', scilimits=[0, 0])
    ax[1].set_xlabel('Annual R&D Expenses')
    ax[1].set_ylabel('Frequency')
    ax[1].set_title('Healthcare Sector R&D Expenses in Year 1')

    plt.tight_layout()
    plt.show()

def main():
    # Load data
    df = pd.read_excel(data_path, engine="openpyxl")

    # Normalize and clean data
    df_cleaned = normalize_column_names(df)
    df_cleaned["years"] = df_cleaned["years"].replace("Year ", "", regex=True)
    df_cleaned["years"] = df_cleaned["years"].astype("int")

    # Display data samples and types
    print(df_cleaned.head())
    print(df_cleaned.dtypes)

    # Question 1
    # q1(df_cleaned)

    # Question 2
    q2(df_cleaned)


if __name__ == "__main__":
    main()
