import pandas as pd
import streamlit as st

@st.cache_data
def load_data():
    df = pd.read_csv('C:/Users/Administrator/Desktop/train.csv', 
                     parse_dates=['datetime']).dropna()
    return df

def main():
    st.title('Data Display st.data_editor()')
    data = load_data()
    st.data_editor(data)

if __name__=='__main__':
    main()