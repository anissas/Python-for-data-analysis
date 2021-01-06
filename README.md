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
  - Le fichier de code au format Jupyter
  - Le fichier relatif à l'API

## Librairies utilisées

## Analyse du probleme 

Afin de comprendre les variables et la facon dont elles influencaient la classe "Revenue", nous avons commencé par faire une datavisualistion de chaque variable ainsi qu'une matrice de correaltion des variables.

Voici notre matrice de corrélation ainsi que plusieurs exemples de graphiques entre nos variable et la variables "Revenue":


## Résultats

## Notre API
