
import functions_vanguard as vd
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import scipy.stats as stats
from matplotlib.ticker import ScalarFormatter
from matplotlib.ticker import FuncFormatter
from scipy.stats import chi2_contingency
from scipy.stats import ttest_ind
from statsmodels.stats.proportion import proportions_ztest


def import_dataframe():
    """
    This function imports a CSV file into a pandas DataFrame.

    Returns:
    pd.DataFrame: The imported DataFrame.
    """
    # File path
    file_path = "data/df_final_demo.txt"
    
    # Import the data
    df = pd.read_csv(file_path)
    
    return df

def analyze_dataframe(df):
    """
    This function performs various analyses and visualizations on the given DataFrame.
    
    Parameters:
    df (pd.DataFrame): The DataFrame to be analyzed.
    """
    # Display basic information about the dataset
    print(df.info())
    
    # Displaying information and visualizing 'clnt_tenure_yr'
    print(df['clnt_tenure_yr'].value_counts())
    plt.figure(figsize=(10, 6))
    sns.histplot(df['clnt_tenure_yr'], kde=True, bins=30, color="salmon")
    plt.title('Histogram of Client Tenure in Years')
    plt.xlabel('Client Tenure in Years')
    plt.ylabel('Frequency')
    plt.show()
    
    # Displaying information and visualizing 'clnt_age'
    print(df['clnt_age'].value_counts())
    plt.figure(figsize=(10, 6))
    sns.histplot(df['clnt_age'], kde=True, bins=30, color="salmon")
    plt.title('Histogram of Client Age')
    plt.xlabel('Client Age')
    plt.ylabel('Frequency')
    plt.show()
    
    # Displaying information and visualizing 'gendr'
    gender_counts = df['gendr'].value_counts()
    print(gender_counts)
    gender_counts.plot.pie(autopct='%1.1f%%', startangle=90, colors=sns.color_palette("Set2"))
    plt.title('Pie Chart of Gender Distribution')
    plt.ylabel('')  # Hide the y-label
    plt.show()
    
    # Displaying information and visualizing 'num_accts'
    num_accts_counts = df['num_accts'].value_counts()
    print(num_accts_counts)
    num_accts_counts.plot.pie(autopct='%1.1f%%', startangle=90, colors=sns.color_palette("Set2"))
    plt.title('Pie Chart of Number of Accounts')
    plt.ylabel('')  # Hide the y-label
    plt.show()
    
    num_accts_sorted = num_accts_counts.sort_index()
    plt.figure(figsize=(10, 6))
    plt.bar(num_accts_sorted.index, num_accts_sorted.values, color='salmon')
    plt.xlabel('Number of Accounts')
    plt.ylabel('Frequency')
    plt.title('Bar Chart of Number of Accounts')
    plt.show()
    
    # Displaying information about 'bal'
    print(df['bal'].value_counts())
    print(df['bal'].describe())
    
    # Displaying information and visualizing 'logons_6_mnth'
    print(df['logons_6_mnth'].value_counts())
    plt.figure(figsize=(10, 6))
    sns.histplot(df['logons_6_mnth'], bins=30, color="salmon")
    plt.title('Histogram of Logons in the Past 6 Months')
    plt.xlabel('Logons in the Past 6 Months')
    plt.ylabel('Frequency')
    plt.show()


def analyze_client_demographics(df):
    """
    This function analyzes the client demographics by adding new columns
    for total tenure in months, client status, and age group.

    Parameters:
    df (pd.DataFrame): The DataFrame to be analyzed.

    Returns:
    pd.DataFrame: The DataFrame with new columns for client demographics analysis.
    """
    # Calculate client tenure in months
    df['total_tenure_months'] = df['clnt_tenure_yr'] * 12 + df['clnt_tenure_mnth']

    # Display the first few rows to inspect the calculation
    print(df[['client_id', 'clnt_tenure_yr', 'clnt_tenure_mnth', 'total_tenure_months']].head())

    # Categorize clients as new or long-standing
    df['client_status'] = np.where(df['total_tenure_months'] <= 24, 'New', 'Long-standing')

    # Display the first few rows of the dataframe to inspect the new columns
    print(df[['client_id', 'client_status', 'total_tenure_months']].head())

    # Categorize clients as younger or older
    df['age_group'] = np.where(df['clnt_age'] <= df['clnt_age'].median(), 'Younger', 'Older')

    # Display the first few rows to inspect the new columns
    print(df[['client_id', 'clnt_age', 'age_group']].head())

    # Display the counts of the age group
    print(df["age_group"].value_counts())
    
    return df

