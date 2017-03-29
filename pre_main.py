from bitmex_websocket import BitMEXWebsocket
import logging
from time import sleep


# Basic use of websocket.
def run():
    logger = setup_logger()

    #symbole
    symbol = "XBTUSD"

    # Instantiating the WS will make it connect. Be sure to add an auth method. You can use login/password
    # or api_key/api_secret.
    ws = BitMEXWebsocket(endpoint="https://testnet.bitmex.com/api/v1", symbol=symbol,
                         login=None, password=None, api_key=None, api_secret=None)

    logger.info("Instrument data: %s" % ws.get_instrument())


    # to save in sqlite Database remove the comming comments
    # import sqlite_StoreData as Sstore
    # # Run forever
    # while(ws.ws.sock.connected):
    #     ticker = ws.get_ticker()
    #     #logger.info("Ticker : %s" % ticker)
    #     funds = ws.funds()
    #     #logger.info("Funds: %s" % funds)
    #     market_depth = ws.market_depth()
    #     #logger.info("Market Depth: %s" % market_depth)
    #     #store market_depth in Sqlite DB
    #     Sstore.store_market_depth(market_depth=market_depth,category="market_depth")
    #     recent_trades = ws.recent_trades()
    #     #logger.info("Recent Trades: %s\n\n" % recent_trades)
    #     #store recent_trades in mongo DB
    #     Sstore.store_recent_trades(recent_trades=recent_trades,category="recent_trades")
    #     sleep(10)


    # # to store in MongoDB remove the comming comments
    # import Mongo_StoreData as Mstore
    # # Run forever
    # while(ws.ws.sock.connected):
    #     ticker = ws.get_ticker()
    #     logger.info("Ticker : %s" % ticker)
    #     funds = ws.funds()
    #     logger.info("Funds: %s" % funds)
    #     market_depth = ws.market_depth()
    #     logger.info("Market Depth: %s" % market_depth)
    #     #store market_depth in mongo DB
    #     Mstore.store_data(category_name="market_depth",ws=market_depth)
    #     recent_trades = ws.recent_trades()
    #     logger.info("Recent Trades: %s\n\n" % recent_trades)
    #     #store recent_trades in mongo DB
    #     Mstore.store_data(category_name="recent_trades",ws=recent_trades)
    #     sleep(10)


def setup_logger():
    # Prints logger info to terminal
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)  # Change this to DEBUG if you want a lot more info
    ch = logging.StreamHandler()
    # create formatter
    formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
    # add formatter to ch
    ch.setFormatter(formatter)
    logger.addHandler(ch)
    return logger


if __name__ == "__main__":
    run()
