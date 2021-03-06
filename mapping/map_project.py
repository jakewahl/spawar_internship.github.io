__author__ = 'jakewahl'

import csv
import os
import dbconnect
from datetime import datetime

host = "localhost"
user = "root"
pwd = "lucky13"
dbname = "aisdb"

def csv_to_list(path, filename):
    lst = []
    with open(os.path.join(path, filename), 'r') as f:
        rdr = csv.reader(f)
        for x in rdr:
            lst.append(x)
    return lst


def geolist_to_jsvar(lst):
    s = "var dataPoints = "
    # for x in lst[1:]:
    #     x[0], x[1], x[2], x[3], x[4], x[5], x[6] = x[2], x[1], x[6], x[0], x[3], x[4], x[5]
    #     s = s + str(x) + ", "
    morphedList = []
    for l in lst:
        morphedList.append([float(l[2]), float(l[1]), "NAME: {}, Time: {}, CRS: {}, SPD: {}, MMSI: {}"
                  .format(l[6], datetime.fromtimestamp(int(l[0])).strftime('%Y-%m-%d %H:%M:%S'), l[3], l[4], l[5])])
    s += str(morphedList)
    s = s + ";"

    with open("js/aisdata.js", "w") as j:
        j.write(s)




def make_query_str(table, filters):
    '''

    :param table: name of table in database
    :param filters: dictionary where the key is the column name and the value is a tuple of strings to be combined into a SQL condition
    :return: a string that is valid SQL syntax to act on a database
    '''

    s = "SELECT unixtime, lat, lon, crs, spd, MMSI, SHIPNAME"

    def make_sql(conditions):
        string = ""
        for k, v in conditions.iteritems():
            if v[0].lower() == 'between':
                v[1], v[3] = min(v[3], v[1]), max(v[3], v[1])
            string += " AND {col} {oper} '{val1}' {_and} '{val2}'".format(col=k, oper=v[0], val1=v[1], _and=v[2], val2=v[3])
        return string

    s += " FROM {table} WHERE 1{filt}".format(table=table, filt=make_sql(filters))
    print s
    return s


if __name__ == '__main__':
    # p = 'csv/'
    # f = 'aisdata.csv'
    # l = csv_to_list(p, f)
    # geolist_to_jsvar(l)

    table = "obs"
    filters = {"lat": ["BETWEEN", "0", "AND", "179"], "lon": ["BETWEEN", "0", "AND", "-111"]}
    sql = make_query_str(table, filters)
    list_of_tuples = dbconnect.complete_command(host, user, pwd, sql, dbname)
    geolist_to_jsvar(list_of_tuples)
