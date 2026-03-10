import streamlit as st
import pandas as pd
import numpy as np
import joblib
import matplotlib.pyplot as plt
import seaborn as sns

pd.read_csv()
joblib.load("model.joblib")

st.set_page_config(
    page_title="NextBuyDELAY Prediction de réachat",
    page_icon="🏪",
    layout="wide",
)
