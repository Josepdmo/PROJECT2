import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from statsmodels.stats.proportion import proportions_ztest
from scipy import stats
from scipy.stats import ttest_ind, chi2_contingency

# Function to import dataframe
def import_dataframe(file_path):
    df = pd.read_csv(file_path)
    return df


def analyze_completion_rates(variation_df):
    """
    This function calculates the completion rates for each group, performs a z-test to compare the completion rates
    between the control and test groups, and plots the results.

    Parameters:
    variation_df (pd.DataFrame): The DataFrame containing the process steps and variation labels.

    Returns:
    pd.DataFrame: A DataFrame containing the completion data and the z-test results.
    """
    # Total number of sessions for each group
    total_sessions = variation_df.groupby('Variation')['visit_id'].nunique().reset_index(name='total_sessions')

    # Filter the data to only include rows where process_step is "confirm"
    confirm_steps = variation_df[variation_df['process_step'] == 'confirm']

    # Count the number of sessions that reached the "confirm" step for each group
    confirm_sessions = confirm_steps.groupby('Variation')['visit_id'].nunique().reset_index(name='confirm_sessions')

    # Merge total sessions with confirm sessions
    completion_data = pd.merge(total_sessions, confirm_sessions, on='Variation')

    # Calculate the completion rate
    completion_data['completion_rate'] = (completion_data['confirm_sessions'] / completion_data['total_sessions']) * 100

    # Extract data for z-test
    control_successes = completion_data[completion_data['Variation'] == 'Control']['confirm_sessions'].values[0]
    control_total = completion_data[completion_data['Variation'] == 'Control']['total_sessions'].values[0]

    test_successes = completion_data[completion_data['Variation'] == 'Test']['confirm_sessions'].values[0]
    test_total = completion_data[completion_data['Variation'] == 'Test']['total_sessions'].values[0]

    # Perform z-test for proportions
    count = [control_successes, test_successes]
    nobs = [control_total, test_total]

    z_stat, p_value = proportions_ztest(count, nobs)

    # Check if the difference is statistically significant
    alpha = 0.05
    is_significant = p_value < alpha

    # Print results
    st.write(f"Z-Statistic: {z_stat}")
    st.write(f"P-Value: {p_value}")
    st.write(f"Is the difference in completion rates statistically significant at alpha = {alpha}? {'Yes' if is_significant else 'No'}")

    # Create a bar chart
    fig, ax = plt.subplots(figsize=(5, 3))
    sns.barplot(x='Variation', y='completion_rate', data=completion_data, palette='Set1', ax=ax)
    ax.set_title('Completion Rate by Variation')
    ax.set_xlabel('Variation')
    ax.set_ylabel('Completion Rate (%)')
    ax.set_ylim(0, 100)
    st.pyplot(fig)

    return completion_data, z_stat, p_value

