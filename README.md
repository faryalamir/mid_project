# Analysis of R&D Spending in Health Care and Information Technology Sectors
This repository contains Python code and data analysis for investigating Research and Development (R&D) spending in the Health Care and Information Technology (IT) sectors. The analysis explores trends in R&D spending, statistical comparisons between the two sectors, and visualizations to provide insights into the data.

Getting Started
## Prerequisites
Python 3.x
Jupyter Notebook (optional)
Required Python packages: pandas, scipy, matplotlib, plotly, numpy

## Installation
You can install the required packages using pip:
bash
Copy code
pip install pandas scipy matplotlib plotly numpy
Data
The analysis uses a dataset of company financials, specifically R&D spending, which is loaded from an Excel file named companies.xlsx. The dataset is cleaned and normalized to prepare it for analysis.

## Analysis
### Question 1: Analyze Health Care Sector R&D Spending Year-over-Year
The code filters the data for the Health Care sector, calculates yearly spending by companies, and plots the year-over-year R&D spending change.
The code calculates the aggregated yearly spending change across all companies in the Health Care sector.
It computes the percentage change (pct_change) in R&D spending year-over-year.
Any NaN values (resulting from the first year with no previous year for comparison) are filled with 0.
The change values are rounded to four decimal places and stored in the yearly_spending DataFrame
### Question 2: Comparing Health Care and IT Sectors in Year 1
This section filters data for both sectors in Year 1 and compares their mean, median, and standard deviation of R&D spending. It also creates histograms for both sectors to visualize the distribution.
### Question 3: Total R&D Spending by Company in Health Care Sector
The code groups the data by company ticker symbols and calculates the total R&D spending for each company in the Health Care sector. It then visualizes the results using a treemap.
### Question 4: Health Care R&D Spendings Over Years
This section focuses on R&D spending trends in the Health Care sector. It creates a boxplot to visualize the distribution of R&D spending over the years.
### Question 5: Statistical Hypothesis Test
A t-test is performed to compare the R&D spending distribution between Health Care and IT companies in Year 1. The results are visualized using a bar chart, and the t-statistic and p-value are printed.

## Usage
Clone this repository to your local machine.
Make sure you have the required packages installed.
Run the Jupyter Notebook or Python script to execute the analysis.

## Acknowledgments
The dataset used in this analysis is hypothetical and is provided for demonstration purposes only.

This analysis is a simplified example and can be extended and customized for more complex real-world datasets.
