# Vanguard Digital Experiment Analysis


## Table of Contents

1. [Project Brief](#project-brief)
2. [The Experiment Conducted](#the-experiment-conducted)
3. [Importing and Exploring Data](#importing-and-exploring-data)
4. [Data Sources](#data-sources)
5. [Data Preparation & Merging Datasets](#data-preparation-&-merging-datasets)
6. [Hypotheses](#hypotheses)
    - [Completion Rate Analysis](#completion-rate-analysis)
    - [Error Rates Analysis](#error-rates-analysis)
    - [Session Duration Analysis](#session-duration-analysis)
7. [Key Findings](#key-findings)
8. [Conclusion](#conclusion)

## Project Brief

This project involves analyzing the results of a digital experiment conducted by Vanguard Investment Management Group to determine if a new User Interface (UI) design improves client process completion rates.The goal is to determine if a new UI design leads to a better user experience and higher process completion rates.

## The Experiment Conducted

An A/B test was conducted from 3/15/2017 to 6/20/2017 with the following groups:
- **Control Group**: Clients interacted with the traditional online process.
- **Test Group**: Clients experienced the new UI design.

Both groups followed the same process sequence, including an initial page, three steps, and a confirmation page.

## Importing and Exploring Data

pandas numpy seaborn matplotlib.pyplot scipy.stats

## Installation

## Data Sources
We will use three datasets for this analysis:
Client Profiles ("data/df_final_demo.txt"): Contains demographics such as age, gender, and account details of Vanguard clients.
Digital Footprints ("data/df_final_web_data_pt_1.txt"), ("data/df_final_web_data_pt_2.txt"): Detailed trace of client interactions online, divided into two parts: pt_1 and pt_2. These need to be merged for comprehensive analysis.
Experiment Roster ("data/df_final_experiment_clients.txt"): Identifies which clients participated in the experiment and their group allocation (Control or Test).

## Data Preparation & Merging Datasets
Merge Digital Footprints: Combine pt_1 and pt_2 from the df_final_web_data dataset to form a complete view of client interactions.
Join Datasets: Integrate the merged digital footprints with the client profiles (df_final_demo) and the experiment roster (df_final_experiment_clients).

## Data Cleaning
Handle Missing Values: Identify and appropriately handle any missing values in the datasets.
Data Transformation: Ensure all data types are correct and any necessary transformations (e.g., date formats) are applied.
Outlier Detection: Detect and handle outliers that could skew the analysis.

## Hypotheses
Completion Rate Hypothesis: The new design (Test group) has a higher completion rate compared to the old design (Control group).
Cost-Effectiveness Hypothesis: The new design leads to a minimum increase of 5% in the completion rate, making it cost-effective.
Engagement Hypothesis: Clients using the new UI have longer session durations, indicating higher engagement.
Task Efficiency Hypothesis: Clients in the test group complete the process with fewer errors and retries compared to the control group.

## Key Findings
Performance Metrics
Completion Rate: Calculate the proportion of users who reach the final ‘confirm’ step for both groups.
Time Spent on Each Step: Determine the average duration users spend on each step.
Error Rates: Identify steps where users go back to a previous step, indicating confusion or errors.
