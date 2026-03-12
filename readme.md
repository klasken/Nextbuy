# NextBuy : Assistant de Prédiction de Réachat

NextBuy est un projet de Data Science visant à analyser les comportements d'achat sur la plateforme Instacart et à prédire la probabilité qu'un utilisateur commande à nouveau un produit spécifique lors de sa prochaine visite.

Le projet combine une analyse exploratoire approfondie (EDA) et un outil de prédiction interactif propulsé par Streamlit.

## Table des Matières
- Aperçu du Projet
- Structure du Dépôt
- Installation et Configuration
- Utilisation
- Méthodologie (Notebook)
- Dashboard Streamlit

## Aperçu du Projet
L'objectif est de répondre à des problématiques métier telles que :
* Analyse temporelle : Identifier quand les clients passent commande (pics horaires et journaliers).
* Analyse produits : Déterminer quels articles sont prioritaires le week-end ou souvent achetés ensemble.
* Prédiction : Anticiper le réachat d'un produit selon l'heure, le jour et le délai depuis la dernière commande.

## Structure du Dépôt
* nextbuy_dashboard.py : L'application interactive Streamlit.
* notebook-marius.ipynb : Le notebook Jupyter contenant l'analyse de données, le nettoyage et l'entraînement du modèle.
* datasets/ : Dossier contenant les fichiers CSV (aisles.csv, departments.csv, order_products.csv, orders.csv, products.csv).
* model.joblib : Le modèle de Machine Learning entraîné.
* encoders.joblib & model_columns.joblib : Fichiers de prétraitement pour assurer la cohérence des données dans le dashboard.

## Installation et Configuration

1. Cloner le projet :
   git clone https://github.com/votre-utilisateur/nextbuy.git
   cd nextbuy

2. Installer les bibliothèques requises :
   pip install streamlit pandas numpy joblib matplotlib seaborn scikit-learn

3. Données : Placez les fichiers CSV d'Instacart dans un dossier nommé datasets à la racine du projet.

## Utilisation

Pour lancer l'interface de prédiction interactive :
streamlit run nextbuy_dashboard.py

## Méthodologie (Notebook)
Le fichier notebook-marius.ipynb retrace tout le pipeline de données :
1. Exploration (EDA) : Visualisation des habitudes (ex: pic de commandes à 10h du matin).
2. Ingénierie des caractéristiques : Préparation des variables telles que l'heure de la journée, le jour de la semaine et le délai depuis la dernière commande.
3. Entraînement : Utilisation d'algorithmes de classification pour prédire la variable cible de réachat.
4. Export : Sauvegarde des composants du modèle pour une utilisation en production.

## Dashboard Streamlit
L'application permet de :
* Simuler une commande : Choisir un produit et définir les conditions (heure, jour, position dans le panier).
* Prédire : Afficher instantanément si le client va probablement recommander l'article (avec un seuil de probabilité de 40%).
* Optimiser : Visualiser une courbe de probabilité sur 24h pour déterminer le meilleur moment pour proposer un produit spécifique au client.

---
Projet réalisé dans le cadre d'une étude sur les comportements d'achat e-commerce.
