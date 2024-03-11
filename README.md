# Explorer son historique de positions Google avec un plugin QGIS

![alt text](https://raw.githubusercontent.com/mastersigat/ExploGooglePosition/main/Images/VisuelPlugin.PNG)

Si vous utilisez régulièrement Google Maps ou que vous possédez un téléphone sous Android, Google enregistre vos activités de déplacement. 

Les étudiants du M2 SIGAT (https://sites-formations.univ-rennes2.fr/mastersigat/) ont développé un PLugin QGIS (basé sur Pyhton) pour visualiser simplement vos données personnelles de localisation collectées par Google directemtn dans QGIS.

## Etape1. Récupérer son historique de position Google

* Se rendre sur le site **https://takeout.google.com/settings/takeout** pour récupérer ses données personnelles

* Cocher uniquement Historique de position
<br> ![alt text](https://raw.githubusercontent.com/bmericskay/GeoDataGoogle/main/1.PNG)

* **Passer à l'étape suivante**

<br> ![alt text](https://raw.githubusercontent.com/bmericskay/GeoDataGoogle/main/2.PNG)


* **Exporter le ficher avec vos données** (par mail par exemple)
<br> ![alt text](https://raw.githubusercontent.com/mastersigat/ExploGooglePosition/main/Images/ExportdataGoogle.PNG)


* **Télécharger le ficher avec vos données** (par mail par exemple)
<br> ![alt text](https://raw.githubusercontent.com/mastersigat/ExploGooglePosition/main/Images/ExportdataGoogle.PNG)


* **Télécharger le  ficher avec vos données puis le décompresser**
<br> ![alt text](https://raw.githubusercontent.com/bmericskay/GeoDataGoogle/main/4.PNG)


* **Dans le dossier, trouver le ficher Records.json** (qui contient tout votre historique de position)
<br> <br> ![alt text](https://raw.githubusercontent.com/bmericskay/GeoDataGoogle/main/5.PNG)

<br> <br>

Le fichier fourni par Google qui centralise vos données est dans le format JSON qui n'est pas très pratique pour explorer des données spatiales, de plus les coordonnées géographiques qui y sont renseignées ne sont pas utilisables.
<br/>

![alt text](https://raw.githubusercontent.com/bmericskay/GeoDataGoogle/main/JSON.PNG)

<br> <br>

## Etape2. Installer le plugin QGIS

Nous avons donc créé un plugin QGIS à l'aide de python qui prend en entrée le fichier JSON sorti par Google et sort un fichier csv et un fichier shapefile. Pour ajouter le plugin veuillez télécharger le zip disponible sur github. Ensuite, dirigez-vous vers les extensions et 'Installer depuis un ZIP'. Vous allez pouvoir renseigner le chemin du plugin et l'installer.</br>

Il faut d'abord télécharger le plugin QGIS (fait avec Python) disponible sur cette page :
<br> https://raw.githubusercontent.com/mastersigat/ExploGooglePosition/main/PluginQGIS_ExplorGooglePosition.zip

Ouvrir dans QGIS le gestionnaire des extensions
![alt text](https://raw.githubusercontent.com/mastersigat/ExploGooglePosition/main/Images/GestionExtension.PNG)

Intaller le plugin téléchargé

![alt text](https://raw.githubusercontent.com/mastersigat/ExploGooglePosition/main/Images/extension.PNG)

Le plugin est bien installé !

![alt text](https://raw.githubusercontent.com/mastersigat/ExploGooglePosition/main/Images/Instasucces.PNG)



## Etape3. Utilisation du plugin Histo_googlemaps

Afin qu'il apparaisse dans votre barre d'outils QGIS, allez dans les extensions installées et cocher le plugin Histo_googlemaps.
Puis, ouvrez le plugin (logo de Google Maps) et renseignez les champs de cette façon : 

![alt text](https://raw.githubusercontent.com/mastersigat/ExploGooglePosition/main/Images/Activateplugin.PNG)

<ul></ul>
  <li>Dans le premier paramètre, allez chercher votre fichier Records.json</li>
  <li>Ensuite, indiquez le répertoire dans lequel vous souhaitez enregistrer le fichier csv en ajoutant .csv après le nom</li>
  <li>Faites de même pour le shapefile en ajoutant .shp après le nom</li></br>

![alt text](https://raw.githubusercontent.com/mastersigat/ExploGooglePosition/main/Images/plugin.PNG)


Voici un exemple de ce que peut sortir le plugin avec des données remontant à 2014 :</br>
![alt text](https://raw.githubusercontent.com/mastersigat/ExploGooglePosition/main/Images/rendu.PNG)


-----------------

Ce plugin a été développé en 2024 par Constant Jonas - Delalande Jules - Lemétayer Clara - Leray Tristan.

