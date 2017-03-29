#!/usr/bin/python

#this is the name of DB
DB_name = "bitmexDb"

#host and port
host ="localhost"
port =27017

#you can add any type here
static_Type = {"static","normal"}

#you can add another categories here
categories = {"market_depth","recent_trades"}

# you can add another element here
# elemet is a tuple of ("ele_name","type_name")
# type_value shoud on of the types that exist in "static_Type" array
elements = {("size","normal"),("tickDirection","static"),("side","static"),("grossValue","normal"),("foreignNotional","normal"),("price","normal"),("trdMatchID","normal"),("homeNotional","normal"),("askSize","normal"),("level","static"),("bidPrice","normal"),("bidSize","normal"),("askPrice","normal")}
