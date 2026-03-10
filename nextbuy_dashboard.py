import streamlit as st
import pandas as pd
import numpy as np
import joblib
import matplotlib.pyplot as plt
import seaborn as sns

model = joblib.load("model.joblib")

st.set_page_config(
    page_title="NextBuy - Delay de Prediction de réachat",
    page_icon="🛒",
    layout="wide",
)

@st.cache_data
def load_data():
    df_aisles = pd.read_csv("./datasets/aisles.csv")
    df_departments = pd.read_csv("./datasets/departments.csv")
    df_order_products = pd.read_csv("./datasets/order_products.csv")
    df_orders = pd.read_csv("./datasets/orders.csv")
    df_products = pd.read_csv("./datasets/products.csv")
    return df_aisles, df_departments, df_order_products, df_orders, df_products

df_aisles, df_departments, df_order_products, df_orders, df_products = load_data()

st.title("NextBuy : Assistant de Réachat")
produit_choisi = st.selectbox(f"Choissisez un produit", df_products["product_name"])

col1, col2 = st.columns(2)

with col1:
    heure = st.slider("heure", 0, 23, 12)
    liste_jours = ["Dimanche", "Lundi", "Mardi", "Mercredi", "Jeudi", "Vendredi", "Samedi"]
    nom_jour = st.selectbox("Jour de la semaine", options=liste_jours)
    jour_index = liste_jours.index(nom_jour)

with col2:
    delai = st.number_input("Jour depuis la dernière commande", min_value=0, max_value=30, value=7)
    position = st.number_input("Ordre d'ajout au panier", min_value=0, max_value=150, value=10)
