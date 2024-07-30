Vanguard Investment Management Company

Introduction
The aim is to determine if a new, modern User Interface (UI) and in-context prompts improve the client experience and increase process completion rates.

Data Sources
We will use three datasets for this analysis:
Client Profiles (df_final_demo): Contains demographics such as age, gender, and account details of Vanguard clients.
Digital Footprints (df_final_web_data): Detailed trace of client interactions online, divided into two parts: pt_1 and pt_2. These need to be merged for comprehensive analysis.
Experiment Roster (df_final_experiment_clients): Identifies which clients participated in the experiment and their group allocation (Control or Test).

Installation
To begin, ensure you have the necessary software and libraries installed. This project will primarily use Python and relevant libraries for data analysis, such as pandas, numpy, scipy, and matplotlib. Additionally, Tableau will be used for data visualization.

Required Libraries
pip install pandas numpy scipy matplotlib seaborn

Data Preparation
Merging Datasets
Merge Digital Footprints: Combine pt_1 and pt_2 from the df_final_web_data dataset to form a complete view of client interactions.
Join Datasets: Integrate the merged digital footprints with the client profiles (df_final_demo) and the experiment roster (df_final_experiment_clients).

Data Cleaning
Handle Missing Values: Identify and appropriately handle any missing values in the datasets.
Data Transformation: Ensure all data types are correct and any necessary transformations (e.g., date formats) are applied.
Outlier Detection: Detect and handle outliers that could skew the analysis.

Hypotheses
Completion Rate Hypothesis: The new design (Test group) has a higher completion rate compared to the old design (Control group).
Cost-Effectiveness Hypothesis: The new design leads to a minimum increase of 5% in the completion rate, making it cost-effective.
Engagement Hypothesis: Clients using the new UI have longer session durations, indicating higher engagement.
Task Efficiency Hypothesis: Clients in the test group complete the process with fewer errors and retries compared to the control group.

Results
Performance Metrics
Completion Rate: Calculate the proportion of users who reach the final ‘confirm’ step for both groups.
Time Spent on Each Step: Determine the average duration users spend on each step.
Error Rates: Identify steps where users go back to a previous step, indicating confusion or errors.
