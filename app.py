import pandas as pd
import streamlit as st

st.title("Redrob AI Hiring System")

df = pd.read_csv("outputs/submission.csv")

st.dataframe(df, hide_index=True)

st.download_button(
    label="Download Submission CSV",
    data=df.to_csv(index=False),
    file_name="submission.csv",
    mime="text/csv"
)