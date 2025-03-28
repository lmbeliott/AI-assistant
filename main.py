import streamlit as st
import openai
import os
from dotenv import load_dotenv

load_dotenv()

max_char = 1000

api_key = os.getenv("OPENAI_API_KEY")
client = openai.OpenAI(api_key=api_key)


def chat_with_gpt(prompt):
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}],
        max_tokens=500
    )
    return response.choices[0].message.content.strip()


st.set_page_config(page_title="Aide Scolaire IA", layout="wide", page_icon="🎓")

st.title("🎓 Aide Scolaire IA - Ton Assistant Intelligent 📚")
st.sidebar.image("gymnase_logo.png")

st.sidebar.write(" ## Choisi une matière où tu as besoin d'aide.")
matiere = st.sidebar.selectbox("Selectionne :", [
    "Français", "Maths", "Physique-Chimie", "Histoire-Géo", "SVT", 
    "Langues", "Informatique", "Planificateur de Révisions"
])

st.write(f"📌 **Matière sélectionnée :** {matiere}")

if matiere == "Français":
    texte = st.text_area("📝 Entre ton texte pour correction :")
    action = st.radio("Que souhaites tu faire ?", ["Corriger la grammaire", "Améliorer la tournure de ton texte"])
    if st.button("Corriger"):
        if texte:
            if len(texte) <= max_char:
                if action == "Corriger la grammaire":
                    prompt = f"Corrige les fautes d'orthographe et de grammaire dans ce texte : {texte}"
                    correction = chat_with_gpt(prompt)
                    st.subheader("✅ Correction :")
                    st.write(correction)
                else:
                    prompt = f"Améliore la tournure des mots et des phrases pour les rendres plus belles dans ce texte : {texte}"
                    correction = chat_with_gpt(prompt)
                    st.subheader("✅ Correction :")
                    st.write(correction)
            else:
                st.subheader("✅ Correction :")
                st.write("Requête trop longue")
    
    st.write("## Dissertation")
    sujet = st.text_input("📖 Entre un sujet de dissertation :")
    if st.button("Générer un plan expliqué"):
        if sujet:
            if len(sujet) <= max_char:
                prompt = f"Donne un plan détaillé pour une dissertation sur : {sujet} en l'expliquant"
                plan = chat_with_gpt(prompt)
                st.subheader("🎭 Plan de dissertation :")
                st.write(plan)
            else:
                st.subheader("🎭 Plan de dissertation :")
                st.write("Requête trop longue")

elif matiere == "Maths":
    equation = st.text_input("🔢 Entre une équation ou un problème mathématique :")
    if st.button("Résoudre"):
        if equation:
            if len(equation) <= max_char:
                prompt = f"Résous cet exercice de maths en expliquant chaque étape : {equation}"
                solution = chat_with_gpt(prompt)
                st.subheader("🧮 Solution :")
                st.write(solution)
            else:
                st.subheader("🧮 Solution :")
                st.write("Requête trop longue")
        else:
            st.subheader("🧮 Solution :")
            st.write("Vous n'avez pas entré d'équations")
    st.write("## Aide à la révision 🧮")
    theme = st.text_input("🔢 Entre un Chapitre de Mathématique")
    classe = st.selectbox("Quelle est ta classe ?", ["Terminale", "Première", "Seconde", "3ème", "4ème", "5ème", "6ème"])
    action = st.radio("Que veut tu générer ?", ["QCM avec correction détaillée", "DS d'entraînement", "Plusieurs exercices avec corrigé"])
    if st.button("Générer"):
        if theme:   
            if len(theme) <= max_char:
                result = chat_with_gpt(f"Génère sur le chapitre de maths {theme}, il faut absolument que ça soit du niveau {classe}, {action} complet")
                st.subheader("Entraînement :")
                st.write(result)
            else:
                st.subheader("Entraînement :")
                st.write("Requête trop longue")



