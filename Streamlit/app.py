import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from vanguardbackend import analyze_control_group

def import_dataframe(file_path):
    df = pd.read_csv(file_path)
    return df


def main():
    st.title('Vanguard New Website Test')
    st.subheader("_Streamlit_ is :blue[cool] :sunglasses:")
    df = import_dataframe('variation.csv')
    analyze_control_group(df)


if __name__ == '__main__':
    main()
