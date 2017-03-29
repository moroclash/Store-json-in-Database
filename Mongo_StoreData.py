import Init_Data as init
from pymongo import MongoClient
import copy

#buffer
trdMatchID =""
def store_data(category_name,ws):
    global trdMatchID
    if category_name == "recent_trades":
        if trdMatchID == ws[0]['trdMatchID']:
            print "it stored"
        else:
            trdMatchID = ws[0]['trdMatchID']
            __store(category_name=category_name,ws=ws)
    else:
        __store(category_name=category_name,ws=ws)




def __store(category_name,ws):
    Client = ""
    # try:
    #connect with server
    Client = MongoClient(init.host,init.port)
    #connect with DB
    db = Client[init.DB_name]
    #get collection
    collection = db['data']
    timeStamp = ""
    symbol = ""
    #array of normal data
    real_data = []
    #to get static data
    for data in ws:
        one_data={}
        for d in data:
            if d =='timestamp':
               timeStamp = data[d]
            if d =='symbol':
                symbol = data[d]
            else:
                one_data[d]=data[d]
        real_data.append(one_data)
    #Preparation data
    data = {"category":category_name,
            "timestamp":timeStamp,
            "symbol":symbol,
            "data":real_data}
    #store data
    collection.insert_one(data)
    Client.close()
    print "Store ",category_name," in mongo done"
    # except Exception:
        #  print "check if your mongo server running and check host and port \"Init_Data\" file "


def retrive_data(category_name , timeStamp , symbol):
    Client=""
    try:
        Client = MongoClient()
        db = Client[init.DB_name]
        collection = db['data']
        real_data = collection.find_one({"timestamp":timeStamp})#{"category":category_name,"timestamp":timeStamp,"symbol":symbol})
        for data in real_data['data']:
            print "-----------------------------------------"
            print "category : " , category_name
            print "timeStamp : " , timeStamp
            print "symbol : "  , symbol
            for d in data:
                print  d ," : ", data[d]
        Client.close()
    except Exception:
         print "check if your mongo server running and check host and port \"Init_Data\" file "
