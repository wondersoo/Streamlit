import streamlit as st
import seaborn as sns
import pandas as pd

@st.cache_data
def load_data():
    df = sns.load_dataset('tips')
    return df

def main():
    st.title('Data Display st.metric()')

    tips = load_data()
    st.table(tips.describe())

    tip_max = tips['tip'].max()
    tip_min = tips['tip'].min()

    st.metric(label='Max Tip', value=tip_max, delta=tip_max-tip_min)
    st.metric(label='Min Tip', value=tip_min, delta=tip_min-tip_max)

if __name__=='__main__':
    main()