def identify_primary_clients(df):
    """
    This function identifies the primary clients by their tenure and age group,
    and visualizes the distribution using a bar plot.

    Parameters:
    df (pd.DataFrame): The DataFrame to be analyzed.

    Returns:
    pd.DataFrame: The DataFrame containing the count of primary clients by tenure and age group.
    """
    # Primary clients' demographics
    primary_clients = df.groupby(['client_status', 'age_group']).size().reset_index(name='count')
    print("Primary Clients by Tenure and Age Group:")
    print(primary_clients)
    
    # Plotting
    plt.figure(figsize=(10, 6))
    sns.barplot(x='client_status', y='count', hue='age_group', data=primary_clients, palette='Set2')

    # Adding titles and labels
    plt.title('Distribution of Primary Clients by Tenure and Age Group')
    plt.xlabel('Client Status')
    plt.ylabel('Number of Clients')
    plt.legend(title='Age Group')
    plt.show()
    
    return primary_clients

def clean_dataframe(df):
    """
    This function cleans the DataFrame by removing rows with null values in specific columns
    and adjusting the data types of certain columns.

    Parameters:
    df (pd.DataFrame): The DataFrame to be cleaned.

    Returns:
    pd.DataFrame: The cleaned DataFrame.
    """
    # Display rows with null values in the 'bal' column
    null_rows = df[df["bal"].isnull()]
    print("Rows with null values in the 'bal' column:")
    print(null_rows)
    
    # Remove rows with null values in 'bal' and 'clnt_age' columns
    df.dropna(subset=["bal", "clnt_age"], inplace=True)
    
    # Display the data types of each column
    print("Data types before adjustment:")
    print(df.dtypes)
    
    # Display the data types of each column after adjustment
    print("Data types after adjustment:")
    print(df.dtypes)
    
    return df

def import_and_check_dataframe_part1():
    """
    This function imports a CSV file into a pandas DataFrame and checks for null values.

    Returns:
    pd.DataFrame: The imported DataFrame if no null values are found.
    """
    # File path
    file_path = "data/df_final_web_data_pt_1.txt"
    
    # Import the data
    df = pd.read_csv(file_path)
    
    # Check for null values
    null_counts = df.isna().sum()
    print("Null values in each column:")
    print(null_counts)
    
    # Return the DataFrame
    return df

def import_and_check_dataframe_part2():
    """
    This function imports a CSV file into a pandas DataFrame and checks for null values.

    Returns:
    pd.DataFrame: The imported DataFrame if no null values are found.
    """
    # File path
    file_path = "data/df_final_web_data_pt_2.txt"
    
    # Import the data
    df = pd.read_csv(file_path)
    
    # Check for null values
    null_counts = df.isna().sum()
    print("Null values in each column:")
    print(null_counts)
    
    # Return the DataFrame
    return df

def merge_dataframes(df1, df2):
    """
    This function merges two DataFrames and sorts them by 'client_id'.

    Parameters:
    df1 (pd.DataFrame): The first DataFrame to be merged.
    df2 (pd.DataFrame): The second DataFrame to be merged.

    Returns:
    pd.DataFrame: The merged and sorted DataFrame.
    """
    # Merge the DataFrames
    df = pd.concat([df1, df2], axis=0)
    
    # Sort the DataFrame by 'client_id'
    df.sort_values(by="client_id", ascending=True, inplace=True)
    
    return df

