# Vanguard Digital Experiment Analysis


## Table of Contents

1. [Project Brief](#project-brief)
2. [The Experiment Conducted](#the-experiment-conducted)
3. [Importing and Exploring Data](#importing-and-exploring-data)
4. [Data Sources](#data-sources)
5. [Data Preparation & Merging Datasets](#data-preparation-&-merging-datasets)
6. [Hypotheses](#hypotheses)
    - [Completion Rate Hypothesis](#completion-rate-hypothesis)
    - [Cost-Effectiveness Hypothesis](#cost-effectiveness-hypothesis)
    - [Engagement Hypothesis](#engagement-hypothesis)
    - [Task Efficiency Hypothesis](#task-efficiency-hypothesis)
7. [Conclusion](#conclusion)
8. [Presentation](#presentation)
9. [Connect With Us](#connect-with-us)

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
- Client Profiles ("data/df_final_demo.txt"): Contains demographics such as age, gender, and account details of Vanguard clients.
- Digital Footprints ("data/df_final_web_data_pt_1.txt"), ("data/df_final_web_data_pt_2.txt"): Detailed trace of client interactions online, divided into two parts: pt_1 and pt_2. These need to be merged for comprehensive analysis.
- Experiment Roster ("data/df_final_experiment_clients.txt"): Identifies which clients participated in the experiment and their group allocation (Control or Test).

## Data Preparation & Merging Datasets
- Merge Digital Footprints: Combine pt_1 and pt_2 from the df_final_web_data dataset to form a complete view of client interactions.
- Join Datasets: Integrate the merged digital footprints with the client profiles (df_final_demo) and the experiment roster (df_final_experiment_clients).
- Univariate Analysis and Visualisation: Understand the demographics and perform statistical analysis on each variable.

## Data Cleaning
1) Dropping Null Values: Identify and appropriately drop any missing values in the datasets.
3) Outlier Detection: Detect and handle outliers that could skew the analysis.

### 1. Completion Rate Hypothesis

**H0**: The completion rate of the new design (Test group) is equal to or lower than the old design (Control group).
**H1**: The completion rate of the new design (Test group) is higher than the old design (Control group).

**Results**:
- Control group completion rate: 49.84%
- Test group completion rate: 58.52%
- The Z-Statistic is -22.89, and the p-value is extremely small (5.39e-116), which is much less than the alpha level of 0.05.

![Completion Rate](https://github.com/Josepdmo/PROJECT2/blob/main/Images/Completion%20Rate.png)
  
**Interpretation**:
- Since the p-value is significantly lower than 0.05, we reject the null hypothesis (H0) and accept the alternative hypothesis (H1).
- Conclusion: The completion rate of the new design (Test group) is statistically significantly higher than that of the old design (Control group).

### 2. Cost-Effectiveness Hypothesis

**H0**: The new design does not lead to a minimum increase of 5% in the completion rate.
**H1**: The new design leads to a minimum increase of 5% in the completion rate.

**Results**:
- Control group completion rate: 49.84%
- Test group completion rate: 58.52%
- Z-Statistic: 22.89
- P-Value : 0.0000

![Cost Effectiveness](https://github.com/Josepdmo/PROJECT2/blob/main/Images/Cost%20Effective%205%25%20Threshold.png)

**Interpretation**:
- The increase in completion rate is approximately 8.68% ((58.52 - 49.84) / 49.84 * 100), which exceeds the 5% threshold. 
- Based on the results of the z-test, we reject the null hypothesis, providing strong evidence that the new design leads to a completion rate increase confirming the new design's cost-effectiveness.

### 3. Engagement Hypothesis

**H0**: The session durations of clients using the new UI are equal to or shorter than those using the old UI.
**H1**: The session durations of clients using the new UI are longer than those using the old UI.

**Results** (average session duration in seconds):
| Step    | Control Avg Duration (s) | Test Avg Duration (s) | t-statistic | p-value      |
|---------|--------------------------|-----------------------|-------------|--------------|
| Start   | 54.335477                | 61.809148             | -4.25       | 2.060898e-05 |
| Step 1  | 42.568871                | 37.394860             | 6.74        | 1.496968e-11 |
| Step 2  | 38.524249                | 47.820970             | -13.24      | 5.650431e-40 |
| Step 3  | 92.515996                | 95.863682             | -3.073      | 2.117474e-03 |
| Confirm | 122.694765               | 111.959636            | 5.29        | 1.225098e-07 |


![Average Time Spent](https://github.com/Josepdmo/PROJECT2/blob/main/Images/Average%20Time%20-%20Engagement.png)

**Interpretation**:
- The new UI significantly increased session durations at the "Start" and "Step 2" stages,indicating reduced efficiency at these points.
- For "Step 1" and "Confirm", the new UI resulted in significantly shorter durations, suggesting improved efficiency in these stages.
- While the new UI shows potential benefits in "Step 1" and "Confirm", it also introduces inefficiencies in "Start" and "Step 2".
- Further refinement is needed to address the observed issues and enhance overall user experience.

### 4. Task Efficiency Hypothesis

**H0**: Clients in the test group complete the process with the same or higher error rates and retries compared to the control group.
**H1**: Clients in the test group complete the process with fewer errors and retries compared to the control group.

**Results**:
- Control group error rate: 6.77%
- Test group error rate: 9.19%
- Chi-Square Test: Chi2 = 625.11, p-value < 0.05

![Error Rates](https://github.com/Josepdmo/PROJECT2/blob/main/Images/Error%20Rates%20-Task%20Efficiency.png)

**Interpretation**:
The higher error rate in the Test group suggests the new UI leads to more user errors. The Chi-Square test shows a very small p-value, indicating the difference in error rates is statistically significant. Therefore, we reject the null hypothesis, confirming the Test group has higher error rates, suggesting that the new UI is less efficient.

## Conclusion

The decision on which website is better depends on the specific priorities of Vanguard Investment Management Group:

If higher completion rates are the primary goal, the new UI is better as it significantly improves this metric.
If minimizing user errors and ensuring a smooth process is more important, the traditional UI might be preferred due to its lower error rate.
If efficiency in terms of time spent is a key criterion, the new UI shows improvements in most steps but needs refinement in the final confirmation step.
To definitively conclude which website is better, further analysis and possibly iterative improvements to the new UI to reduce error rates would be necessary. Balancing these factors based on Vanguard's strategic goals will determine the best approach.

## Presentation 
https://www.canva.com/design/DAGMmaYZr6g/qpERRTuj69-TA0QzIWLXkA/view?utm_content=DAGMmaYZr6g&utm_campaign=designshare&utm_medium=link&utm_source=editor

## Connect With Us
Dalreen Soares- https://www.linkedin.com/in/dalreen-soares/
Lasma Oficiere
Josep de Marti
