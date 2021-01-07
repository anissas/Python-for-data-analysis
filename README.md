# Python-for-data-analysis

## Notre dataset

Notre data set est composé de 12 330 sessions sur l'intention d'achat des utilisateurs d'un site de e-commerce. Le but est de prédire si un visiteur, déjà inscrit sur le site ou nouveau, va acheter un produit ou non. 

Pour cela, nous avons accès à des données d'utilisateurs sur une période d'un an.
Le dataset se compose de 18 classes, 10 numériques et 8 catégoriques et aucune valeur ne manque. Nous avons converti certaines valeurs en valeurs numériques telles que "Revenue", "Week-end", "Visitor_type" et "Months" afin de pouvoir les analyser plus simplement. 
Les valeurs de ces fonctionnalités sont dérivées des informations URL des pages visitées par l'utilisateur et mises à jour en temps réel lorsqu'un utilisateur effectue une action, par exemple, passer d'une page à une autre.

La classe 'Revenue' est celle que nous voulons prédire. Il s'agit de valeurs booleenes que nous avons converties en numériques, 0 ou 1, qui nous permettent de savoir si l'utilisateur a acheté ou non.

  - "Administrative", "Administrative Duration", "Informational", "Informational Duration", "Product Related" et "Product Related Duration" représentent le nombre de différents types de pages visitées par le visiteur au cours de cette session et le temps total passé dans chacune des ces catégories de page. 
  
  - "Bounce Rate", "Exit Rate" et "Page Value" représentent les statistiques mesurées par "Google Analytics" pour chaque page du site de commerce électronique. Par exemple, la valeur de la fonctionnalité "Bounce Rate" pour une page Web fait référence au pourcentage de visiteurs qui accèdent à une page, puis la quittent sans déclencher d'autres demandes.
  
  - "Page Value" représente la valeur moyenne d'une page Web visitée par un utilisateur avant d'effectuer une transaction. 
  
  - "Special Day" indique la proximité de l'heure de visite du site avec un jour spécial spécifique (par exemple, Noël ou la Saint-Valentin).
  
  - Les autres classes sont "Operating System", "Browser", "Region", "Traffic Type", "Visitor Type" (Déjà utilisateur ou non) ainsi que "Week-end" (commandes effectuées en week-end ou non).
  
## Contenu

Vous trouverez dans ce Github:

  - Le fichier Readme qui introduisant notre jeu de données, notre API et nos résulats 
  - Une présentation Powerpoint expliquant les tenants et aboutissants du problème, ainsi que nos réflexions et choix
  - Le dataset en format csv
  - Le fichier de code au format Jupyter
  - Le fichier relatif à l'API


## Analyse du probleme 

Afin de comprendre les variables et la facon dont elles influencaient la classe "Revenue", nous avons commencé par faire une datavisualistion de chaque variable ainsi qu'une matrice de correaltion des variables.

Voici notre matrice de corrélation ainsi que plusieurs exemples de graphiques entre nos variable et la variables "Revenue":

## Résultats

Nous avons realisé plusieurs modèles de classification binaire sur notre jeu de données comme par exemple le KNN, la régression logistique ou même l'arbre décisionnel. Afin de comprendre le fonctionnement des modeles par rapport à nos données et d'analyser la précision, nous avons, pour chaque modele, appliqué le grid search afin de trouver les meilleurs hyper-paramètres. 

Nous comparons ensuite tous les modèles (avec les meilleurs hyper paramètres pour chacun) pour en conclure sur le meilleur modele: 

L'arbre décisionnel est donc le meilleur modèle parmi tout les modèles de classification testés avec les paramètres 'criterion':"gini" et 'max_depth':4.
Cela nous permet de trouver une précision de 0.902.

## Notre API

Nous avons réalisé une API grâce à Flask en Python.

Deux npoint ont été créés:
"/": Accueil de l'utilisateur sur notre API

"/predict" methods 'post':
L'utilisateur entre un tableau de ligne à prédire et notre meilleur modèle sort les prédictions faites dans un tableau.

Fichier contenant nos lignes du xtest:
x_test.json

