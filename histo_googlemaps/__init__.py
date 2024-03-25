# -*- coding: utf-8 -*-
"""
/***************************************************************************
 HistoriqueDesPositionsGoogle
                                 A QGIS plugin
 Ce plugin prend en entrée le fichier json de Google Maps et en ressort une visualisation des points GPS 
 Generated by Plugin Builder: http://g-sherman.github.io/Qgis-Plugin-Builder/
                             -------------------
        begin                : 2024-02-21
        copyright            : (C) 2024 by M2 SIGAT Groupe4
        email                : you@mail.box.fr
        git sha              : $Format:%H$
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
 This script initializes the plugin, making it known to QGIS.
"""


# noinspection PyPep8Naming
def classFactory(iface):  # pylint: disable=invalid-name
    """Load HistoriqueDesPositionsGoogle class from file HistoriqueDesPositionsGoogle.

    :param iface: A QGIS interface instance.
    :type iface: QgsInterface
    """
    #
    from .Histo_GoogleMaps import HistoriqueDesPositionsGoogle
    return HistoriqueDesPositionsGoogle(iface)
