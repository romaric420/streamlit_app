# Titanic Analysis Dashboard

Application Streamlit d'analyse et de prédiction de la survie des passagers du Titanic.

## Description

Ce projet est une application web interactive construite avec Streamlit qui permet :
- D'explorer les données du Titanic avec des filtres dynamiques
- D'analyser les statistiques et corrélations
- De prédire la survie d'un passager avec un modèle de Machine Learning

## Structure du Projet
```
titanic_project/
│
├── app.py                      # Page d'accueil
├── requirements.txt            # Dépendances Python
├── README.md                   # Documentation
│
├── pages/
│   ├── 1_Exploration.py        # Page d'exploration des données
│   ├── 2_Analyse.py            # Page d'analyse statistique
│   └── 3_Predictions.py        # Page de prédiction ML
│
└── utils/
    ├── __init__.py             # Package Python
    ├── config.py               # Configuration (couleurs, labels)
    └── data_loader.py          # Chargement des données
```

## Fonctionnalités

### Page d'Accueil
- KPIs principaux (nombre de passagers, taux de survie, âge moyen, tarif moyen)
- Visualisation de la survie globale (pie chart)
- Survie par classe (bar chart)
- Téléchargement des données brutes en CSV

### Page Exploration
- Filtres interactifs (sexe, classe, âge)
- KPIs dynamiques selon les filtres
- Graphiques qui se mettent à jour automatiquement
- Export des données filtrées

### Page Analyse
- Statistiques descriptives
- Matrice de corrélation (heatmap)
- Tests d'hypothèses (Chi2) pour la survie selon le sexe et la classe
- Graphiques avancés (boxplot, violin plot)

### Page Prédictions
- Modèle Random Forest entraîné sur les données
- Affichage de l'accuracy et de la matrice de confusion
- Prédiction interactive : l'utilisateur entre les caractéristiques d'un passager et obtient une prédiction de survie

## Technologies Utilisées

| Technologie | Usage |
|-------------|-------|
| Python 3.x | Langage de programmation |
| Streamlit | Interface web |
| Pandas | Manipulation des données |
| Plotly | Visualisations interactives |
| Scikit-learn | Machine Learning |
| Scipy | Tests statistiques |
| Seaborn | Chargement du dataset |

## Installation

### 1. Cloner le repository
```bash
git clone https://github.com/votre-username/titanic-analysis.git
cd titanic-analysis
```

### 2. Créer un environnement virtuel
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows
```

### 3. Installer les dépendances
```bash
pip install -r requirements.txt
```

### 4. Lancer l'application
```bash
streamlit run app.py
```

L'application sera accessible sur `http://localhost:8501`

## Requirements
```
streamlit>=1.28.0
pandas>=2.0.0
numpy>=1.24.0
plotly>=5.17.0
scikit-learn>=1.3.0
scipy>=1.11.0
seaborn>=0.12.0
```

## Dataset

Le dataset Titanic provient de Seaborn et contient 891 observations avec les variables suivantes :

| Variable | Description | Type |
|----------|-------------|------|
| survived | Survie (0 = Non, 1 = Oui) | Target |
| pclass | Classe (1, 2, 3) | Catégoriel |
| sex | Sexe (male, female) | Catégoriel |
| age | Âge en années | Numérique |
| sibsp | Nombre de frères/soeurs/conjoints à bord | Numérique |
| parch | Nombre de parents/enfants à bord | Numérique |
| fare | Tarif du billet | Numérique |
| embarked | Port d'embarquement (C, Q, S) | Catégoriel |

## Résultats du Modèle

- Modèle : Random Forest Classifier
- Accuracy : ~80%
- Features utilisées : pclass, sex, age, sibsp, parch, fare, embarked

## Aperçu

### Page d'Accueil
Vue d'ensemble avec KPIs et graphiques principaux.

### Page Exploration
Filtres dynamiques pour explorer les données selon différents critères.

### Page Analyse
Statistiques détaillées, corrélations et tests d'hypothèses.

### Page Prédictions
Interface interactive pour prédire la survie d'un passager.

## Auteur

Romaric - 2026



