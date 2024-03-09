# Explorer son historique de positions Google avec un plugin QGIS

## Etape1. Récupérer son historique de position Google

* Se rendre sur le site **https://takeout.google.com/settings/takeout**

* Cocher uniquement Historique de position
<br> ![alt text](https://raw.githubusercontent.com/bmericskay/GeoDataGoogle/main/1.PNG)

* **Passer à l'étape suivante**

<br> ![alt text](https://raw.githubusercontent.com/bmericskay/GeoDataGoogle/main/2.PNG)

* **Exporter le ficher avec vos données** (par mail par exemple)
<br> ![alt text](https://raw.githubusercontent.com/bmericskay/GeoDataGoogle/main/3.PNG)


* **Télécharger le  ficher avec vos données puis le décompresser**
<br> ![alt text](https://raw.githubusercontent.com/bmericskay/GeoDataGoogle/main/4.PNG)


* **Dans le dossier, trouver le ficher Records.json** (qui contient tout votre historique de position)
<br> <br> ![alt text](https://raw.githubusercontent.com/bmericskay/GeoDataGoogle/main/5.PNG)

<br> <br>
## Etape2. Préparer les données

Le fichier fourni par Google qui centralise vos données est dans le format JSON qui n'est pas très pratique pour explorer des données spatiales, de plus les coordonnées géographiques qui y sont renseignées ne sont pas utilisables.
<br/>

![alt text](https://raw.githubusercontent.com/bmericskay/GeoDataGoogle/main/JSON.PNG)
