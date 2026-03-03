FINAL VERSION-MILESTONE-1 SUBMISSION

✈️ AirFly Insights – Milestone 1

📌 Project Statement
The objective of this project is to analyze large-scale airline flight data to
 uncover operational trends, delay patterns, and cancellation 
 behavior using data analysis and visualization techniques.

The goal is to understand airline and airport performance and generate actionable insights using
 structured preprocessing and feature engineering.

🎯 Expected Outcomes

Preprocess and clean aviation dataset

Identify delay and cancellation patterns

Prepare dataset for visualization and advanced analysis

Build foundation for trend analysis and stakeholder insights

📂 Dataset

Source: Kaggle – Airlines Flights Data (2018 subset used)
## Dataset
The dataset is not included in this repository due to size limitations.
It can be downloaded from:(https://www.kaggle.com/datasets/sherrytp/airline-delay-analysis)

The dataset contains flight-level operational details including:

Flight Date

Airline Carrier

Origin & Destination Airports

Scheduled & Actual Times

Departure & Arrival Delays

Cancellation Status

Distance

Taxi Times

🗂 Milestone 1: Data Foundation and Cleaning

🔹 Week 1: Project Initialization and Dataset Setup

✔ Defined Goals & KPIs

Focused on:

Delay trends

Cancellation rate

Route-level patterns

Airline performance

✔ Loaded Dataset

Used pandas to load the CSV file.

✔ Explored Dataset

Performed:

df.shape → checked number of rows and columns

df.info() → inspected datatypes and null values

df.isnull().sum() → identified missing values

df.describe() → reviewed statistical summary

✔ Selected Relevant Columns

Reduced dataset from 28 columns to 16 required columns for analysis.

✔ Checked Duplicates

Verified that no duplicate rows exist.

✔ Sampling

Created a 20% sample for faster experimentation and testing.

✔ Memory Optimization

Converted categorical columns to category

Converted float columns to float32

Reduced overall memory usage

🔹 Week 2: Preprocessing and Feature Engineering

✔ Handled Missing Values

Delay columns had null values.

Used median instead of mean due to skewed delay distribution.

Removed highly null column CANCELLATION_CODE.

Filtered cancelled flights when analyzing delay performance.

✔ Datetime Formatting

Converted FL_DATE to datetime format to enable time-based analysis.

✔ Feature Engineering

Created new derived features:

MONTH → extracted from flight date

DAY_OF_WEEK → numeric weekday

DAY_NAME → weekday name

DEP_HOUR → extracted from scheduled departure time

ROUTE → combined ORIGIN and DEST

These features help analyze:

Seasonal trends

Weekly patterns

Hourly delay trends

Route-level performance

✔ Saved Processed Dataset

Saved cleaned dataset to:

Data/Processed/flights_2018_processed.csv

This allows faster reuse without repeating preprocessing steps.

📦 Deliverables
1️⃣ Cleaned Dataset

Optimized

Null-handled

Feature engineered

Ready for analysis

2️⃣ Summary of Preprocessing Logic

Column selection

Null handling using median

Duplicate validation

Datetime formatting

Feature creation

Memory optimization

3️⃣ Feature Dictionary

| Feature Name      | Description |
|-------------------|------------|
| FL_DATE           | Flight date |
| OP_CARRIER        | Airline carrier code |
| ORIGIN            | Departure airport |
| DEST              | Arrival airport |
| CRS_DEP_TIME      | Scheduled departure time |
| DEP_TIME          | Actual departure time |
| DEP_DELAY         | Departure delay (minutes) |
| ARR_TIME          | Actual arrival time |
| ARR_DELAY         | Arrival delay (minutes) |
| CANCELLED         | Cancellation flag (0 = No, 1 = Yes) |
| DISTANCE          | Flight distance |
| TAXI_IN           | Taxi-in time (minutes) |
| TAXI_OUT          | Taxi-out time (minutes) |
| MONTH             | Extracted month |
| DAY_OF_WEEK       | Numeric weekday |
| DAY_NAME          | Weekday name |
| DEP_HOUR          | Scheduled departure hour |
| ROUTE             | Origin-Destination combination |



Milestone 2 visualisation analysis....

Overview

In Milestone 2, a detailed visual analysis was performed on the processed flight dataset (January 2018). The objective was to explore delay patterns, airline performance, operational factors, and time-based trends using univariate and bivariate analysis techniques.

Note: The dataset contains flights from January only; therefore, seasonal comparison across months was not performed.


🔍 Univariate Analysis

The following single-variable analyses were performed:

Distribution of Arrival Delays (Histogram)

Boxplot of Arrival Delays (Outlier Detection)

Flight Distribution by Departure Hour

Key Observations:

Most flights experience small delays.

Delay distribution is right-skewed with extreme outliers.

Flight departures peak during morning hours and remain steady during daytime.


🔄 Bivariate Analysis

The following relationship-based analyses were conducted:

Average Arrival Delay by Airline

Taxi-Out Time vs Departure Delay (Scatter Plot)

Key Observations:

Airline performance varies significantly in terms of average delay.

Taxi-out time shows a weak relationship with departure delay, indicating that congestion may contribute to delays but is not the only factor.

Operational efficiency appears to differ across carriers.

Week 4 – Delay Analysis
Overview

In this section, delay patterns were analyzed using arrival delay (ARR_DELAY) and departure delay (DEP_DELAY) data. Since the dataset contains only January data, the analysis focuses on operational and airline-based delay patterns rather than full seasonal comparison.

1. Arrival Delay Distribution

A histogram and boxplot were used to understand the distribution of arrival delays.

Most flights have small or moderate delays.

The distribution is right-skewed.

There are several extreme outliers with very high delay values.

This indicates that while most flights are near schedule, a small number experience significant delays.

2. Average Arrival Delay by Airline

A bar chart was used to compare average arrival delays across different airlines.

Some airlines show higher average delays compared to others.

A few airlines maintain relatively low average delays.

This suggests operational efficiency varies between carriers.

3. Average Arrival Delay by Departure Hour

A line plot was used to analyze delay trends across departure hours.

Delays vary depending on departure time.

Certain hours show higher average delays.

This suggests time-of-day congestion may impact flight punctuality


Tools Used

Python
Pandas
Matplotlib
Seaborn
Jupyter Notebook