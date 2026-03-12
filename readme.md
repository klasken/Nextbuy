# NextBuy : Assistant de Prédiction de Réachat

NextBuy est un projet de Data Science visant à analyser les comportements d'achat et à prédire la probabilité qu'un utilisateur commande à nouveau un produit spécifique lors de sa prochaine visite.

Le projet combine des analyses exploratoires approfondies réalisées par plusieurs analystes et un outil de prédiction interactif propulsé par Streamlit.

## Table des Matières
- Aperçu du Projet
- Structure du Dépôt
- Installation et Configuration
- Utilisation
- Détail des Analyses (Notebooks)
- Dashboard Streamlit

## Aperçu du Projet
L'objectif est de répondre à des problématiques métier telles que :
* Analyse temporelle : Identifier quand les clients passent commande (pics horaires et journaliers).
* Segmentation client : Distinguer les profils d'acheteurs (nocturnes, occasionnels, etc.).
* Prédiction : Anticiper le réachat d'un produit selon l'heure, le jour et le délai depuis la dernière commande.

## Structure du Dépôt
* nextbuy_dashboard.py : L'application interactive Streamlit.
* notebook-marius.ipynb : Analyse des pics de commande, produits du samedi et entraînement du modèle.
* notebook-antoine.ipynb : Étude des profils clients, analyse du premier article ajouté au panier et taux de réachat par produit.
* notebook-oles.ipynb : Analyse comparative (nourriture animaux) et corrélation entre délai de commande et réachat.
* datasets/ : Dossier contenant les fichiers CSV (aisles, departments, order_products, orders, products).
* model.joblib : Le modèle de Machine Learning entraîné.
* encoders.joblib & model_columns.joblib : Fichiers de prétraitement pour le dashboard.

## Installation et Configuration

1. Cloner le projet :
   git clone https://github.com/klasken/nextbuy.git
   cd nextbuy

2. Installer les bibliothèques requises :
   pip install streamlit pandas numpy joblib matplotlib seaborn scikit-learn

3. Données : Placez les fichiers CSV d'Instacart dans un dossier nommé datasets à la racine du projet.

## Utilisation

Pour lancer l'interface de prédiction interactive :
```bash
streamlit run nextbuy_dashboard.py
