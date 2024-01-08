import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns

@st.cache_data
def load_data():
    df = sns.load_dataset('tips')
    return df

def main():
    st.title('Streamlit with Seaborn')
    tips = load_data()

    m_tips = tips.loc[tips['sex']=='Male']
    f_tips = tips.loc[tips['sex']=='Female']

    fig, ax = plt.subplots(ncols=2, figsize=(10,6), sharex=True, sharey=True)
    sns.scatterplot(data=m_tips, x='total_bill', y='tip', ax=ax[0])
    ax[0].set_title('Male')
    sns.scatterplot(data=f_tips, x='total_bill', y='tip', ax=ax[1])
    ax[1].set_title('Female')
    ax[1].set(xlabel=None, ylabel=None)

    st.pyplot(fig)

if __name__=='__main__':
    main()