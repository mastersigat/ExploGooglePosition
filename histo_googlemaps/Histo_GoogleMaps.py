# -*- coding: utf-8 -*-
"""
/***************************************************************************
 HistoriqueDesPositionsGoogle
                                 A QGIS plugin
 Ce plugin prend en entrée le fichier json de Google Maps et en ressort une visualisation des points GPS 
 Generated by Plugin Builder: http://g-sherman.github.io/Qgis-Plugin-Builder/
                              -------------------
        begin                : 2024-02-21
        git sha              : $Format:%H$
        copyright            : (C) 2024 by M2 SIGAT Groupe4
        email                : you@mail.box.fr
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
"""
from qgis.PyQt.QtCore import QSettings, QTranslator, QCoreApplication
from qgis.PyQt.QtGui import QIcon
from qgis.PyQt.QtWidgets import QAction

# Initialize Qt resources from file resources.py
from .resources import *
# Import the code for the dialog
from .Histo_GoogleMaps_dialog import HistoriqueDesPositionsGoogleDialog
import os.path
from qgis.PyQt.QtWidgets import *

#Import fonction historique des positions
import pandas as pd
import json
import geopandas as gpd
from qgis.core import QgsVectorLayer, QgsProject, QgsGraduatedSymbolRenderer, QgsRendererCategory
import pyproj
import matplotlib.pyplot as plt
from matplotlib.colors import LinearSegmentedColormap



