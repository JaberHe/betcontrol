import streamlit as st

st.set_page_config(
    page_title="Hello",
    page_icon="👋",
)


st.sidebar.success("Veuillez sélectionner une page")

st.markdown("<h1 style='text-align: center; font-size: 3em;'>🎯 Bienvenue dans BetControl!</h1>", unsafe_allow_html=True)

# Lien URL de la présentation Canva

gdoc_url = "https://docs.google.com/presentation/d/1E2r1wxmoIYhMAKQ4jju-UxA1pelksvHOitH8y1Q0YWE/embed?start=false&loop=false&delayms=3000"


# Ajouter l'iframe dans Streamlit
st.components.v1.iframe(gdoc_url, width=800, height=600, scrolling=False)
