import streamlit as st
from sklearn.ensemble import RandomForestClassifier
from sklearn.datasets import load_iris
import plotly.express as px
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

#configurer la mise en page de la page Streamlit pour quelle soit large
st.set_page_config(layout="wide")

#titre principal
st.title("Hello j'apprend streamlit")
st.subheader("je vais devenir tellement fort ")

#crerr une side bar
st.sidebar.title("mon side bar")
st.sidebar.subheader("contenu principal")

#ecrire un markdown
st.markdown("##ici c'est un Markdown")

#creation de trois colonnes avec des largeurs specifiques(2:1:2)
c1,c3,c2 = st.columns(3)

#ajouter des titre aux colonnes
c1.title("column 1")
c2.title("column 2")
c3.title("column 3")

#ajouter des espaces et des lignes de separation
st.write("##")
st.divider()
st.write("##")

#titre pour la deuxieme section
st.title("input widgets")

#widget pour entrer unj nombre avec une valeur par defaut de 42.0
st.number_input("Nombre", value=42,min_value=10,max_value=500)

#pour afficher une notification toast lorsquil est clique
if st.button("button"):
    st.toast("merci d'avoir cliquer sur le button")

#pour afficher un warning lorsquil est clique
if st.button("button 2"):
    st.warning("attention")
    
#pour afficher un info lorsquil est clique
if st.button("button 3"):
    st.info("realisation  au top")

#pour afficher un succes lorsquil est clique
if st.button("button 4"):
    st.info("clique realiser avec succes")
    
#chekbox qui renvoi un booleen
is_checked = st.checkbox("cocher pour activer")
st.write(f"Checkbox : {is_checked}")

#toggle identique a un choix ici
is_toggle = st.toggle("toggle pour activer")
st.write(f"toggle:{is_toggle}")

#selectionner une option parmit plusieurs
one_select = st.selectbox("selectbox",["veuillez faire un choix svp","option 1","option 2","option 3"],index=1)
st.write(f"selectbox: {one_select}")

#Multiselection on choisis plusieurs option
multi_select = st.multiselect("Multiselect",["option 1","option 2","option 3"])
st.write(f"Multiselect: {multi_select}")

#creer un formulaire avec un champs de texte
with st.form("mon formulaire"):
    text_input = st.text_input("votre nom svp")
    text_area = st.text_area("un message svp")
    submit_button = st.form_submit_button("submit")

#afficher la valeur saisies dans le formulaire
if submit_button:
    st.write(f"Text input : {text_input}")
    st.write(f"Text area : {text_area}")
    
#ajouter un espaces et une ligne de separation
st.write("#####")
st.divider()
st.write("#####")    



#sous-titre pour la section des graphiques
st.subheader("Graphiques")

#--------graphiaue avec plotly-------------
#charger le jeu de donnees 'iris avec seaborn

df = sns.load_dataset("iris")

#creer un graphique simple avec plotly
fig = px.scatter(df,x="sepal_length",y="sepal_width",color="species")

# afficher le graphique plotly dans l'application
st.plotly_chart(fig)



#-----------graphyque avec matplotlib------------
#Generer des donnees pour le graphique
x = np.linspace(0,10,100)
y = np.sin(x)

#crerr une figure matplotlib
figure = plt.figure()
#tracer la courbe
plt.plot(x,y)
#afficher le graphique Matplotlib dans lapplication
st.pyplot(figure)

#ajouter des espaces et une ligne de separation
st.write("###")
st.divider()
st.write("###")

#ajouter uyn header de la troisieme partie
st.subheader("Affichage du Dataframe")

#creer un datframe
df = pd.DataFrame(np.random.randn(50,5),columns=("colonne %d" % i for i in range(5)))

#aficher le dataframe
st.dataframe(df)

#sous-titre chargement de fichier csv
upload_file = st.file_uploader("choisissez un fichier csv")

#si un fichier est uploader le lire et afficher
if upload_file is not None:
    df = pd.read_csv(upload_file)
    st.write(df)
else:
    st.info("veuillez charger un fichier csv pour afficher les donnees.")

