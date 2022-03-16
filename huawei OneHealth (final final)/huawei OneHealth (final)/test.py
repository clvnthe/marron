import mysql.connector

my_db = mysql.connector.connect(host="116.205.136.149",
                                port="3306",
                                user="root",
                                passwd="marron123!",
                                database="onehealth",
                                autocommit=True)
my_cursor = my_db.cursor()