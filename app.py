import streamlit as st
import pickle as pkl
import pandas as pd
import math
pipe = pkl.load(open("CPP.pkl", "rb+"))
st.title("Car Price Prediction")
df=pd.read_csv("cleaned_car_data.csv")
companies = sorted(df["company"].unique())
company=st.selectbox("Enter Company", companies)
names=sorted(df[df["company"]==company]["name"].unique())
name=st.selectbox("Enter Car Model", names)
year=st.number_input("Enter Year of Manufacturing", min_value=1995, max_value=2026)
kms_driven=st.number_input("Enter kms driven", min_value=30000)
fuel_types=sorted(df["fuel_type"].unique())
fuel_type=st.selectbox("Enter Fuel Type", fuel_types)
if st.button("Predict"):
    data=[[name,company,year,kms_driven,fuel_type]]
    column=["name", "company", "year", "kms_driven", "fuel_type"]
    input=pd.DataFrame(data=data, columns=column)
    result=pipe.predict(input)
    result=result[0,0]
    value=math.ceil(result)
    st.text(f"₹{value:,}")