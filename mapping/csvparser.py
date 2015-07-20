__author__ = 'jakewahl'

import os
import csv
from datetime import datetime

def read_in_csv(path, file_name):
    """
    parses through a csv to separate individual pieces of data as well as different observations
    :param path: how to get to file
    :param file_name: name of data file
    :return: a list of the individual observation lists
    """
    lines = []
    with open(os.path.join(path, file_name), "r") as csv_file:
        reader = csv.reader(csv_file)
        for line in reader:
            lines.append(line)
    return lines

def make_geojson_js(path, file_name):
    '''
    writes to geojson.js the data in path+file_name as a geojson
    :param path: how to get to file: file_name
    :param file_name: where to get data
    :return: a dictionary that is formatted to convert l into a GeoJSON
    '''

    data_list = []
    # skip the first line of headers
    for line in read_in_csv(path, file_name)[1:101]:
        data_list.append(line)
    # points are ready to be formatted

    # prep str
    geojson_collection = """
    var aisData = {"type": "FeatureCollection", 'crs': {'type': 'name','properties':
        {'name': 'EPSG:3857'}}, "features": [
        """

    # for each observation format the geojson
    for line_list in data_list:
        json = """{"type": "Feature",
                "geometry": {"type": "Point", "coordinates": ["""+\
               "{0}, {1}".format(float(line_list[2]), float(line_list[1]))+\
                """]}, "properties": {"popupContent":
                """ +\
               """
               "Shipname: {0} Speed: {1} datetime: {2} mmsi: {3}"
               """.format(line_list[6], line_list[4], datetime.fromtimestamp(
                                    int(line_list[0])).strftime("%Y-%m-%d %H:%M:%S"), line_list[5])
        # add the geojson to the large str
        geojson_collection += json + "}},"
    # finally close brackets
    geojson_collection += "\n]}"

    #Write to file
    with open('js/geojson.js', 'w') as bla:
        bla.writelines(geojson_collection)

    # Useless return statement
    return geojson_collection

# When run this will execute
if __name__ == "__main__":
    #directory updated to be in same folder
    path = "csv/"
    file_name = "aisdata.csv"
    a = make_geojson_js(path, file_name)