def analyze_session_durations_by_step(variation_df):
    """
    This function analyzes the session durations by step for both control and test groups,
    performs t-tests to compare the durations, and plots the results.

    Parameters:
    variation_df (pd.DataFrame): The DataFrame containing the process steps and variation labels.

    Returns:
    pd.DataFrame: A DataFrame containing the t-test results for each process step.
    """
    # Calculate average time spent on each step for the Control group
    time_spent_summary_control = variation_df[variation_df['Variation'] == 'Control'].groupby('process_step')['time_spent'].mean().reset_index()
    time_spent_summary_control['Variation'] = 'Control'
    st.write("Average Time Spent on Each Step (Control Group):")
    st.write(time_spent_summary_control)
    
    # Calculate average time spent on each step for the Test group
    time_spent_summary_test = variation_df[variation_df['Variation'] == 'Test'].groupby('process_step')['time_spent'].mean().reset_index()
    time_spent_summary_test['Variation'] = 'Test'
    st.write("Average Time Spent on Each Step (Test Group):")
    st.write(time_spent_summary_test)
    
    # Combine both dataframes
    combined_df = pd.concat([time_spent_summary_control, time_spent_summary_test])

    # Order the process steps correctly
    step_order = ['start', 'step_1', 'step_2', 'step_3', 'confirm']
    combined_df['process_step'] = pd.Categorical(combined_df['process_step'], categories=step_order, ordered=True)
    combined_df = combined_df.sort_values('process_step').reset_index(drop=True)
    st.write("Combined DataFrame:")
    st.write(combined_df)
    
    # Plotting
    fig, ax = plt.subplots(figsize=(12, 6))
    
    # Create separate palettes for control and test groups
    palette = {'Control': 'skyblue', 'Test': 'red'}
    
    # Create a bar plot using Seaborn
    sns.barplot(x='process_step', y='time_spent', hue='Variation', data=combined_df, palette=palette, ax=ax)
    
    # Set plot title and labels
    ax.set_title('Average Duration Spent on Each Step by Group (in seconds)')
    ax.set_xlabel('Process Step')
    ax.set_ylabel('Average Duration (seconds)')
    
    # Show plot
    st.pyplot(fig)
    
    # Initialize list to store results
    results = []
    
    # Perform t-test for each process step
    for step in step_order:
        control_times = variation_df[(variation_df['Variation'] == 'Control') & (variation_df['process_step'] == step)]['time_spent']
        test_times = variation_df[(variation_df['Variation'] == 'Test') & (variation_df['process_step'] == step)]['time_spent']
        
        if not control_times.empty and not test_times.empty:
            t_stat, p_value = ttest_ind(control_times, test_times, equal_var=False)
            results.append({
                'process_step': step,
                'control_mean': control_times.mean(),
                'test_mean': test_times.mean(),
                't_stat': t_stat,
                'p_value': p_value
            })
        else:
            results.append({
                'process_step': step,
                'control_mean': control_times.mean() if not control_times.empty else None,
                'test_mean': test_times.mean() if not test_times.empty else None,
                't_stat': None,
                'p_value': None
            })
    
    # Convert results to DataFrame
    ttest_results_df = pd.DataFrame(results)
    
    # Display the t-test results
    st.write("T-test Results for Each Process Step:")
    st.write(ttest_results_df)
    
    return ttest_results_df



def analyze_error_rates(df):
    df = df.sort_values(by=['client_id', 'visit_id', 'date_time'])
    step_mapping = { 'start': 0, 'step_1': 1, 'step_2': 2, 'step_3': 3, 'confirm': 4 }
    df['step_index'] = df['process_step'].map(step_mapping)
    df['prev_step_index'] = df.groupby('visit_id')['step_index'].shift(1)
    df['is_back_track'] = df['prev_step_index'] > df['step_index']
    error_rates = df.groupby('Variation')['is_back_track'].mean().reset_index(name='Error Rate')

    fig, ax = plt.subplots(figsize=(10, 6))
    sns.barplot(x='Variation', y='Error Rate', data=error_rates, palette=['skyblue', 'red'], ax=ax)
    ax.set_title('Error Rates for Control and Test Groups')
    ax.set_xlabel('Group')
    ax.set_ylabel('Error Rate')
    st.pyplot(fig)

    contingency_table = pd.crosstab(df['Variation'], df['is_back_track'])
    chi2, p, dof, ex = chi2_contingency(contingency_table)
    st.write(f"Chi-Square Test:\nChi2: {chi2}\np-value: {p}")

    return error_rates, chi2, p

# Main Streamlit app
def main():
    st.title("Vanguard A/B Testing Results")

    # Directly import dataframe using a file path
    df = import_dataframe('variation.csv')
    st.write(df.head())

    # Analyze completion rates
    st.header("Analyze Completion Rates")
    completion_data, z_stat, p_value = analyze_completion_rates(df)
    st.write(completion_data)

    # Analyze session durations by step
    st.header("Analyze Session Durations by Step")
    analyze_session_durations_by_step(df)

    # Analyze error rates
    st.header("Analyze Error Rates")
    error_rates, chi2, p = analyze_error_rates(df)
    st.write(error_rates)

if __name__ == "__main__":
    main()