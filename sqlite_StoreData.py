#!/usr/bin/python
import sqlite3
import Init_Data as db

flage = True
con = ""
#return Connction
def __get_connection():
    global flage
    global con
    if flage:
        con = sqlite3.connect("DataBases/"+db.DB_name+".db")
        flage=False
        return con
    else:
        return con


#get type id such as  Static --> 1  #Done
def __get_type_id(type):
    con = __get_connection()
    type_id = con.execute("SELECT id FROM type WHERE type_name=\'" + type + "\';")
    try:
        type_id = type_id.fetchone()[0]
    except Exception as e:
        #if not found , will store it
        con.execute("INSERT INTO type (type_name ) VALUES (\'" + type + "\');")
        con.commit()
        type_id = con.execute("SELECT MAX(id) FROM type;")
        type_id = type_id.fetchone()[0]
    return type_id


#return category id     #done
def __get_category_id(category_name):
    con = __get_connection()
    category_id = con.execute("SELECT id FROM categories WHERE name=\'" + category_name + "\';")
    try:
        category_id = category_id.fetchone()[0]
    except Exception as e:
        #if not found , will store it
        con.execute("INSERT INTO categories (name ) VALUES (\'" + category_name + "\');")
        con.commit()
        category_id = con.execute("SELECT MAX(id) FROM categories;")
        #to fetch id
        category_id = category_id.fetchone()[0]
    return category_id




#get category element id     #done
def __get_category_element_id(category_id,element_id):
    con = __get_connection()
    cat_ele_id = con.execute("SELECT id FROM category_elements WHERE category_id=" + str(category_id) + " AND element_id="+str(element_id)+";")
    try:
        cat_ele_id = cat_ele_id.fetchone()[0]
    except Exception as e:
        #if not found , will store it
        con.execute("INSERT INTO category_elements (category_id,element_id) VALUES ("+str(category_id)+","+str(element_id)+ ");")
        con.commit()
        cat_ele_id = con.execute("SELECT MAX(id) FROM category_elements;")
        cat_ele_id = cat_ele_id.fetchone()[0]
    return cat_ele_id
#print __get_category_element_id(category_id=1,element_id=2)

#                       #done
def __get_TimeStamp_id(timeStamp):
    con = __get_connection()
    timeStamp_id = con.execute("SELECT id FROM time_stamp WHERE time_stamp=\'" + timeStamp + "\';")
    try:
        timeStamp_id = timeStamp_id.fetchone()[0]
    except Exception as e:
        con.execute("INSERT INTO time_stamp (time_stamp ) VALUES (\'" + timeStamp + "\');")
        con.commit()
        timeStamp_id = con.execute("SELECT MAX(id) FROM time_stamp;")
        timeStamp_id = timeStamp_id.fetchone()[0]
    return timeStamp_id


#                    #done
def __get_Symbol_id(symbol):
    con = __get_connection()
    symble_id = con.execute("SELECT id FROM symbols WHERE symbol=\'" + symbol + "\';")
    try:
        symble_id = symble_id.fetchone()[0]
    except Exception as e:
        con.execute("INSERT INTO symbols (symbol ) VALUES (\'" + symbol + "\');")
        con.commit()
        symble_id = con.execute("SELECT MAX(id) FROM symbols ;")
        symble_id = symble_id.fetchone()[0]
    return symble_id


#to get id of spacefic time_stamp_id and symbol_id  #done
def __get_main_data_id(timestamp_id,symbol_id):
    con = __get_connection()
    main_data_id = con.execute("SELECT id FROM main_data WHERE time_stamp_id=" + str(timestamp_id) + " AND symbol_id="+str(symbol_id)+";")
    try:
        main_data_id = main_data_id.fetchone()[0]
    except Exception as e:
        #if not found , will store it
        con.execute("INSERT INTO main_data (time_stamp_id,symbol_id) VALUES ("+str(timestamp_id)+","+str(symbol_id)+ ");")
        con.commit()
        main_data_id = con.execute("SELECT MAX(id) FROM main_data;")
        main_data_id = main_data_id.fetchone()[0]
    return main_data_id