Test de l'API:
Ouvrez un invite de commande.
Placez vous dans le répertoire où se situe le fichier appPython.py 
Tapez sur une console:

❯ cd /path/to/workspace/API
❯ python appPython.py

(Notre API se lance toujours sur le port 80 car nous l'avons définit nous même)

Avec postman copiez le lien: "http://127.0.0.1:80/predict" 

Choisir "POST":

Sélectionnez Body

Sélectionnez raw

Copiez/Collez toutes ou quelques lignes depuis le fichier x_test.json fourni.

⚠️ Les lignes copiées doivent être contenues dans un tableau comme dans l'exemple suivant:

[
    {"Administrative":0,"Administrative_Duration":0.0,"Informational":0,"Informational_Duration":0.0,"ProductRelated":1,"ProductRelated_Duration":0.0,"BounceRates":0.2,"ExitRates":0.2,"PageValues":0.0,"SpecialDay":0.0,"Month":1,"OperatingSystems":1,"Browser":1,"Region":1,"TrafficType":1,"VisitorType":1,"Weekend":0},
    {"Administrative":0,"Administrative_Duration":0.0,"Informational":0,"Informational_Duration":0.0,"ProductRelated":2,"ProductRelated_Duration":64.0,"BounceRates":0.0,"ExitRates":0.1,"PageValues":0.0,"SpecialDay":0.0,"Month":1,"OperatingSystems":2,"Browser":2,"Region":1,"TrafficType":2,"VisitorType":1,"Weekend":0},
    {"Administrative":0,"Administrative_Duration":0.0,"Informational":0,"Informational_Duration":0.0,"ProductRelated":1,"ProductRelated_Duration":0.0,"BounceRates":0.2,"ExitRates":0.2,"PageValues":0.0,"SpecialDay":0.0,"Month":1,"OperatingSystems":4,"Browser":1,"Region":9,"TrafficType":3,"VisitorType":1,"Weekend":0},
    {"Administrative":0,"Administrative_Duration":0.0,"Informational":0,"Informational_Duration":0.0,"ProductRelated":2,"ProductRelated_Duration":2.666666667,"BounceRates":0.05,"ExitRates":0.14,"PageValues":0.0,"SpecialDay":0.0,"Month":1,"OperatingSystems":3,"Browser":2,"Region":2,"TrafficType":4,"VisitorType":1,"Weekend":0},
    {"Administrative":0,"Administrative_Duration":0.0,"Informational":0,"Informational_Duration":0.0,"ProductRelated":10,"ProductRelated_Duration":627.5,"BounceRates":0.02,"ExitRates":0.05,"PageValues":0.0,"SpecialDay":0.0,"Month":1,"OperatingSystems":3,"Browser":3,"Region":1,"TrafficType":4,"VisitorType":1,"Weekend":1},
    {"Administrative":0,"Administrative_Duration":0.0,"Informational":0,"Informational_Duration":0.0,"ProductRelated":19,"ProductRelated_Duration":154.2166667,"BounceRates":0.015789474,"ExitRates":0.024561404,"PageValues":0.0,"SpecialDay":0.0,"Month":1,"OperatingSystems":2,"Browser":2,"Region":1,"TrafficType":3,"VisitorType":1,"Weekend":0},
    {"Administrative":0,"Administrative_Duration":0.0,"Informational":0,"Informational_Duration":0.0,"ProductRelated":1,"ProductRelated_Duration":0.0,"BounceRates":0.2,"ExitRates":0.2,"PageValues":0.0,"SpecialDay":0.4,"Month":1,"OperatingSystems":2,"Browser":4,"Region":3,"TrafficType":3,"VisitorType":1,"Weekend":0},
    {"Administrative":1,"Administrative_Duration":0.0,"Informational":0,"Informational_Duration":0.0,"ProductRelated":0,"ProductRelated_Duration":0.0,"BounceRates":0.2,"ExitRates":0.2,"PageValues":0.0,"SpecialDay":0.0,"Month":1,"OperatingSystems":1,"Browser":2,"Region":1,"TrafficType":5,"VisitorType":1,"Weekend":1}
]

Exemple de sortie: 
{
    "prediction": "[0, 0, 0, 0, 0, 0, 0, 0]"
}
