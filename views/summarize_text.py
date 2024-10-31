import streamlit as st
from transformers import BartForConditionalGeneration, BartTokenizer

# Charger le modèle et le tokenizer pour le résumé
model = BartForConditionalGeneration.from_pretrained('facebook/bart-large-cnn')
tokenizer = BartTokenizer.from_pretrained('facebook/bart-large-cnn')

# Fonction pour résumer un texte donné
def summarize_text(text, max_length=150, min_length=50):
    inputs = tokenizer.encode("summarize: " + text, return_tensors="pt", max_length=1024, truncation=True)
    summary_ids = model.generate(inputs, max_length=max_length, min_length=min_length, length_penalty=2.0, num_beams=4, early_stopping=True)
    summary = tokenizer.decode(summary_ids[0], skip_special_tokens=True)
    return summary

st.title("Résumé de Texte Libre")

# Entrée de l'utilisateur pour le texte à résumer
text_input = st.text_area("Entrez le texte à résumer")

if st.button("Résumer"):
    if text_input:
        summary = summarize_text(text_input)
        st.write("Résumé:")
        st.write(summary)
    else:
        st.write("Veuillez entrer un texte à résumer.")