def import_and_analyze_experiment_clients():
    """
    This function imports a CSV file into a pandas DataFrame, determines the size of each group,
    and checks for null values in the DataFrame.

    Returns:
    pd.DataFrame: The imported DataFrame.
    """
    # File path
    file_path = "data/df_final_experiment_clients.txt"
    
    # Import the data
    df = pd.read_csv(file_path)
    
    # Determine the size of each group
    variation = df.groupby("Variation").size()
    print("Size of each group:")
    print(variation)
    
    # Check for null values
    null_counts = df.isna().sum()
    print("Null values in each column:")
    print(null_counts)
    
    return df


def merge_and_clean_dataframes(df_final_demo, df_merged, df_final_experiment_clients):
    """
    This function merges multiple data frames and drops rows with null values in the 'Variation' column.

    Parameters:
    df_final_demo (pd.DataFrame): The first DataFrame to be merged.
    df_merged (pd.DataFrame): The second DataFrame to be merged.
    df_final_experiment_clients (pd.DataFrame): The third DataFrame to be merged.

    Returns:
    pd.DataFrame: The merged and cleaned DataFrame.
    """
    # Merge the data frames
    new_df = pd.merge(df_final_demo, df_merged, how="left", on="client_id")
    
    # Merge with the experiment clients data frame
    variation_df = pd.merge(new_df, df_final_experiment_clients, on="client_id", how="inner")
    
    # Reset index and drop rows with null values in 'Variation' column
    variation_df.reset_index(drop=True, inplace=True)
    variation_df.dropna(subset=["Variation"], inplace=True)

    # Adjust the data type of 'client_id' to string
    variation_df["client_id"] = variation_df["client_id"].astype(str)
    
    return variation_df

def analyze_control_group(variation_df):
    """
    This function extracts the control DataFrame from the merged DataFrame, analyzes its demographics,
    and plots a histogram of age and a pie chart of gender distribution.

    Parameters:
    variation_df (pd.DataFrame): The DataFrame to be analyzed.

    Returns:
    pd.DataFrame: The control DataFrame.
    """
    # Extract control DataFrame
    control_df = variation_df[variation_df["Variation"] == "Control"]
    
    # Plotting the histogram of the 'clnt_age' column
    plt.figure(figsize=(10, 6))
    plt.hist(control_df['clnt_age'], bins=15, edgecolor='black')
    plt.title('Histogram of Age (Control Group)')
    plt.xlabel('Age')
    plt.ylabel('Frequency')
    plt.show()

    # Plotting the gender distribution pie chart
    gender_counts = control_df['gendr'].value_counts()
    plt.figure(figsize=(8, 8))
    plt.pie(gender_counts, labels=gender_counts.index, autopct='%1.1f%%', startangle=140)
    plt.title('Gender Distribution (Control group)')
    plt.show()
    
    return control_df

def analyze_test_group(variation_df):
    """
    This function extracts the test DataFrame from the merged DataFrame, analyzes its demographics,
    and plots a histogram of age and a pie chart of gender distribution.

    Parameters:
    variation_df (pd.DataFrame): The DataFrame to be analyzed.

    Returns:
    pd.DataFrame: The test DataFrame.
    """
    # Extract test DataFrame
    test_df = variation_df[variation_df["Variation"] == "Test"]
    
    # Plotting the histogram of the 'clnt_age' column for test group
    plt.figure(figsize=(10, 6))
    plt.hist(test_df['clnt_age'], bins=15, edgecolor='black')
    plt.title('Histogram of Age (Test Group)')
    plt.xlabel('Age')
    plt.ylabel('Frequency')
    plt.show()

    # Plotting the gender distribution pie chart for test group
    gender_counts_test = test_df['gendr'].value_counts()
    plt.figure(figsize=(8, 8))
    plt.pie(gender_counts_test, labels=gender_counts_test.index, autopct='%1.1f%%', startangle=140)
    plt.title('Gender Distribution (Test Group)')
    plt.show()
    
    return test_df
    

