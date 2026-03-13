AirFly Insights ✈️

Project Overview

AirFly Insights is a data analysis project that explores airline flight operations, delays, and traffic patterns using flight data. The project aims to uncover insights about airline performance, busiest routes, and the major causes of flight delays.



Dataset

The dataset contains historical flight data including airlines, departure times, routes, and delay information.

Dataset Link from kaggle:
(https://www.kaggle.com/datasets/raminhuseyn/airlines-delay)


Tools and Technologies

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Jupyter Notebook


Project Structure

AirFly-Insights
│
├── notebooks
│   ├── Milestone-1_analysis.ipynb
│   └── Milestone-2_updated_visual.ipynb
│
├── src
│   └── data_processing.py
│
├── README.md
├── requirements.txt
└── .gitignore


Week 3: Univariate and Bivariate Analysis

Several visualizations were created to explore flight activity and trends.

Top Airlines

Bar charts were used to identify airlines operating the highest number of flights.

Busiest Routes

The most common origin–destination routes were identified using route frequency analysis.

Busiest Months

A line chart was used to analyze seasonal flight trends across different months.

Flight Distribution by Departure Hour

Hourly flight distribution charts were used to identify peak airport activity periods.

Airline Delay Comparison

Boxplots were used to compare delay distributions across different airlines.


Week 4: Delay Cause Analysis

Multiple visualizations were used to analyze different causes of flight delays.

Delay Causes

Operational issues such as crew availability or aircraft preparation can cause airline delays.

Weather Delays

Weather conditions such as storms or fog can disrupt flight schedules.

NAS Delays

National Airspace System delays occur due to congestion in the air traffic system.

Airport Congestion

Airport infrastructure limitations and high traffic can cause delays.


Key Insights

- Carrier delays contribute significantly to total delay minutes.
- Weather delays occur less frequently but can cause severe disruptions.
- NAS delays indicate congestion in the air traffic system.
- Some airlines consistently show higher average delay times compared to others.




AirFly Insights – Milestone 3

Overview

Milestone 3 focuses on analyzing airline operational patterns including routes, airport traffic, cancellations, and delays. The goal is to identify important trends affecting airline performance and visualize them using a Streamlit dashboard.

Route Analysis

Top Routes

1.Identified the most frequent flight routes.
2.High-frequency routes represent major airline travel corridors.

Visualization

1.Bar chart showing top routes by flight count.

Insight

1.Some routes experience significantly higher traffic compared to others.

Airport Traffic Analysis

Busiest Airports

1.Analyzed airports with the highest number of flight departures.

Visualization

1.Bar chart showing airports with the highest flight volume.

Insight

1.Major airports handle large volumes of flights and act as aviation hubs.

Cancellation Analysis

Flight Cancellation Reasons

1.Flights may be cancelled due to operational or environmental factors.

Visualization

1.Pie chart showing distribution of cancellation reasons.

Cancellation Codes

A – Carrier
B – Weather
C – NAS (National Airspace System)
D – Security

Insight

1.Carrier and weather-related issues are common causes of cancellations.

Delay Cause Analysis

Average Delay by Cause

Analyzes the average delay minutes caused by different operational factors.

Delay Types

1.Carrier Delay
2.Weather Delay
NAS Delay
3.Security Delay
4.Late Aircraft Delay

Visualization

1.Bar chart showing average delay by cause.

Insight

1.Carrier and late aircraft delays contribute significantly to overall delays.

Seasonal Delay Analysis

Average Arrival Delay by Season

Examines how flight delays vary across different seasons.

Visualization

1.Bar chart showing average arrival delay by season.

Insight

1.Certain seasons experience higher delays due to weather conditions and travel demand.

Flight Schedule Analysis

Flights by Departure Hour

Analyzes how flight departures are distributed throughout the day.

Visualization

1.Line chart showing number of flights by departure hour.

Insight

1.Flight departures peak during morning and evening travel periods.



Streamlit Dashboard

An interactive Streamlit dashboard was created to visualize airline operational insights.

Dashboard Sections

--Dataset preview
--Route analysis
--Airport traffic analysis
--Cancellation analysis
--Delay cause analysis
--Seasonal delay trends
--Flight schedule analysis
--Key insights summary

Each visualization includes:

--Clear titles
--Axis labels
--Short explanations


Key Insights

--Major airports handle high volumes of flight traffic.
--Certain routes experience significantly higher demand.
--Carrier delays contribute heavily to total delays.
--Seasonal patterns affect delay trends.
--Flight departures peak during specific hours of the day.

Deliverables

Milestone 3 includes:

--Route and airport traffic analysis
--Cancellation and delay insights
--Seasonal delay analysis
--Interactive Streamlit dashboard
--GitHub repository with analysis code and visualizations


Author
Fouziya