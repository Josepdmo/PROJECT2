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

### 1. Completion Rate Hypothesis

**H0**: The completion rate of the new design (Test group) is equal to or lower than the old design (Control group).
**H1**: The completion rate of the new design (Test group) is higher than the old design (Control group).

**Results**:
- Control group completion rate: 49.84%
- Test group completion rate: 58.52%
- The Z-Statistic is -22.89, and the P-Value is extremely small (5.39e-116), which is much less than the alpha level of 0.05.
  
**Interpretation**:
- Since the P-Value is significantly lower than 0.05, we reject the null hypothesis (H0) and accept the alternative hypothesis (H1).
- Conclusion: The completion rate of the new design (Test group) is statistically significantly higher than that of the old design (Control group).

### 2. Cost-Effectiveness Hypothesis

**H0**: The new design does not lead to a minimum increase of 5% in the completion rate.
**H1**: The new design leads to a minimum increase of 5% in the completion rate.

**Results**:
- Control group completion rate: 49.84%
- Test group completion rate: 58.52%

**Interpretation**:
The increase in completion rate is approximately 8.68% ((58.52 - 49.84) / 49.84 * 100), which exceeds the 5% threshold. However, without a p-value or confidence interval, we can't confirm the statistical significance of this increase.

### 3. Engagement Hypothesis

**H0**: The session durations of clients using the new UI are equal to or shorter than those using the old UI.
**H1**: The session durations of clients using the new UI are longer than those using the old UI.

**Results** (average session duration in seconds):
| Step    | Control Avg Duration (s) | Test Avg Duration (s) | t-statistic | p-value   |
|---------|--------------------------|-----------------------|-------------|-----------|
| Start   | 78,598.63                | 65,390.81             | -4.35       | 0.999993  |
| Step 1  | 38,631.85                | 28,503.09             | -4.06       | 0.999975  |
| Step 2  | 18,786.24                | 12,545.78             | -3.43       | 0.999694  |
| Step 3  | 38,168.53                | 20,870.51             | -6.23       | 1.000000  |
| Confirm | 250,213.99               | 266,014.22            | 1.00        | 0.157563  |

**Interpretation**:
- For steps "start", "step_1", "step_2", and "step_3", the new UI resulted in significantly shorter session durations compared to the old UI, supporting the null hypothesis (H0).
- For the "confirm" step, there was no significant difference in session durations between the new and old UIs.
- Overall, the new UI appears to be more efficient, reducing session durations for most steps.

### 4. Task Efficiency Hypothesis

**H0**: Clients in the test group complete the process with the same or higher error rates and retries compared to the control group.
**H1**: Clients in the test group complete the process with fewer errors and retries compared to the control group.

**Results**:
- Control group error rate: 6.77%
- Test group error rate: 9.19%
- Chi-Square Test: Chi2 = 625.11, p-value < 0.05

**Interpretation**:
The higher error rate in the Test group suggests the new UI leads to more user errors. The Chi-Square test shows a very small p-value, indicating the difference in error rates is statistically significant. Therefore, we reject the null hypothesis, confirming the Test group has higher error rates, suggesting that the new UI is less efficient.

### Summary of Results

1. **Completion Rate Hypothesis**: The Test group has a higher completion rate, but further statistical testing is needed to confirm significance.
2. **Cost-Effectiveness Hypothesis**: The increase in completion rate is above 5%, suggesting cost-effectiveness, but statistical significance is not confirmed.
3. **Engagement Hypothesis**: The Test group has shorter session durations, indicating no increase in engagement. The t-test confirms this result is not statistically significant.
4. **Task Efficiency Hypothesis**: The Test group has a higher error rate, and the Chi-Square test confirms this is statistically significant, suggesting the new UI design is less efficient.

### Additional Hypothesis (Session Duration T-Test)

**H0**: There is no significant difference in session durations between the Test and Control groups.
**H1**: There is a significant difference in session durations between the Test and Control groups.

**Results**:
- t-statistic: -1.121
- p-value: 0.262

**Interpretation**:
With a p-value of 0.262, which is greater than 0.05, we fail to reject the null hypothesis. There is no significant difference in session durations between the Test and Control groups.