def analyze_test_group(variation_df):
    """
    This function extracts the test DataFrame from the merged DataFrame, analyzes its demographics,
    and plots a histogram of age and a pie chart of gender distribution.

    Parameters:
    variation_df (pd.DataFrame): The DataFrame to be analyzed.

    Returns:
    pd.DataFrame: The test DataFrame.
    """
    # Extract test DataFrame
    test_df = variation_df[variation_df["Variation"] == "Test"]
    
    # Plotting the histogram of the 'clnt_age' column for test group
    plt.figure(figsize=(10, 6))
    plt.hist(test_df['clnt_age'], bins=15, edgecolor='black')
    plt.title('Histogram of Age (Test Group)')
    plt.xlabel('Age')
    plt.ylabel('Frequency')
    plt.show()

    # Plotting the gender distribution pie chart for test group
    gender_counts_test = test_df['gendr'].value_counts()
    plt.figure(figsize=(8, 8))
    plt.pie(gender_counts_test, labels=gender_counts_test.index, autopct='%1.1f%%', startangle=140)
    plt.title('Gender Distribution (Test Group)')
    plt.show()
    
    return test_df

def compare_age_distributions(control_df, test_df):
    """
    This function plots histograms of age data from control and test groups on the same graph.

    Parameters:
    control_df (pd.DataFrame): The control DataFrame.
    test_df (pd.DataFrame): The test DataFrame.
    """
    plt.figure(figsize=(10, 6))
    plt.hist(control_df['clnt_age'], bins=15, edgecolor='black', alpha=0.5, label='Age (Control Group)', color='blue')
    plt.hist(test_df['clnt_age'], bins=15, edgecolor='black', alpha=0.5, label='Age (Test Group)', color='orange')
    plt.title('Histogram of Age Data from Control and Test Groups')
    plt.xlabel('Age')
    plt.ylabel('Frequency')
    plt.legend()
    plt.show()

def analyze_time_spent(variation_df):
    """
    This function analyzes the time spent on each step in the process, calculates the average time spent on each step,
    and plots the results.

    Parameters:
    variation_df (pd.DataFrame): The DataFrame containing the process steps and timestamps.

    Returns:
    tuple: A tuple containing the modified DataFrame with the 'time_spent' column and a summary DataFrame with the average time spent on each step.
    """
    # Convert date_time to datetime format
    variation_df['date_time'] = pd.to_datetime(variation_df['date_time'])
    
    # Sort by visit_id and date_time
    variation_df = variation_df.sort_values(by=['visit_id', 'date_time'])
    
    # Calculate time spent on each step
    variation_df['time_spent'] = variation_df.groupby('visit_id')['date_time'].diff().dt.total_seconds()
    
    # Fill NaN values in time_spent with 0 for the first step
    variation_df['time_spent'] = variation_df['time_spent'].fillna(0)
    
    # Calculate average time spent on each step
    time_spent_summary = variation_df.groupby('process_step')['time_spent'].mean().reset_index()
    print("Average Time Spent on Each Step:")
    print(time_spent_summary)
    
    # Plotting the average time spent on each step
    plt.figure(figsize=(10, 6))
    sns.barplot(x='process_step', y='time_spent', data=time_spent_summary, palette='viridis')
    
    # Adding titles and labels
    plt.title('Average Time Spent on Each Step')
    plt.xlabel('Process Step')
    plt.ylabel('Average Time Spent (seconds)')
    plt.xticks(rotation=45)
    plt.show()
    
    return variation_df, time_spent_summary

def analyze_session_durations(variation_df):
    """
    This function calculates session durations for each visit_id, performs a t-test to compare control and test groups,
    and interprets the results.

    Parameters:
    variation_df (pd.DataFrame): The DataFrame containing the process steps and timestamps.

    Returns:
    tuple: A tuple containing the t-statistic and p-value of the t-test.
    """
    # Calculate session duration for each visit_id
    session_durations = variation_df.groupby('visit_id')['time_spent'].sum().reset_index()

    # Merge with the original data to get the Variation labels
    df_merged = session_durations.merge(variation_df[['visit_id', 'Variation']].drop_duplicates(), on='visit_id')

    # Separate the data into control and test groups
    control_group = df_merged[df_merged['Variation'] == 'Control']['time_spent']
    test_group = df_merged[df_merged['Variation'] == 'Test']['time_spent']

    # Perform t-test
    t_stat, p_value = ttest_ind(test_group, control_group, alternative='greater')

    # Output the results
    print(f"T-statistic: {t_stat}")
    print(f"P-value: {p_value}")

    # Interpretation
    alpha = 0.05
    if p_value < alpha:
        print("Reject the null hypothesis. Clients using the new UI have significantly longer session durations.")
    else:
        print("Fail to reject the null hypothesis. There is no significant difference in session durations.")

    return t_stat, p_value

