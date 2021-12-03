from binance.client import Client

class Account():
    def __init__(self, username, password):
        self.client=Client(username, password)
        self.wallet=self.get_wallet(self.client)

    def get_wallet(self):
        pass

    def view_wallet(self):
        pass






if __name__=="__main__":
    username=("")#set('API KEY')
    password=("")#set('API SECRET')

    client=Account(username, password)







