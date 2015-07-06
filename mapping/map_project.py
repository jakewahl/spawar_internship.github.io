__author__ = 'jakewahl'

import csv
import os

def csv_to_list(path, filename):
    lst = []
    with open(os.path.join(path, filename), 'r') as f:
        rdr = csv.reader(f)
        for x in rdr:
            lst.append(x)
    return lst


def geolist_to_jsvar(lst):
    s = "var dataPoints = ["
    for x in lst[1:]:
        x[0], x[1], x[2], x[3], x[4], x[5], x[6] = x[2], x[1], x[6], x[0], x[3], x[4], x[5]
        s = s + str(x) + ", "
    s = s[0: -1] + "];"

    with open("js/aisdata.js", "w") as j:
        j.write(s)

if __name__ == '__main__':
    p = 'csv/'
    f = 'aisdata.csv'
    l = csv_to_list(p, f)
    geolist_to_jsvar(l)







