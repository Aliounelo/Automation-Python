######################################################################################
#  Author : Alioune LO
#  Mail :   aliounelo2206@outlook.com
#  Github : aliounelo
#######################################################################################

import os
import pandas as pd
import mysql.connector
from mysql.connector import Error

filename_= os.getcwd() + '/en_US_frontend.json'
#print(filename_)
read_file = pd.read_json(filename_ , typ='dictionary')
print(read_file)

nfilename_ = filename_.split('.')[0]+ '.csv'
#print(nfilename_)

read_file.to_csv (f'{nfilename_}', index = True, sep= ';' , header=True)
empdata = pd.read_csv(f'{nfilename_}',index_col=False, delimiter = ';')

#print(empdata)
#print(empdata.fillna(0))
ctr = 0
try : 
    mydb = mysql.connector.connect(
    host='127.0.0.1',
    user='root',
    password='',
    database ='db_JSON_CSV'
    )
    if mydb.is_connected() :
        mycursor = mydb.cursor()
        mycursor.execute("select database();")
        record = mycursor.fetchone()
        print("connected to database : ",record)
        for i,row in empdata.fillna(0).iterrows() :
            ctr += 1
            #-- Add or remove the number of string into Values depending of your number of values.
            sql = "INSERT into db_JSON_CSV.JSON_TO_CSV Values (%s, %s)"
            mycursor.execute(sql, tuple(row))
            print("Record inserted")
            mydb.commit()
        print(ctr,"Record(s) inserted")
except Error as e : 
    print("Error while connecting to MySQL", e)
 
