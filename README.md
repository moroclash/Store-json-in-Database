# Store **BitMex api** for realtime data in DB

###### you can store it in **MonogDB** or **Sqlite**

###### this Program work on Linux

## prerequisite :
* download **Python Adapter for BitMEX Realtime Data**
get it from [here](https://github.com/BitMEX/api-connectors/tree/master/official-ws/python)
* setup it


## file explain :
1. **Schema.png** :- it is DB schema for retional DB.
2. **Init_Data.py** :- Initial data this have shared data such as **DB_name** and some data used to setup sqliteDB.
3. **Mongo_StoreData.py** :- have function that used to **Store** and **Retrieve** from MongoDB.
4. **SqliteDB_Setupe.py** :- have the **sql query** that use to build DB in first time .
5. **sqlite_StoreData.py** :- have function that used to **Store** and **Retrieve** from Sqlite.
6. **pre_main** :- that have updated code that will replaced with **main.py** file.


###### you can change **DataBase_name** , **host** and **port** in **Init_Data.py** file, and you add more **"categories"** and add more **elements** to any category and change and specify his type as **"Static"** or **"Dinamic"**

## How to use :
* Clone this **repository**
```
git clone https://github.com/moroclash/Store-json-in-Database.git
```
* replace local **main.py** with **pre_main.py** run this command
```
cat pre_main.py >> main.py
```
* you shoud put your **mail** and **password** to can connect with **API** , put them in file **main.py**
> login=None, password=None     #line 16 in main.py file

* to store Data in DB
  - **MongoDB** :
    1. check that you have **MongoDB** on your PC , install it if not exist
    2. go to **main.py** file and remove this command symbol from **ln 40** to **ln 56**
    ># to store in MongoDB remove the comming comments
     import Mongo_StoreData as Mstore
     # Run forever
     while(ws.ws.sock.connected):
         ticker = ws.get_ticker()
         logger.info("Ticker : %s" % ticker)
         funds = ws.funds()
         logger.info("Funds: %s" % funds)
         market_depth = ws.market_depth()
         logger.info("Market Depth: %s" % market_depth)
         #store market_depth in mongo DB
         Mstore.store_data(category_name="market_depth",ws=market_depth)
         recent_trades = ws.recent_trades()
         logger.info("Recent Trades: %s\n\n" % recent_trades)
         #store recent_trades in mongo DB
         Mstore.store_data(category_name="recent_trades",ws=recent_trades)
         sleep(10)

      3. Run program
      ```
      python main.py
      ```
      4. it will store market_depth ans recent_trades in DB
  - **Sqlite** :
    1. you should run **SqliteDB_Setupe.py** file at first time to create DataBase
    2. go to **main.py** file and remove this command symbol from **ln 21** to **ln 37**
    ># to save in sqlite Database remove the comming comments
     import sqlite_StoreData as Sstore
     # Run forever
     while(ws.ws.sock.connected):
         ticker = ws.get_ticker()
         #logger.info("Ticker : %s" % ticker)
         funds = ws.funds()
         #logger.info("Funds: %s" % funds)
         market_depth = ws.market_depth()
         #logger.info("Market Depth: %s" % market_depth)
         #store market_depth in Sqlite DB
         Sstore.store_market_depth(market_depth=market_depth,category="market_depth")
         recent_trades = ws.recent_trades()
         #logger.info("Recent Trades: %s\n\n" % recent_trades)
         #store recent_trades in mongo DB
         Sstore.store_recent_trades(recent_trades=recent_trades,category="recent_trades")
         sleep(10)

      3. Run program
      ```
      python main.py
      ```
      4. it will store market_depth ans recent_trades in **sqliteDB**


## MongoDB VS sqliteDB :
* MongoDB :
###### have high performance and high speed it will store data even **API** change his Data format in runtime , but it will have duplicated data.
* Sqlite :
###### have less performance and speed than MongoDB , but it is very efficient in using memory space because it don't have any duplicated data and it will store data even **API** change his Data format in runtime .