elif matiere == "Physique-Chimie":
    question = st.text_area("🔬 Entre une question sur la physique ou la chimie :")
    if st.button("Expliquer"):
        if question:
            if len(question) <= max_char:
                prompt = f"Explique en détail cette question de physique ou chimie : {question}"
                explication = chat_with_gpt(prompt)
                st.subheader("🧪 Explication :")
                st.write(explication)
            else:
                st.subheader("🧪 Explication :")
                st.write("Requête trop longue")
    st.write("## Aide à la révision ")
    theme = st.text_input("Entre un Chapitre de Physique ou de Chimie 🔬")
    classe = st.selectbox("Quelle est ta classe ?", ["Terminale", "Première", "Seconde", "3ème", "4ème", "5ème", "6ème"])
    action = st.radio("Que veut tu générer ?", ["QCM avec correction détaillée", "DS d'entraînement", "Plusieurs exercices avec corrigé"])
    if st.button("Générer"):
        if theme:
            if len(theme) <= max_char:
                result = chat_with_gpt(f"Génère sur le chapitre de physique-chimie {theme}, il faut absolument que ça soit du niveau {classe}, {action} complet")
                st.subheader("Entraînement :")
                st.write(result)
            else:
                st.subheader("Entraînement :")
                st.write("Requête trop longue")

elif matiere == "Histoire-Géo":
    sujet = st.text_input("📜 Entre un sujet historique ou géographique :")
    classe = st.selectbox("Quelle est ta classe ?", ["Terminale", "Première", "Seconde", "3ème", "4ème", "5ème", "6ème"])
    if st.button("Créer une fiche de révision"):
        if sujet:
            if len(sujet) <= max_char:
                prompt = f"Fais une fiche de révision concise et complète sur : {sujet}, il faut absolument que ça soit du niveau {classe}"
                fiche = chat_with_gpt(prompt)
                st.subheader("🗺️ Fiche de Révision :")
                st.write(fiche)
            else:
                st.subheader("🗺️ Fiche de Révision :")
                st.write("Requête trop longue")

elif matiere == "SVT":
    concept = st.text_input("🌱 Entre un concept de SVT à réviser :")
    if st.button("Expliquer"):
        if concept:
            if len(concept) <= max_char:
                prompt = f"Explique clairement ce concept de SVT : {concept}"
                explication = chat_with_gpt(prompt)
                st.subheader("🧬 Explication :")
                st.write(explication)
            else:
                st.subheader("🧬 Explication :")
                st.write("Requête trop longue")
    
    st.write("## Fiche de révision sur ce thème.")
    if st.button("Générer"):
        if concept:
            if len(concept) <= max_char:
                prompt = f"Fais une fiche de révision claire et concise sur ce concept de SVT : {concept}"
                explication = chat_with_gpt(prompt)
                st.subheader("🧬 Fiche :")
                st.write(explication)
            else:
                st.subheader("🧬 Fiche :")
                st.write("Requête trop longue")



elif matiere == "Langues":
    langue = st.selectbox("🌎 Choisis une langue :", ["Anglais", "Espagnol", "Allemand"])
    phrase = st.text_input("💬 Entre une phrase à corriger ou traduire :")
    action = st.radio("Que veux-tu faire ?", ["Corriger", "Traduire", "S'entraîner à parler"])

    if st.button("Lancer"):
        if phrase:
            if len(phrase) <= max_char:
                if action == "Corriger":
                    prompt = f"Corrige cette phrase en {langue} : {phrase}"
                elif action == "Traduire":
                    prompt = f"Traduis cette phrase en {langue} : {phrase}"
                else:
                    prompt = f"Imagine un dialogue en {langue} où tu réponds à : {phrase}"

                reponse = chat_with_gpt(prompt)
                st.subheader("🌍 Résultat :")
                st.write(reponse)
            else:
                st.subheader("🌍 Résultat :")
                st.write("Requête trop longue")


elif matiere == "Informatique":
    code = st.text_area("💻 Entre du code à analyser :")
    if st.button("Débugger/Expliquer"):
        if code:
            if len(code) <= max_char:
                prompt = f"Analyse et corrige ce code, en expliquant les erreurs : {code}"
                correction = chat_with_gpt(prompt)
                st.subheader("🖥️ Explication :")
                st.write(correction)
            else:
                st.subheader("🖥️ Explication :")
                st.write("Requête trop longue")

elif matiere == "Planificateur de Révisions":
    matieres = st.text_area("📆 Entre les matières et chapitres à réviser :")
    temps = st.slider("⏳ Temps de révision par jour (en minutes) :", 30, 180, 60)

    if st.button("Générer un planning"):
        if matieres:
            if len(matieres) <= max_char:
                prompt = f"Génère un planning de révisions avec {temps} minutes par jour pour ces matières : {matieres}"
                planning = chat_with_gpt(prompt)
                st.subheader("📅 Planning de révision :")
                st.write(planning)
            else:
                st.subheader("📅 Planning de révision :")
                st.write("Requête trop longue")


st.markdown("---")
st.markdown("👨‍💻 *Créé avec ❤️ par Eliott LAMBERT-ROME*")
