import streamlit as st
import datetime
import humanize
from currency_converter import convert_currency, get_exchange_rate, get_currencies


st.title("💱 Currency Converter")

st.divider()

col1, col2 = st.columns(2)

currencies = get_currencies()
with col1:
    base_currency = st.selectbox("From Currency (Base) :", currencies)
with col2:
    target_currency = st.selectbox("To Currency (Target) :", currencies)

amount = st.number_input("Amount :", min_value=1.0 , value=1.0)

convert_button = st.button("Convert", icon='🔁')

st.divider()

if amount >= 1 and base_currency and target_currency and convert_button:
    exchange_rate, time_last_updated = get_exchange_rate(base_currency, target_currency)
    time_diff = datetime.datetime.now() - datetime.datetime.fromtimestamp(time_last_updated)
    time_ago = humanize.naturaltime(time_diff)

    if exchange_rate:
        converted_amount = convert_currency(amount, exchange_rate)
        col1, col2, col3 = st.columns(3)
        col1.metric(label="Base Currency", value=f"{amount:.2f} {base_currency}")
        col2.markdown("<h1 style='text-align: center; margin: 0;'>&#8594;</h1>", unsafe_allow_html=True)
        col3.metric(label="Target Currency", value=f"{converted_amount:.2f} {target_currency}")
        st.success(f"✅ Exchange Rate: {exchange_rate:.2f} (Last updated: {time_ago})")
    else:
        st.error("Error: Unable to fetch the exchange rate. Please try again.")