# to get static value id     #done
def ____get_static_value_id(element_id,value):
    con = __get_connection()
    #if value was number
    try:
        static_value_id = con.execute("SELECT id FROM static_values WHERE element_id=" + str(element_id) + " AND value="+str(value)+";")
    #if value was string
    except Exception as e:
        static_value_id = con.execute("SELECT id FROM static_values WHERE element_id=" + str(element_id) + " AND value=\'"+str(value)+"\';")
    try:
        static_value_id = static_value_id.fetchone()[0]
    except Exception as e:
        #if not found , will store it
        try:
            #if value was number
           con.execute("INSERT INTO static_values (element_id,value) VALUES ("+str(element_id)+","+str(value)+ ");")
        except Exception as ee:
           #if value was string
           con.execute("INSERT INTO static_values (element_id,value) VALUES ("+str(element_id)+",\'"+str(value)+ "\');")
        con.commit()
        static_value_id = con.execute("SELECT MAX(id) FROM static_values;")
        static_value_id = static_value_id.fetchone()[0]
    return static_value_id



# get element id      #Done
def __get_element_id(element_name):
    con = __get_connection()
    element = con.execute("SELECT id,type_id FROM element WHERE element_name=\'" + element_name + "\';")
    try:
        # make tuple of (element_id,type_id)
        element = (element.fetchall()[0])
    except Exception as e:
        #if element not exist
        #get normal id
        type_id = __get_type_id(type="normal")
        #store element in elment table as normal type
        con.execute("INSERT INTO element (element_name,type_id) VALUES (\'" + element_name + "\',"+str(type_id)+");")
        con.commit()
        element = con.execute("SELECT id,type_id FROM element WHERE element_name=\'" + element_name + "\';")
        element = (element.fetchall()[0])
    return element

#global variable
timestamp_id=0
symbol_id=0


def __get_init_element_dectionary(depth):
    ele_ids = {}
    global timestamp_id
    global symbol_id
    for one_depth in depth:
        #becouse TimeStamp and Symbol are main_data in all
        if one_depth != "timestamp" and one_depth != "symbol":
            #to get element id from DB
            ele_id = __get_element_id(element_name=one_depth)
            #to store element_id and type_id
            ele_ids[one_depth]=(ele_id)
        #check if this element is a TimeStamp
        elif one_depth == "timestamp":
                timestamp_id = __get_TimeStamp_id(timeStamp=depth[one_depth])
        #check if this element is a TimeStamp
        elif one_depth == "symbol":
                symbol_id = __get_Symbol_id(symbol=depth[one_depth])
    return ele_ids




# to store market_depth    #Done
def store_market_depth(market_depth,category):
    global timestamp_id
    global symbol_id
    #open connection
    con = __get_connection()
    depth = market_depth[0]
    #this dictionary have element and his ID
    ele_ids = __get_init_element_dectionary(depth=depth)
    #get main data id
    main_data_id = __get_main_data_id(timestamp_id=timestamp_id,symbol_id=symbol_id)
    #to get market_depth_id
    category_id = __get_category_id(category_name=category);
    #this loop to store real data in tables Real_Static_Data and Real_Normal_Data
    for one_depth in market_depth:
        con.execute("INSERT INTO data_link (main_data_id) VALUES ("+str(main_data_id)+");")
        con.commit()
        last_link_id = con.execute("SELECT MAX(id) FROM data_link").fetchone()[0]
        for ele in one_depth:
            if ele != "timestamp" and ele != "symbol":
                # print ele , "  " ,one_depth[i]
                cat_ele_id = __get_category_element_id(category_id=category_id,element_id=ele_ids[ele][0])
                #get element type id
                ele_type_id = ele_ids[ele][1]
                #static element
                if ele_type_id==1:
                    #get static value id
                    static_value_id = ____get_static_value_id(element_id=ele_ids[ele][0],value=one_depth[ele])
                    con.execute("INSERT INTO real_static_data (data_link_id,category_element_id,static_value_id) VALUES ("+str(last_link_id)+","+str(cat_ele_id)+","+str(static_value_id)+");")
                    con.commit()
                #normal element
                elif ele_type_id ==2:
                    con.execute("INSERT INTO real_normal_data (category_element_id,value,data_link_id) VALUES ("+str(cat_ele_id)+","+"\'"+str(one_depth[ele])+"\',"+str(last_link_id)+");")
                    con.commit()
    con.close()
    global flage
    flage=True
    print "data_Stored #Done"





