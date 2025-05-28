# 📈 SmartPortfolio — Application Streamlit d'analyse boursière

SmartPortfolio est une application interactive développée avec [Streamlit](https://streamlit.io/) pour visualiser et analyser les actions du **S&P 500**, en calculant des indicateurs financiers pertinents, et en permettant à l'utilisateur de simuler un portefeuille d'investissement optimisé.

---

## ✨ Fonctionnalités

- 🔍 **Filtrage des entreprises** du S&P 500 par secteur
- 📈 **Graphiques interactifs** des cours de clôture (via Plotly)
- ⏳ **Récupération en temps réel** des données boursières (via Yahoo Finance)
- 📥 **Téléchargement CSV** des entreprises sélectionnées
- 💼 Idée à venir : **optimisation de portefeuille** selon le profil utilisateur (risque, éthique, frais...)

---

## 🧠 Technologies utilisées

- Python 3.10
- Streamlit
- Pandas
- yFinance
- Plotly
- Matplotlib / Seaborn
- GitHub

---

## 🚀 Lancer l'application en local

```bash
git clone https://github.com/KaiserXXX/smartportfolio.git
cd smartportfolio
pip install -r requirements.txt
streamlit run app.py
