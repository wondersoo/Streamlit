import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns

@st.cache_data
def load_data():
    df = sns.load_dataset('tips')
    return df

def main():
    st.title('Streamlit with Matplotlib')
    tips = load_data()

    m_tips = tips.loc[tips['sex']=='Male']
    f_tips = tips.loc[tips['sex']=='Female']

    fig, ax = plt.subplots(ncols=2, figsize=(10,6), sharex=True, sharey=True)
    ax[0].scatter(x=m_tips['total_bill'], y=m_tips['tip'])
    ax[0].set_title('Male')
    ax[1].scatter(x=f_tips['total_bill'], y=f_tips['tip'])
    ax[1].set_title('Female')

    st.pyplot(fig)

if __name__=='__main__':
    main()