import streamlit as st

# --- Configuration des pages ---
document_summary_page = st.Page(
    page="views/summarize_document.py",
    title="Résumé de Document",
    # icon=":page_facing_up:",
    default=True
)
rag_page = st.Page(
    page="views/rag.py",
    title="Recherche RAG",
    # icon=":mag_right:"
)
text_summary_page = st.Page(
    page="views/summarize_text.py",
    title="Résumé de Texte",
    # icon=":memo:"
)

# --- Navigation ---
pg = st.navigation(
    {
        "Fonctionnalités": [document_summary_page, rag_page, text_summary_page]
    }
)

# --- Logo ou informations supplémentaires ---
# st.logo("path/to/logo.png")  # Remplacez avec le chemin réel du logo
st.sidebar.text("Fait par LE TEAM 😎")

# --- Lancer la navigation ---
pg.run()