#global variable used to check if this recent_trade is sotred before
trdMatchID=""
#to store_recent_trades
def store_recent_trades(recent_trades,category):
    global trdMatchID
    if recent_trades[0]["trdMatchID"] == trdMatchID:
       print "data_IS    Stored #Done"
    else:
       trdMatchID=recent_trades[0]["trdMatchID"]
       store_market_depth(market_depth=recent_trades,category=category)



#return array that have category (cat_ele_id,element_name) #Done
def __get_category_elements_ids(category_id):
    con = __get_connection()
    ids=[]
    fetch = con.execute("SELECT id,element_id FROM category_elements WHERE category_id="+str(category_id)+";")
    id=0
    for cat_ele in fetch:
        id=cat_ele[0]
        element_name=con.execute("SELECT element_name FROM element WHERE id="+str(cat_ele[1])+";").fetchone()[0]
        ids.append((id,element_name))
    return ids


def __get_static_value(static_id):
    con = __get_connection()
    return con.execute("SELECT value FROM static_values WHERE id="+str(static_id)+";").fetchone()[0]



import copy

#retrive data of market_depth
def retrive_market_depth(TimeStamp,symbol,category_name):
    con = __get_connection()
    data_set =[]
    category_id = __get_category_id(category_name=category_name)
    #[(cat_ele_id,element_name)]
    element = __get_category_elements_ids(category_id=category_id)
    timestamp_id = __get_TimeStamp_id(timeStamp=TimeStamp)
    symbol_id = __get_Symbol_id(symbol=symbol)
    main_data_id = __get_main_data_id(timestamp_id=timestamp_id,symbol_id=symbol_id)
    print main_data_id
    links_ids = con.execute("SELECT id FROM data_link WHERE main_data_id="+str(main_data_id)+";")
    for link_id in links_ids:
        data = []
        #(cat_ele_id,value)
        normal_element = con.execute("SELECT category_element_id,value FROM real_normal_data WHERE data_link_id="+str(link_id[0])+";")
        normal_element = normal_element.fetchall()
        if element[0][0] == normal_element[0][0]:
            i=0
            temporary_data = copy.copy(element)
            for normal in normal_element:
                for ele in temporary_data:
                    if normal[0]==ele[0]:
                        data.append((ele[1],normal[1]))
                        break
            #(cat_ele_id,static_value_id)
            static_elements_ids = con.execute("SELECT category_element_id,static_value_id FROM real_static_data WHERE data_link_id="+str(link_id[0])+";")
            temporary_data = copy.copy(element)
            for static in static_elements_ids:
                for ele in temporary_data:
                    if(static[0]==ele[0]):
                        static_value = __get_static_value(static_id=static[1])
                        data.append((ele[1],static_value))
                        break
            data.append(("timestamp",TimeStamp))
            data.append(("symbol",symbol))
            data_set.append(data)
    con.close()
    global flage
    flage=True
    return data_set



def retrive_recent_trades(TimeStamp,symbol,category_name):
    return retrive_market_depth(TimeStamp=TimeStamp,symbol=symbol,category_name="recent_trades")




def store_funds(funds , sympole):
    print 1

def store_ticker(ticker , sympole):
    print 0
