# -*- coding: utf-8 -*-
"""
/***************************************************************************
 ERA5DataReader
                                 A QGIS plugin
 This plugin loads and analyzes evaporation data from the Climate Data Store.
 Generated by Plugin Builder: http://g-sherman.github.io/Qgis-Plugin-Builder/
                             -------------------
        begin                : 2020-10-04
        copyright            : (C) 2020 by Elaf Seif
        email                : s-elaf.seif@zewailcity.edu.eg
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
    """Load ERA5DataReader class from file ERA5DataReader.

    :param iface: A QGIS interface instance.
    :type iface: QgsInterface
    """
    #
    from .era5_data_reader import ERA5DataReader
    return ERA5DataReader(iface)