#sous-titre de la section prediction avec un modele de machine learning
st.subheader("prediction avedc un modele de machine learning")

#--------------chargement et entrainement du modele---------------
#charger  le jeu de donnees iris
iris = load_iris()
X = iris.data
y = iris.target

#crerr un classifieur random Forest
clf = RandomForestClassifier()

#Entrainer le modele sur lensemble des donnees
clf.fit(X,y)

#-----------------interface utilisateur pour entrer les donnees du modele------------
st.sidebar.divider()
st.sidebar.subheader("parametres d'entree du modele de machine learning")

# Sliders pour saisir les caractéristiques du modèle
sepal_length = st.sidebar.slider(
    "Longueur du sépale",
    float(X[:, 0].min()),
    float(X[:, 0].max()),
    float(X[:, 0].mean()),
)

sepal_width = st.sidebar.slider(
    "Largeur du sépale",
    float(X[:, 1].min()),
    float(X[:, 1].max()),
    float(X[:, 1].mean()),
)

petal_length = st.sidebar.slider(
    "Longueur du pétale",
    float(X[:, 2].min()),
    float(X[:, 2].max()),
    float(X[:, 2].mean()),
)

petal_width = st.sidebar.slider(
    "Largeur du pétale",
    float(X[:, 3].min()),
    float(X[:, 3].max()),
    float(X[:, 3].mean()),
)

#button pour lancer la prediction
start_prediction = st.sidebar.button("predire")

#ajouter un espace avant la session de resultat
st.write("#####")
st.subheader("utilisation de modele de machine learning")

# -------- Effectuer la prédiction --------
if start_prediction:
    # Créer un tableau avec les valeurs d'entrée
    input_data = [[sepal_length, sepal_width, petal_length, petal_width]]

    # Prédire la classe de la fleur
    prediction = clf.predict(input_data)

    # Obtenir les probabilités pour chaque classe
    prediction_proba = clf.predict_proba(input_data)

    # Afficher le résultat de la prédiction
    st.write("### Classe prédite :", iris.target_names[prediction][0])
    st.write("### Probabilités :")
    st.write(prediction_proba)

# Ajouter des espaces et une ligne de séparation
st.write("##")
st.divider()
st.write("##")

#sous titre pour la section html css

st.subheader("utiliser html et css")

#injecter dun css personaliser pour augmenter la taille du text


st.markdown(
    """
    <style>
        .grand-text{
            font-siwe:70px !important;
        }
    </style>
    """,
    unsafe_allow_html=True,
)


# Utiliser une balise HTML avec la classe CSS définie
st.markdown("<p class='grand-texte'>Texte en grand</p>", unsafe_allow_html=True)

# Ajouter un espace avant la section suivante
st.write("##")
st.subheader("Utiliser le cache")

# -------- Utilisation du cache avec st.cache_data --------
@st.cache_data(ttl=60)  # Le cache expire après 60 secondes
def charger_donnees():
    # Simulation d'un chargement de données coûteux
    data = {"valeurs": [1, 2, 3, 4, 5]}
    return data

#appeler la fonction pour charger les donnees
data = charger_donnees()
st.write(data)

# -------- Mise en cache d'un modèle de Machine Learning --------
@st.cache_data
def train_model():
    # Simuler un entrainement de modèle coûteux
    clf = RandomForestClassifier(n_estimators=100)
    clf.fit(X, y)
    return clf

# Appeler la fonction pour entrainer le modèle (sera mis en cache)
clf = train_model()

# Ajouter un espace avant la section suivante
st.write("##")
st.subheader("Utiliser la session")

# -------- Gestion de l'état avec st.session_state --------
# Initialiser un compteur dans la session si ce n'est pas déjà fait
if "compteur" not in st.session_state:
    st.session_state.compteur = 0

# Bouton pour incrémenter le compteur
if st.button("Incrémenter"):
    st.session_state.compteur += 1

# Afficher la valeur actuelle du compteur
st.write("Valeur du compteur :", st.session_state.compteur)
