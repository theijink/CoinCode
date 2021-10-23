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


class Manage():
   
    def get_orders():
        return "order list"

