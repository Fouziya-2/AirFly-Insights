
AirFly Insights: Data Visualization and Analysis of Airline Operations

Project Overview

AirFly Insights is a data analysis project focused on understanding airline operations using historical flight data. The goal is to explore flight delays, cancellation patterns, airline performance, and operational trends through data preprocessing and visual analytics.
This project uses flight-level data to uncover insights related to delay causes, busiest airlines and routes, and operational inefficiencies. The analysis is performed using Python with libraries such as Pandas, Matplotlib, and Seaborn.
you can download the dataset from kaggle:

Milestone 1: Data Foundation and Cleaning
Objective
Prepare the airline dataset for analysis by cleaning the data, handling missing values, optimizing data types, and creating useful derived features.

Step 1: Data Acquisition
The dataset was obtained from airline operational records containing information about flights, delays, cancellation reasons, and airport operations.

The dataset includes key fields such as:
Flight Date
Airline Carrier
Origin and Destination Airports
Departure and Arrival Delays
Cancellation Status
Delay Causes (Carrier, Weather, NAS, Security, Late Aircraft etc..)

Step 2: Data Exploration
The dataset was initially explored to understand its structure and contents.
The following checks were performed:
Dataset size and structure using 'df.shape'
Column types using 'df.info()'
Summary statistics using 'df.describe()'
Missing values using 'df.isnull().sum()'
This helped identify which columns required cleaning or transformation.

Step 3: Handling Missing Values
Several columns contained missing values due to operational conditions.
Delay Columns

Delay-related columns such as:
Carrier Delay
Weather Delay
NAS Delay
Security Delay
Late Aircraft Delay.....
were filled with 0 because missing values indicate that no delay occurred for that specific reason.
Cancellation Columns
The CANCELLATION_CODE column contained missing values for flights that were not cancelled. These values were replaced with
 "Not Cancelled" to maintain consistency.
Taxi and Air Time

Columns such as:
Taxi Out
Taxi In
Air Time
contained null values when flights were cancelled. These values were replaced with 0.

Step 4: Data Type Optimization
Data types were optimized to reduce memory usage and improve processing efficiency.

Examples include:
Converting categorical columns such as airline carriers and airports to category
Converting numeric columns to smaller integer types
Converting the flight date column to datetime format like etc...

Step 5: Feature Engineering
Additional features were created to support advanced analysis.
New features include:
Route
Combines origin and destination airports.
'Example: ATL - LAX'
Departure Hour
Extracted from departure time to analyze hourly traffic.

Date Features Derived from the flight date:
Year
Month
Day
Day of Week
Season Flights were categorized into seasons (Winter, Spring, Summer, Fall) based on month values.

Step 6: Saving Processed Data
After cleaning and feature engineering, the processed dataset was saved for reuse in analysis and visualization.
This improves performance and avoids repeating preprocessing steps.



Milestone 2: Visual Exploration and Delay Trends

Objective
Analyze airline operations through visualizations to understand delay patterns, flight distribution, and operational trends.

Week 3: Univariate and Bivariate Analysis
Several visualizations were created to explore flight activity and delay behavior.

Top Airlines:
Bar charts were used to identify airlines operating the highest number of flights.

Busiest Routes:
The most common origin-destination routes were identified using route frequency analysis.

Busiest Months:
A line chart was used to analyze seasonal flight trends across different months.
Flight Distribution by Day
Flights were analyzed based on the day of the week to observe weekly patterns.
Flight Distribution by Departure Hour
Hourly flight distributions were analyzed to identify peak airport activity periods.
Delay Distribution
Histogram plots were used to understand the spread and frequency of arrival delays.
Airline Delay Comparison
Boxplots were used to compare delay distributions across different airlines.

Week 4: Delay Cause Analysis
Delay causes were analyzed using multiple visualizations to understand operational challenges.
Carrier Delays
These delays occur due to airline-related operational issues such as crew availability or aircraft preparation.
Weather Delays
Weather conditions such as storms or fog can disrupt flight schedules and cause delays.
NAS Delays
National Airspace System delays occur due to air traffic control congestion or airport infrastructure limitations.

Delay Cause Comparison
Pir chart for checking the cancelled and non cancelled flights and reason for cancellation
Bar charts were used to compare the average delay minutes caused by:
Carrier operations
Weather conditions
Airspace congestion
Delay Trends by Time of Day
Average delays were analyzed across different departure hours to observe congestion patterns during peak travel times.
Airport Delay Analysis
Airports with the highest average delays were identified using aggregated delay statistics.

Key Insights
Carrier delays contribute significantly to total delay minutes, indicating operational inefficiencies.
NAS delays are also a major contributor, highlighting congestion in the air traffic system.
Weather delays occur less frequently but can cause severe disruptions when they occur.
Certain airlines consistently show higher average delay times compared to others.
Tools and Libraries


The project was implemented using:
Python
Pandas
NumPy
Matplotlib
Seaborn
Jupyter Notebook