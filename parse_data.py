#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar  3 12:33:35 2020

@author: janwillem
"""
import mysql.connector
from mysql.connector import Error
import time
from influxdb import InfluxDBClient
client = InfluxDBClient('64.227.64.221', 8086, 'admin', 'supersecretpassword', 'telegraf')

import json

def insert_CountLogs(logEntryId, Timestamp,RegisterId, Value, Name):
    
    try:
        connection = mysql.connector.connect(host='localhost',
                                             database='mydb',
                                             user='root',
                                             password='Welkom2012')
        cursor = connection.cursor()

        sql_insert_data = """INSERT INTO CountLogs (logEntryId, Timestamp, RegisterId, Value, Name) 
                          VALUES (%s, %s, %s, %s, %s) """
        data = (logEntryId, Timestamp, RegisterId, Value, Name)  
        cursor.execute(sql_insert_data, data)
        connection.commit()
        print("Record inserted successfully")
        
    except mysql.connector.Error as error:
        print("Failed to insert into MySQL table {}".format(error))
 
        
def insert_space(string, integer):
    return string[0:integer] + ' ' + string[integer:]

def parse_data():

    p = '10-3-2020.json'
    with open(p, 'r') as f:
        data = json.load(f)

    for log in data['CountLogs']:
        x = log['Counts']
        time = log['Timestamp'].replace('T', '')
        datetime = time.replace('Z', '')
        datum = insert_space(datetime, 10)
        #print("Timestamp: ", log['Timestamp'])
        print(datum)

        print("LogEntryId: ", log['LogEntryId'])
        #print(type(x))
        for i in range(len(x)):
            if x[i]['RegisterId'] == 0:                                             # People walking in 
                print("RegisterID: ", x[i]['RegisterId'])
                print("Aantal klanten binnengelopen: ", x[i]['Value'])              # Amount of people walked in
                value_0 = x[i]['Value']
                insert_CountLogs(log['LogEntryId'], datum, x[i]['RegisterId'], x[i]['Value'], x[i]['Name'])

            elif x[i]['RegisterId'] == 1:                                           # People walking out
                print("RegisterID: ", x[i]['RegisterId'])
                print("Aantal klanten weggelopen: ", x[i]['Value'])                 # Amount of people walked out
                value_1 = x[i]['Value']
                insert_CountLogs(log['LogEntryId'], datum, x[i]['RegisterId'], x[i]['Value'], x[i]['Name'])
                print("\n")
                
    
def main():
        
    parse_data()
    
if __name__ == "__main__":
    main()