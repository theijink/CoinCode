import binance
import tkinter

class Account():
    def __init__(self, username, password):
        self.username=username
        self.password=password
        self.client=binance.Client()
        

    def login():
        return "logged in"

    def buy():
        return "bought"

    def sell():
        return "sold"

    def get_orders():
        return "order list"

