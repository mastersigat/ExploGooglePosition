# Explorer son historique de positions Google avec un plugin QGIS

![alt text](https://raw.githubusercontent.com/mastersigat/ExploGooglePosition/main/Images/VisuelPlugin.PNG)

Si vous utilisez régulièrement Google Maps ou que vous possédez un téléphone sous Android, Google enregistre vos activités de déplacement. 

Les étudiants du Master 2 [SIGAT](https://sites-formations.univ-rennes2.fr/mastersigat/) ont développé un Plugin QGIS (basé sur Python) pour visualiser simplement vos données personnelles de localisation collectées par Google directement dans QGIS.

*Ce plugin a été développé en 2024 par Constant Jonas - Delalande Jules - Lemétayer Clara - Leray Tristan*


## Etape1. Récupérer son historique de position Google

* Se rendre sur le site **https://takeout.google.com/settings/takeout** pour récupérer ses données personnelles

* Cocher uniquement Historique de position

<p align="center">
  <img src="https://raw.githubusercontent.com/bmericskay/GeoDataGoogle/main/1.PNG" alt="alt tag" width="600">
</p>



* **Exporter le ficher avec vos données** (par mail par exemple)

<p align="center">
  <img src="https://raw.githubusercontent.com/mastersigat/ExploGooglePosition/main/Images/ExportTakeout.PNG" alt="alt tag" width="500">
</p>




* **Télécharger le  ficher avec vos données puis le décompresser**
<p align="center">
  <img src="https://raw.githubusercontent.com/mastersigat/ExploGooglePosition/main/Images/ExportdataGoogle.PNG" alt="alt tag" width="600">
</p>



* **Dans le dossier, trouver le ficher Records.json** (qui contient tout votre historique de position)
<br> <br> ![alt text](https://raw.githubusercontent.com/bmericskay/GeoDataGoogle/main/5.PNG)

<br> 

--------------------------------------------------------------------------------------------------------------------------

Le fichier fourni par Google qui centralise vos données est dans le format JSON qui n'est pas très pratique pour explorer des données spatiales, de plus les coordonnées géographiques qui y sont renseignées ne sont pas utilisables.

<p align="center">
  <img src="https://raw.githubusercontent.com/bmericskay/GeoDataGoogle/main/JSON.PNG" alt="alt tag" width="450">
</p>



<br> 

## Etape2. Installer le plugin QGIS

Afin de permettre de visualiser simplement les données de positions collectées par Google nous avons  créé un **plugin QGIS** à l'aide de python qui prend en entrée le fichier JSON sorti par Google et sort un fichier csv et un fichier shapefile. 


**Télécharger le plugin QGIS**<br><br>
Il faut d'abord télécharger le plugin QGIS (fait avec Python) disponible sur cette page :
<br> https://raw.githubusercontent.com/mastersigat/ExploGooglePosition/main/PluginQGIS_ExplorGooglePosition.
<br>

**Ouvrir dans QGIS le gestionnaire des extensions** <br>

<p align="center">
  <img src="https://raw.githubusercontent.com/mastersigat/ExploGooglePosition/main/Images/GestionExtension.PNG" alt="alt tag" width="850">
</p>

**Intaller le plugin téléchargé en chargant directement le fichier.zip** <br>
Il se peux que des messages d'erreurs apparaissent, il faut tout accepter ;)  <br>


<p align="center">
  <img src="https://raw.githubusercontent.com/mastersigat/ExploGooglePosition/main/Images/extension.PNG" alt="alt tag" width="850">
</p>



**Le plugin est bien installé !** <br>
<p align="center">
  <img src="https://raw.githubusercontent.com/mastersigat/ExploGooglePosition/main/Images/Instasucces.PNG" alt="alt tag" width="850">
</p>




## Etape3. Utilisation du plugin Histo_googlemaps

**Activer le nouveau Plugin dans le gestionnaire des extensions** 
Afin qu'il apparaisse dans votre barre d'outils QGIS, allez dans les extensions installées et cocher le plugin Histo_googlemaps.

![alt text](https://raw.githubusercontent.com/mastersigat/ExploGooglePosition/main/Images/Activateplugin.PNG)

**Lancer le plugin**

![alt text](https://raw.githubusercontent.com/mastersigat/ExploGooglePosition/main/Images/Lancementplugin.PNG)

**Configurer le chargement de votre historique de positions comme une couche géographique**


<ul></ul>
  <li>Dans le premier paramètre, allez chercher votre fichier Records.json</li>
  <li>Ensuite, indiquez le répertoire dans lequel vous souhaitez enregistrer le fichier csv en ajoutant .csv après le nom </li>
  <li>Faites de même pour enregistrer le fichier en shapefile en ajoutant .shp après le nom</li>

 <br>
<p align="center">
  <img src="https://raw.githubusercontent.com/mastersigat/ExploGooglePosition/main/Images/plugin.PNG" alt="alt tag" width="700">
</p>

**Vous pouvez explorer vos traces Google dans QGIS**

Voici un exemple de ce que peut sortir le plugin avec des données remontant à 2014 : <br><br>
![alt text](https://raw.githubusercontent.com/mastersigat/ExploGooglePosition/main/Images/Rendu.PNG)


-----------------


