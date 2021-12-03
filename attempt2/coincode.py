from binance.client import Client

class Trade():

    def buy():
        return "bought"

    def sell():
        return "sold"



class Account():

    def login(username, password):
        client=Client(username, password)
        ## return api logged in client
        return client

    def wallet(client):
        wallet=[]
        info=client.get_account()
        for coin in info['balances']:
            if eval(coin['free'])>0 or eval(coin['locked'])>0:
                wallet.append({'asset':coin['asset'], 'free':coin['free'], 'locked':coin['locked']})
        return wallet
   
    def get_orders(client, market):
        info = client.get_account()
        my_trades = client.get_my_trades(symbol=market)
        return my_trades

class Manage():

    
    def get_all_markets(client):
        tickers = client.get_ticker()
        markets = [market['symbol'] for market in tickers]
        return markets
    