def calculate_completion_rate(variation_df):
    """
    This function calculates the total number of sessions and the number of sessions that reached the "confirm" step
    for each group, then calculates the completion rate for each group.

    Parameters:
    variation_df (pd.DataFrame): The DataFrame containing the process steps and variation labels.

    Returns:
    pd.DataFrame: A DataFrame containing the total sessions, confirm sessions, and completion rate for each group.
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

    print(completion_data)
    
    return completion_data

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
    print(f"Z-Statistic: {z_stat}")
    print(f"P-Value: {p_value}")
    print(f"Is the difference in completion rates statistically significant at alpha = {alpha}? {'Yes' if is_significant else 'No'}")

    # Create a bar chart
    plt.figure(figsize=(5, 3))
    sns.barplot(x='Variation', y='completion_rate', data=completion_data, palette='Set1')
    plt.title('Completion Rate by Variation')
    plt.xlabel('Variation')
    plt.ylabel('Completion Rate (%)')
    plt.ylim(0, 100)
    plt.show()

    return completion_data, z_stat, p_value

def analyze_cost_effectiveness(variation_df, completion_data, threshold=5.0):
    """
    This function analyzes the cost-effectiveness hypothesis by testing whether the new design leads to a minimum
    increase of 5% in the completion rate, making it cost-effective.

    Parameters:
    variation_df (pd.DataFrame): The DataFrame containing the process steps and variation labels.
    completion_data (pd.DataFrame): The DataFrame containing completion data for each variation.
    threshold (float): The threshold for the minimum increase in completion rate (default is 5%).

    Returns:
    None
    """
    # Filter for clients that have the 'Test' variation
    test_clients = variation_df[variation_df['Variation'] == 'Test']

    # Identify completions based on the highest process_step
    test_clients['completion'] = test_clients['process_step'] == 'confirm'

    # Calculate the completion rate for each client
    completion_rate = test_clients.groupby('client_id')['completion'].mean() * 100  # Convert to percentage
    print("Completion rate per client (Test group):")
    print(completion_rate)

    # Perform a one-sample t-test against the 5% threshold
    t_stat, p_value = stats.ttest_1samp(completion_rate, threshold)

    if completion_rate.mean() >= threshold and p_value < 0.05:
        print("The observed increase in completion rate meets or exceeds the 5% threshold and is statistically significant.")
    else:
        print("The observed increase in completion rate does not meet the 5% threshold or is not statistically significant.")

    # Print additional details
    print(f"Mean completion rate: {completion_rate.mean():.2f}%")
    print(f"t-statistic: {t_stat:.2f}, p-value: {p_value:.4f}")

    # Create a DataFrame for plotting
    results = pd.DataFrame({
        'Measure': ['Completion Rate', 'Threshold'],
        'Value': [completion_rate.mean(), threshold]
    })

    # Plotting
    fig, ax = plt.subplots()

    # Bar plot
    results.plot(kind='bar', x='Measure', y='Value', ax=ax, color=['skyblue', 'lightcoral'])

    # Add threshold line
    ax.axhline(y=threshold, color='r', linestyle='--', label='5% Threshold')

    # Adding annotations
    for index, row in results.iterrows():
        ax.text(index, row['Value'] + 1, f"{row['Value']:.2f}", ha='center')

    # Titles and labels
    ax.set_title('Completion Rate vs. 5% Threshold')
    ax.set_ylabel('Percentage')
    ax.legend()

    plt.show()

    # Calculate the observed increase in completion rate
    completion_rate_control = completion_data.loc[completion_data['Variation'] == 'Control', 'completion_rate'].values[0]
    completion_rate_test = completion_data.loc[completion_data['Variation'] == 'Test', 'completion_rate'].values[0]
    observed_increase = completion_rate_test - completion_rate_control
    print(f"Observed Increase in Completion Rate: {observed_increase:.2f}%")


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
    print("Average Time Spent on Each Step (Control Group):")
    print(time_spent_summary_control)
    
    # Calculate average time spent on each step for the Test group
    time_spent_summary_test = variation_df[variation_df['Variation'] == 'Test'].groupby('process_step')['time_spent'].mean().reset_index()
    time_spent_summary_test['Variation'] = 'Test'
    print("Average Time Spent on Each Step (Test Group):")
    print(time_spent_summary_test)
    
    # Combine both dataframes
    combined_df = pd.concat([time_spent_summary_control, time_spent_summary_test])

    # Order the process steps correctly
    step_order = ['start', 'step_1', 'step_2', 'step_3', 'confirm']
    combined_df['process_step'] = pd.Categorical(combined_df['process_step'], categories=step_order, ordered=True)
    combined_df = combined_df.sort_values('process_step').reset_index(drop=True)
    print("Combined DataFrame:")
    display(combined_df)
    
    # Plotting
    plt.figure(figsize=(12, 6))
    
    # Create separate palettes for control and test groups
    palette = {'Control': 'skyblue', 'Test': 'red'}
    
    # Create a bar plot using Seaborn
    sns.barplot(x='process_step', y='time_spent', hue='Variation', data=combined_df, palette=palette)
    
    # Set plot title and labels
    plt.title('Average Duration Spent on Each Step by Group (in seconds)')
    plt.xlabel('Process Step')
    plt.ylabel('Average Duration (seconds)')
    
    # Show plot
    plt.show()
    
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
    print("T-test Results for Each Process Step:")
    print(ttest_results_df)
    
    return ttest_results_df

def analyze_error_rates(variation_df):
    """
    This function analyzes the error rates and retries for clients in both control and test groups,
    performs a chi-square test to compare the error rates, and plots the results.

    Parameters:
    variation_df (pd.DataFrame): The DataFrame containing the process steps and variation labels.

    Returns:
    pd.DataFrame: A DataFrame containing the error rates for each group and the chi-square test results.
    """
    # Sort the data by client_id, visit_id, and date_time
    variation_df = variation_df.sort_values(by=['client_id', 'visit_id', 'date_time'])
    
    # Mapping process steps to numeric values
    step_mapping = { 'start': 0, 'step_1': 1, 'step_2': 2, 'step_3': 3, 'confirm': 4 } 
    variation_df['step_index'] = variation_df['process_step'].map(step_mapping)
    
    # Creating prev_step_index
    variation_df['prev_step_index'] = variation_df.groupby('visit_id')['step_index'].shift(1)
    
    # Detect backward navigation
    variation_df['is_back_track'] = variation_df['prev_step_index'] > variation_df['step_index']
    
    # Calculate error rates
    error_rates = variation_df.groupby('Variation')['is_back_track'].mean().reset_index(name='Error Rate')
    print("Error Rates:")
    print(error_rates)
    
    # Plotting the error rates
    plt.figure(figsize=(10, 6))
    sns.barplot(x='Variation', y='Error Rate', data=error_rates, palette=['skyblue', 'red'])
    
    # Set plot title and labels
    plt.title('Error Rates for Control and Test Groups')
    plt.xlabel('Group')
    plt.ylabel('Error Rate')
    
    # Show plot
    plt.show()
    
    # Create a contingency table
    contingency_table = pd.crosstab(variation_df['Variation'], variation_df['is_back_track'])
    
    # Perform chi-square test
    chi2, p, dof, ex = chi2_contingency(contingency_table)
    print(f"Chi-Square Test:\nChi2: {chi2}\np-value: {p}")
    
    # Return the error rates and chi-square test results
    return error_rates, chi2, p