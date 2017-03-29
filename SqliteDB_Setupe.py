#!/usr/bin/python
import os
import sqlite3
import Init_Data as db

DB_name = db.DB_name

def Creat_Tables(DB_name):
    #it will created inside DataBases/ folder
    #sqlite setupe
    os.system('mkdir DataBases')

    #open sqlite_bitmex connection if exitst or create it and open connection if not exist
    con =  sqlite3.connect('DataBases/'+ DB_name +'.db')
    #create tables where will store the data

    #create Categories table
    con.execute("CREATE TABLE IF NOT EXISTS categories (id INTEGER PRIMARY KEY AUTOINCREMENT , name TEXT NOT NULL);")
    #create Type table
    con.execute("CREATE TABLE IF NOT EXISTS type (id INTEGER PRIMARY KEY AUTOINCREMENT , type_name TEXT NOT NULL);")
    #create Elements table
    con.execute("CREATE TABLE IF NOT EXISTS element (id INTEGER PRIMARY KEY AUTOINCREMENT , element_name TEXT NOT NULL,type_id INT NOT NULL,FOREIGN KEY (type_id) REFERENCES type(id));")
    #create Category_Elmentes table
    con.execute("CREATE TABLE IF NOT EXISTS category_elements (id INTEGER PRIMARY KEY AUTOINCREMENT , element_id INT NOT NULL ,category_id INT NOT NULL, FOREIGN KEY (category_id) REFERENCES categories(id), FOREIGN KEY (element_id) REFERENCES element(id));")
    #create Time_Stamp table
    con.execute("CREATE TABLE IF NOT EXISTS time_stamp (id INTEGER PRIMARY KEY AUTOINCREMENT , time_stamp TEXT NOT NULL);")
    #create symbols table
    con.execute("CREATE TABLE IF NOT EXISTS symbols (id INTEGER PRIMARY KEY AUTOINCREMENT , symbol TEXT NOT NULL);")
    #creat Main_Data table
    con.execute("CREATE TABLE IF NOT EXISTS main_data (id INTEGER PRIMARY KEY AUTOINCREMENT , time_stamp_id INT NOT NULL ,symbol_id INT NOT NULL, FOREIGN KEY (time_stamp_id) REFERENCES time_stamp(id), FOREIGN KEY (symbol_id) REFERENCES Symble(id));")
    #creat Static_Values table
    con.execute("CREATE TABLE IF NOT EXISTS static_values (id INTEGER PRIMARY KEY AUTOINCREMENT , element_id INT NOT NULL,value TEXT,FOREIGN KEY (element_id) REFERENCES element(id));")
    #create data_Link table
    con.execute("CREATE TABLE IF NOT EXISTS data_link (id INTEGER PRIMARY KEY AUTOINCREMENT , main_data_id INT NOT NULL , FOREIGN KEY (main_data_id) REFERENCES main_data(id));")
    #create Real_Normal_Data
    con.execute("CREATE TABLE IF NOT EXISTS real_normal_data (category_element_id INT NOT NULL ,value TEXT NOT NULL,data_link_id INT NOT NULL , FOREIGN KEY (data_link_id) REFERENCES data_link(id), FOREIGN KEY (category_element_id) REFERENCES category_elements(id));")
    #create Real_Static_Data
    con.execute("CREATE TABLE IF NOT EXISTS real_static_data (category_element_id INT NOT NULL ,static_value_id INT NOT NULL,data_link_id INT NOT NULL, FOREIGN KEY (data_link_id) REFERENCES data_link(id), FOREIGN KEY (category_element_id) REFERENCES category_elements(id),FOREIGN KEY (static_value_id) REFERENCES static_values(id));")

    #close connection
    con.close()
    print "create sqlite database "+DB_name+"  #Done"


def Store_init_Data(DB_name):
    con =  sqlite3.connect('DataBases/'+ DB_name +'.db')
    #this to store static types
    for valu in db.static_Type:
    #Add some static info
        con.execute("INSERT INTO type (type_name) VALUES (\'"+ valu + "\');")
        con.commit()


    #this to store categoury
    for valu in db.categories:
        #Add some static info
        con.execute("INSERT INTO categories (name) VALUES (\'"+ valu + "\');")
        con.commit()

    #this to store elements
    for (ele,type) in db.elements:
        type_id = con.execute("SELECT id FROM type WHERE type_name=\'" + type + "\';")
        type_id = type_id.fetchone()[0]
        con.execute("INSERT INTO element (element_name , type_id) VALUES (\'" + ele + "\'" +","+str(type_id)+");")
        con.commit()

    #close connection
    con.close()
    print "store init data in"+DB_name+" #Done"


Creat_Tables(DB_name=DB_name)
Store_init_Data(DB_name=DB_name)
