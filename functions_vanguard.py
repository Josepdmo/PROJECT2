
import functions_vanguard as vd
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import scipy.stats as st
from matplotlib.ticker import ScalarFormatter
from matplotlib.ticker import FuncFormatter
from scipy.stats import chi2_contingency
from scipy.stats import ttest_ind

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
    
    # Adjust the data type of 'client_id' to string
    df["client_id"] = df["client_id"].astype(str)
    
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



