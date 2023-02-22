import streamlit as st
# import required modules
import os
from qgis.core import *
from qgis.utils import iface

# specify the path to the input shapefile
input_path = "path/to/colombia_shapefile.shp"

# specify the names of the regions to extract
regions = ["Santander", "Tolima"]

# specify the output directory for the shapefiles
output_dir = "path/to/output/directory"

# create a new layer object from the input shapefile
layer = QgsVectorLayer(input_path, "Colombia", "ogr")

# set the provider to read-only mode
layer.setReadOnly(True)

# create a new memory layer to hold the extracted features
mem_layer = QgsVectorLayer("Polygon?crs=epsg:4326", "Extracted Regions", "memory")

# get the feature writer for the memory layer
writer = mem_layer.dataProvider().getFeatureWriter()

# iterate over the features in the input layer
for feature in layer.getFeatures():
    # get the name of the current feature
    name = feature["NAME_1"]
    
    # check if the name matches one of the regions to extract
    if name in regions:
        # add the feature to the memory layer
        writer.addFeature(feature)
    
# commit the changes to the memory layer
mem_layer.commitChanges()

# create the output directory if it doesn't exist
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# iterate over the extracted regions and export them as shapefiles
for region in regions:
    # construct the output filename
    output_path = os.path.join(output_dir, f"{region}.shp")
    
    # apply a filter to the memory layer to select only the current region
    mem_layer.setSubsetString(f"NAME_1 = '{region}'")
    
    # export the selected features to a shapefile
    QgsVectorFileWriter.writeAsVectorFormatV2(mem_layer, output_path, QgsCoordinateTransformContext(), driverName="ESRI Shapefile")
    
    # reset the subset string for the memory layer
    mem_layer.setSubsetString("")