class HistoriqueDesPositionsGoogle:
    """QGIS Plugin Implementation."""

    def __init__(self, iface):
        """Constructor.

        :param iface: An interface instance that will be passed to this class
            which provides the hook by which you can manipulate the QGIS
            application at run time.
        :type iface: QgsInterface
        """
        # Save reference to the QGIS interface
        self.iface = iface
        # initialize plugin directory
        self.plugin_dir = os.path.dirname(__file__)
        # initialize locale
        locale = QSettings().value('locale/userLocale')[0:2]
        locale_path = os.path.join(
            self.plugin_dir,
            'i18n',
            'HistoriqueDesPositionsGoogle_{}.qm'.format(locale))

        if os.path.exists(locale_path):
            self.translator = QTranslator()
            self.translator.load(locale_path)
            QCoreApplication.installTranslator(self.translator)

        # Declare instance attributes
        self.actions = []
        self.menu = self.tr(u'&Historique des positions Google')

        # Check if plugin was started the first time in current QGIS session
        # Must be set in initGui() to survive plugin reloads
        self.first_start = None

    # noinspection PyMethodMayBeStatic
    def tr(self, message):
        """Get the translation for a string using Qt translation API.

        We implement this ourselves since we do not inherit QObject.

        :param message: String for translation.
        :type message: str, QString

        :returns: Translated version of message.
        :rtype: QString
        """
        # noinspection PyTypeChecker,PyArgumentList,PyCallByClass
        return QCoreApplication.translate('HistoriqueDesPositionsGoogle', message)


    def add_action(
        self,
        icon_path,
        text,
        callback,
        enabled_flag=True,
        add_to_menu=True,
        add_to_toolbar=True,
        status_tip=None,
        whats_this=None,
        parent=None):
        """Add a toolbar icon to the toolbar.

        :param icon_path: Path to the icon for this action. Can be a resource
            path (e.g. ':/plugins/foo/bar.png') or a normal file system path.
        :type icon_path: str

        :param text: Text that should be shown in menu items for this action.
        :type text: str

        :param callback: Function to be called when the action is triggered.
        :type callback: function

        :param enabled_flag: A flag indicating if the action should be enabled
            by default. Defaults to True.
        :type enabled_flag: bool

        :param add_to_menu: Flag indicating whether the action should also
            be added to the menu. Defaults to True.
        :type add_to_menu: bool

        :param add_to_toolbar: Flag indicating whether the action should also
            be added to the toolbar. Defaults to True.
        :type add_to_toolbar: bool

        :param status_tip: Optional text to show in a popup when mouse pointer
            hovers over the action.
        :type status_tip: str

        :param parent: Parent widget for the new action. Defaults None.
        :type parent: QWidget

        :param whats_this: Optional text to show in the status bar when the
            mouse pointer hovers over the action.

        :returns: The action that was created. Note that the action is also
            added to self.actions list.
        :rtype: QAction
        """

        icon = QIcon(icon_path)
        action = QAction(icon, text, parent)
        action.triggered.connect(callback)
        action.setEnabled(enabled_flag)

        if status_tip is not None:
            action.setStatusTip(status_tip)

        if whats_this is not None:
            action.setWhatsThis(whats_this)

        if add_to_toolbar:
            # Adds plugin icon to Plugins toolbar
            self.iface.addToolBarIcon(action)

        if add_to_menu:
            self.iface.addPluginToMenu(
                self.menu,
                action)

        self.actions.append(action)

        return action

    def initGui(self):
        """Create the menu entries and toolbar icons inside the QGIS GUI."""

        icon_path = ':/plugins/Histo_GoogleMaps/icon.png'
        self.add_action(
            icon_path,
            text=self.tr(u'Historique des positions Google'),
            callback=self.run,
            parent=self.iface.mainWindow())

        # will be set False in run()
        self.first_start = True


    def unload(self):
        """Removes the plugin menu item and icon from QGIS GUI."""
        for action in self.actions:
            self.iface.removePluginMenu(
                self.tr(u'&Historique des positions Google'),
                action)
            self.iface.removeToolBarIcon(action)


    def run(self):
        """Run method that performs all the real work"""

        # Create the dialog with elements (after translation) and keep reference
        # Only create GUI ONCE in callback, so that it will only load when the plugin is started
        if self.first_start == True:
            self.first_start = False
            self.dlg = HistoriqueDesPositionsGoogleDialog()
            self.initBtns()

        # show the dialog
        self.dlg.show()
        
        # Run the dialog event loop
        result = self.dlg.exec_()
        # See if OK was pressed
        if result:
            self.process_data(self.dlg.lineEdit_in.text(), self.dlg.lineEdit_out.text())
            self.csv_to_shapefile(self.dlg.lineEdit_out.text(), self.dlg.lineEdit_out2.text())
            self.add_shp_map(self.dlg.lineEdit_out2.text(), self.dlg.lineEdit_out2.text())
            pass


    def initBtns(self):
        self.dlg.toolButton_in.clicked.connect(self.completeLineEdit_in)
        self.dlg.toolButton_out.clicked.connect(self.completeLineEdit_out)
        self.dlg.toolButton_out2.clicked.connect(self.completeLineEdit_out2)

    #rentrer le JSON
    def completeLineEdit_in(self):
        fileNameIn, _ = QFileDialog.getOpenFileName()
        print("chemin json", fileNameIn)
        self.dlg.lineEdit_in.setText(fileNameIn)
    
    #enregistrer le csv
    def completeLineEdit_out(self):
        filenameOut, _ = QFileDialog.getSaveFileName()
        print("chemin de sortie csv", filenameOut)
        self.dlg.lineEdit_out.setText(filenameOut)
    
    #enregistrer le shp
    def completeLineEdit_out2(self):
        filenameOut2, _ = QFileDialog.getSaveFileName()
        print("chemin de sortie shp", filenameOut2)
        self.dlg.lineEdit_out2.setText(filenameOut2)    
       
    #Code pour changer le JSON des traces GPS de Google en csv
    def process_data(self, json_file_path, csv_output_path):
        # Charger le fichier JSON
        with open(json_file_path) as f:
            data = json.load(f)
        # Transformer les données en DataFrame
        locations = pd.DataFrame(data["locations"])
        # Calculer les coordonnées en latitude et longitude
        locations["lat"] = locations["latitudeE7"] / 1e7
        locations["lon"] = locations["longitudeE7"] / 1e7
        # Sélectionner les colonnes nécessaires
        Historiquedepositions = locations[["timestamp", "lat", "lon"]]
        # Renommer les colonnes
        Historiquedepositions.columns = ["timestamp", "lat", "lon"]
        # Enregistrer en CSV
        Historiquedepositions.to_csv(csv_output_path, index=False)

    def csv_to_shapefile(self, csv_file, output_shapefile):
        # Charger le fichier CSV en tant que DataFrame
        data = pd.read_csv(csv_file)
        # Créer une géométrie Point à partir des colonnes lat et lon
        geometry = gpd.points_from_xy(data.lon, data.lat)
        # Convertir le DataFrame en GeoDataFrame
        gdf = gpd.GeoDataFrame(data, geometry=geometry)
        # Définir la projection initiale (EPSG:4326)
        gdf.crs = "EPSG:4326"
        # Reprojeter vers EPSG:2154
        gdf = gdf.to_crs("EPSG:2154")
        # Supprimer les colonnes lat et lon car elles sont maintenant incluses dans la géométrie
        gdf.drop(columns=['lat', 'lon'], inplace=True)
        # Écrire le shapefile
        gdf.to_file(output_shapefile, driver="ESRI Shapefile")
        return output_shapefile

        
    #ajouter le shapefile sur QGIS
    def add_shp_map(self, shapefile_path, layer_name):
        # Extraire le nom de la couche à partir de l'URL
        layer_nameok = layer_name.split('/')[-1]  # Supprimez tout le chemin de l'URL et conservez seulement le nom du fichier
        layer_nameok = layer_nameok[:-4]
        print("Nom du layer_name : ", layer_nameok) 
        # Construire le chemin complet vers la couche dans le shapefile
        layer_path = "{}|layername={}".format(shapefile_path, layer_nameok)
        # Chargement de la couche shapefile
        layer = QgsVectorLayer(layer_path, layer_nameok, "ogr")
        # Vérification si le chargement de la couche a réussi
        if not layer.isValid():
            print("Impossible de charger la couche !")
            return False        
        # Ajout de la couche à la carte QGIS
        QgsProject.instance().addMapLayer(layer)
        return True
