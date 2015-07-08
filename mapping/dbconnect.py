__author__ = 'jakewahl'

import time
import os
from collections import OrderedDict
import MySQLdb
import sys
import csv
from datetime import datetime

host = "localhost"
user = "root"
pwd = "lucky13"
dbname = "aisdb"
table = "obs"


def create_connection(host, user, pwd, dbname):
    '''

    :param host:
    :param user:
    :param pwd:
    :param dbname:
    :return:
    '''

    try:
        conn = MySQLdb.connect(host, user, pwd, dbname)
        print "connection completed"
    except MySQLdb.Error as e:
        print "no connection.\nError Message: {}\nexiting...".format(e)
        sys.exit(1)
    return conn

def create_db(host, user, pwd, dbname):
    '''
    create_db(host, user, pwd, dbname)
    :param host:
    :param user:
    :param pwd:
    :param dbname:
    :return:
    '''

    conn = create_connection(host, user, pwd)
    cursor = conn.cursor()
    try:
        # open db connection
        # MySQLdb.connect(host, user, pwd)
        sql = "CREATE DATABASE IF NOT EXISTS" + dbname
        cursor.execute(sql)
        print "Created db: ", dbname
        cursor.close()
        conn.close()

def create table(tablename, columns, host, user, pwd, dbname):
    '''
    create_table('obs', d, host, user, pwd, dbname)
    d = OrderedDict([('id', ('INT', 'NOT NULL AUTO_INCREMENT')),
             ('unixtime', ('BIGINT', 'NOT NULL')),
             ('lat', ('DOUBLE', 'NOT NULL')),
             ('lon', ('DOUBLE', "")),
             ('crs', ('DOUBLE', "")),
             ('spd', ('DOUBLE', '')),
             ('MMSI', ('VARCHAR(9)', "")),
             ('SHIPNAME', ('VARCHAR(50)', "")),
             ('', ('PRIMARY KEY(id)', ''))
             ])
    '''
    conn = create_connection(host, user, pwd, dbname)
    cursor = conn.cursor()

    cols = ""
    for key, val in columns.iteritems():
        cols += ", {} {} {}".format(key, val[0], val[1])
    begin = "CREATE TABLE IF NOT EXISTS" + tablename + " ("
    sql = begin + cols[2:] + ") "
    try:
        # conn = MySQLdb.connect(host, user, pwd, dbname)
        # cursor = conn.cursor()
        cursor.execute(sql)
        print "Created table: ", tablename
        cursor.close()
        conn.close()
    except MySQLdb.Error as e:
        print 'Error: {} | Error code: {}'.format(e[1], e[0])
        cursor.close()
        conn.close()

def insert_data(csvpath, csv_file, dbname, insert_str, host, user, pwd):
    '''
    insert = "INSERT INTO {0} (unixtime, lat, lon, crs, spd, MMSI, SHIPNAME)
    VALUES (%s, %s, %s, %s, %s, %s, %s)".format(table)
    insert_data('csv/', 'aisdata.csv', dbname, insert, host, user, pwd)
    :param csvpath:
    :param csv_file:
    :param dbname:
    :param insert_str:
    :param host:
    :param user:
    :param pwd:
    :return:
    '''

    conn = create_connection(host, user, pwd, dbname)
    cursor = conn.cursor()

    try:
        # conn = MySQLdb.connect(host, user, pwd, dbname)
        # cursor = conn.cursor()
        with open(os.path.join(csvpath, csv_file), 'r') as f:
            reader = csv.reader(f)
            reader.next() #to pop the header
            for line in reader:
                cursor.execute(insert_str, line)
            conn.commit()
        print "Great success!"
        cursor.close()
        conn.close()
    except MySQLdb.Error as e:
        print 'Error: {} | Error code: {}'.format(e[1], e[0])'
        cursor.close()
        conn.close()


def complete_command(host, user, pwd, sql, dbname):
    conn = create_connection(host, user, pwd, sql, dbname):
    cursor = conn.cursor()

    try:
        print "Cursor created"
        cursor = cursor.execute(sql)
        list_of_tuples = cursor.fetchall()
        print "Command Executed"
    except MySQLdb.Error as e:
        print "Command not executed.\nError Message: {}\nexiting...".format(e)
        cursor.close()
        conn.close()
        sys.exit(1)
    list_of_tuples = list(list_of_tuples)

    return list_of_tuples