# Healthcare R&D Spending Analysis
This project analyzes Research and Development (R&D) spending data for companies in the Health Care sector.

The python code for analysis is available in `main.py`.

To run execute:
```python 
python main.py
```

## Data Preprocessing and Cleaning
The data is loaded from an `xlsx` file in to a pandas dataframe. The data is relatively clean. The columns are normalized, including the values in the years column. Relevant columns are filtered and the data is ready for exploration.


## Analaysis
**Total R&D Spending By Company In Health Care Sector Over 4 Years**

This analysis focuses on visualizing the total R&D spending by individual companies in the Health Care sector over a 4-year period.

We use a treemap visualization to display the distribution of R&D spending among companies.

The main visualization is a treemap that provides insights into R&D spending trends within the Health Care sector.

Health Care vs. IT R&D Spending Comparison in Year 1
In this analysis, we compare R&D spending between the Health Care and Information Technology (IT) sectors for Year 1.
We perform a statistical t-test to determine if there is a significant difference in R&D spending distributions between these sectors.
Code and Visualization

The key visualization is a bar chart comparing mean R&D spending between the Health Care and IT sectors in Year 1.


Total R&D Spending Change Across Health Care Companies
This analysis focuses on understanding the aggregated yearly spending changes across Health Care companies.
We calculate spending changes, round off the values, and visualize the data to identify trends.
Code and Visualization

The primary visualization is a line chart showing the changes in R&D spending over the years.


Total R&D Spending By Company In Health Care Sector in 4 Years
In this analysis, we aim to visualize the total R&D spending by Health Care companies over a 4-year period.
We use a treemap to represent the distribution of spending among companies over these years.
Code and Visualization


The main visualization is a treemap that offers a comprehensive view of R&D spending trends over the 4-year period.
Usage
You can use the provided Python code to replicate these analyses with your own dataset.
Make sure to install the required libraries using pip install pandas matplotlib plotly scipy.

## Presentation
A presentation summarizing these analyses and their conclusions can be found in the slides folder.

## Conclusion
This project provides valuable insights into R&D spending patterns in the Health Care sector. It covers data preprocessing, visualization of spending trends, statistical comparisons, and treemap visualizations to help stakeholders make informed decisions regarding investments and resource allocation.
