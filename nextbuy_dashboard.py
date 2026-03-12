import streamlit as st
import pandas as pd
import numpy as np
import joblib

st.set_page_config(page_title="NextBuy", page_icon="🛒", layout="wide")

@st.cache_data
def load_products():
    return pd.read_csv("./datasets/products.csv")

@st.cache_resource
def load_model_assets():
    model = joblib.load("model.joblib")
    encoders = joblib.load("encoders.joblib")
    columns = joblib.load("model_columns.joblib")

    model_antoine = joblib.load("model-antoine.joblib")
    columns_antoine = joblib.load("model_column-antoine.joblib")

    return model, encoders, columns, model_antoine, columns_antoine


df_products = load_products()
model, dictionnaire_encodeurs, model_columns, model_antoine, columns_antoine = load_model_assets()


st.title("NextBuy : Assistant de Réachat")
produit_choisi = st.selectbox("Choisissez un produit", df_products["product_name"])
col1, col2 = st.columns(2)



with col1:
    heure = st.slider("Heure de la commande", 0, 23, 12)
    liste_jours = ["Dimanche", "Lundi", "Mardi", "Mercredi", "Jeudi", "Vendredi", "Samedi"]
    nom_jour = st.selectbox("Jour de la semaine", options=liste_jours)
    jour_index = liste_jours.index(nom_jour)



with col2:
    delai = st.number_input("Jours depuis la dernière commande", 0, 30, 7)
    position = st.number_input("Ordre d'ajout au panier", 1, 50, 5)

if st.button("Analyser la probabilité"):
    le_produit = dictionnaire_encodeurs["product_name_le"]

    if produit_choisi not in le_produit.classes_:
        st.warning("Produit non reconnu par le modèle.")
    else:
        encode_chiffre = le_produit.transform([produit_choisi])[0]

        X_predict = pd.DataFrame({
            "order_hour_of_day": [heure],
            "order_dow": [jour_index],
            "days_since_prior_order": [delai],
            "product_name": [encode_chiffre],
            "add_to_cart_order": [position]
        })[model_columns]

        proba_reachat = model.predict_proba(X_predict)[0][1]

        if proba_reachat >= 0.4:
            st.success(f"Réachat probable {proba_reachat:.1%}")
        else:
            st.error(f"Réachat peu probable {proba_reachat:.1%}")
        st.markdown("---")
        st.subheader("Analyse des probabilités sur 24h")
        df_simul = pd.DataFrame({
            "order_hour_of_day": list(range(24)),
            "order_dow": [jour_index] * 24,
            "days_since_prior_order": [delai] * 24,
            "product_name": [encode_chiffre] * 24,
            "add_to_cart_order": [position] * 24
        })[model_columns]

        probas_heures = model.predict_proba(df_simul)[:, 1]
        best_h = np.argmax(probas_heures)
        max_p = np.max(probas_heures)
        st.metric(label="Moment idéal pour proposer ce produit", value=f"{best_h}h")
        st.bar_chart(pd.DataFrame({"Probabilité": probas_heures}, index=list(range(24))))

    st.subheader("Tendance par jour de la semaine ")
    df_simul_jours = pd.DataFrame(0, index=range(7), columns=columns_antoine)


    if "order_hour_of_day" in columns_antoine: df_simul_jours["order_hour_of_day"] = heure
    if "add_to_cart_order" in columns_antoine: df_simul_jours["add_to_cart_order"] = position
    if "days_since_prior_order" in columns_antoine: df_simul_jours["days_since_prior_order"] = delai
    if "order_dow" in columns_antoine: df_simul_jours["order_dow"] = list(range(7))
    probas_jours_antoine = model_antoine.predict_proba(df_simul_jours)[:, 1]
    df_plot_jours = pd.DataFrame({"Probabilité": probas_jours_antoine}, index=liste_jours)
    st.line_chart(df_plot_jours)
