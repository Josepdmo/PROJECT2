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
from statsmodels.stats.proportion import proportions_ztest

def Main():
    # Import the demo data
    df_final_demo = vd.import_dataframe()
    # Analyze client demographics
    df_final_demo = vd.analyze_client_demographics(df_final_demo)
    # Clean the demo DataFrame
    df_final_demo = vd.clean_dataframe(df_final_demo)
    
    # Import and check the first part of the DataFrame
    df_pt1 = vd.import_and_check_dataframe_part1()
    # Import and check the second part of the DataFrame
    df_pt2 = vd.import_and_check_dataframe_part2()
    
    # Merge the two parts of the DataFrame
    df = vd.merge_dataframes(df_pt1, df_pt2)
    
    # Import and analyze experiment clients
    df_final_experiment = vd.import_and_analyze_experiment_clients()
    
    # Merge and clean all DataFrames
    variation_df = vd.merge_and_clean_dataframes(df_final_demo, df, df_final_experiment)
    
    # Save the final DataFrame to a CSV file
    variation_df.to_csv('variation_df.csv', index=False)
    print("The file 'variation_df.csv' has been saved on your computer.")