import binance
import tkinter

class Account():
    def __init__(self, username, password):
        self.username=username
        self.password=password
        #self.client=binance.Client()
        

    def login(self):
        return "logged in \n{}\n{}".format(self.username, self.password)

    def buy():
        return "bought"

    def sell():
        return "sold"

    def get_orders():
        return "order list"

