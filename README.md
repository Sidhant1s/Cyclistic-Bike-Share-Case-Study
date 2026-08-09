# Cyclistic-Bike-Share-Case-Study


An end-to-end data analytics portfolio project analyzing historical trip data to uncover behavioral differences between casual riders and annual members, complete with Python automation, Tableau data visualizations, and strategic conversion recommendations aimed at converting casual riders into annual members.

---

## 📋 Table of Contents

1. [Project Overview & Business Problem]
2. [Data Processing & Preparation Phase]
3. [Process & Automation Phase (Python)]
4. [Analysis & Visualization Phase (Tableau)]
5. [presentation ]
6. [Changelog]
7. [License]

---

## 1. Project Overview & Business Problem

* **Business Task**: Analyze historical trip data for Cyclistic (a fictional bike-share company based in Chicago) to understand how annual members and casual riders use bikes differently.
* **Goal**: Provide data-driven insights to help the marketing team design targeted campaigns aimed at converting casual riders into annual members.
* **Key Stakeholders**: Cyclistic executive team, marketing analytics department, and marketing campaign managers.

---

## 2. Data Processing & Preparation Phase

* **Data Source & Organization**: Downloaded historical monthly trip data provided by Motivate International Inc. under an open data license[cite: 3]. Files were organized year-by-year within a local project directory.
* **Data Safety & Integrity**: Created isolated duplicate copies of raw directories to ensure data integrity and safeguard original records before any manipulation[cite: 3]. Verified column structures, checked for null values, and validated schemas.
* **Data Scope & Exclusions**:
* Older historical datasets were excluded due to inconsistencies.
* Specific monthly files (`202406-divvy-tripdata`, `2025divvy-tripdata`, and `2026-divvy-tripdata`) along with files missing mandatory date values were dropped because they lacked complete timestamps required for duration calculations.



---

## 3. Process & Automation Phase (Python)

* **Tool Selection**: Microsoft Excel encountered performance and memory constraints when handling millions of multi-month trip rows. Python (`pandas` and `glob`) was utilized to programmatically process and combine the data.
* **Data Transformation**:
* Calculated `ride_length` by subtracting the start time column from the end time column (`d2-c2`).
* Derived `day_of_week` values using the weekly index formula (`weekofday(c2,1)`), noting that 1 represents Sunday and 7 represents Saturday.
* Optimized the dataset by dropping non-essential station and coordinate columns (`start_station_name`, `end_station_name`, `end_station_id`, `start_lng`, `end_lat`, `end_lng`) that fell outside the scope of user-behavior analysis.


* **Merging**: Programmatically merged all valid monthly CSV files into a single master dataset.

---

## 4. Analysis & Visualization Phase (Tableau)

* **Analytical Platform**: Bypassed traditional SQL database setups by importing the merged master CSV directly into Tableau Public as a flat text file.
* **Data Transformation & Metric Correction**:
* Implemented a custom calculated field—`ABS(DATEDIFF('minute', [Started At], [Ended At]))`—to resolve negative numeric rendering outputs and enforce absolute positive trip durations across all visual aggregations.


* **Visualizations**: Generated clear visual charts comparing average trip durations and weekly volume trends between member and casual user groups.

---

## 5. Key Findings & Strategic Insights

* Usage Parity: Total ride volumes and usage levels between casual riders and annual members are relatively close, showing that the gap between the two groups is not excessively large, and casual riders frequently match or exceed member activity levels in specific areas.
* Behavioral Split: Casual riders represent a highly active market segment with significant trip durations and heavy weekend activity peaks, whereas annual members maintain consistent commuting patterns throughout the week.
* Solution Statement: Offer discounted pricing or lower the price for annual memberships to increase the conversion rate of casual riders into members.
* Further Recommendations**: Conduct expanded customer surveys to capture deeper qualitative insights and more precise user preferences for future decision-making.

---

## 6. Changelog

*  Project Inception & Data Gathering**: Downloaded raw historical monthly trip data and established secure local backup copies.
*  Scoping & Data Filtering**: Excluded legacy datasets and incomplete timestamp files (`202406`, `2025`, `2026`, and date-missing entries).
*  Data Transformation**: Calculated `ride_length` and `day_of_week`, while dropping unused location columns.
*  Python Automation**: Executed script using `pandas` and `glob` to merge monthly files into a single master dataset.
* Tableau Integration**: Imported master CSV into Tableau and applied the absolute duration calculation to fix rendering anomalies.
*  Strategic Synthesis**: Formulated final conversion recommendations and finalized portfolio documentation.

---

## 7. License

This project is licensed under the terms of the **MIT License**.
