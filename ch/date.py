import streamlit as st
import pandas as pd
import yfinance as yf
import plotly.graph_objects as go

def main():
    st.sidebar.title('Stock Chart')

    ticker = st.sidebar.text_input('Enter a ticker', value='AAPL')
    st.sidebar.markdown('Tickers Link : [All Stock Symbols](https://stockanalysis.com/stock/)')

    start_date = st.sidebar.date_input('Start date', value=pd.to_datetime('2023-01-01'))
    end_date = st.sidebar.date_input('End date', value=pd.to_datetime('today'))

    data = yf.download(ticker, start=start_date, end=end_date)

    chart_type = st.sidebar.radio('Select chart type', ('Candlestick', 'Line'))
    candlestick = go.Candlestick(x=data.index, open=data['Open'], high=data['High'],
                                 low=data['Low'], close=data['Close'])
    line = go.Scatter(x=data.index, y=data['Close'], mode='lines', name='Close')

    if chart_type=='Candlestick':
        fig = go.Figure(candlestick)
    elif chart_type=='Line':
        fig = go.Figure(line)
    else: pass

    fig.update_layout(title=f"{ticker} Stock {chart_type} Chart", xaxis_title='Date', yaxis_title='Price')

    st.plotly_chart(fig)
    st.markdown('<hr>', unsafe_allow_html=True)

    num_row = st.sidebar.number_input('Number of Raws', min_value=1, max_value=len(data))
    st.dataframe(data[-num_row:].reset_index().sort_index(ascending=False).set_index('Date'), use_container_width=True)

if __name__=='__main__':
    main()


