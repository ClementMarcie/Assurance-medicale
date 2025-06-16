import streamlit as st
import pandas as pd
import pickle

with open('mon_modele.pkl', 'rb') as f:
    model = pickle.load(f)

# Titre
st.title("Prédiction des charges d'assurance")

# Saisie utilisateur
age = st.slider("Âge", 18, 64, 30)
sex = st.selectbox("Sexe", ["male", "female"])
bmi = st.number_input("IMC", min_value=10.0, max_value=50.0, value=25.0)
children = st.number_input("Nombre d'enfants", min_value=0, max_value=5, value=0)
smoker = st.selectbox("Fumeur", ["yes", "no"])
region = st.selectbox("Région", ["northeast", "northwest", "southeast", "southwest"])

# DataFrame d'entrée
input_df = pd.DataFrame([{
    "age": age,
    "sex": sex,
    "bmi": bmi,
    "children": children,
    "smoker": smoker,
    "region": region
}])

# Prédiction
prediction = model.predict(input_df)[0]
st.subheader(f"Charge prédite : ${prediction:,.2f}")