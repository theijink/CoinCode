import binance
import tkinter as tk

class Account():
    def __init__(self):
        self.account={'username':tk.StringVar(), 'password':tk.StringVar()}
        self.account['username'].set('API KEY')
        self.account['password'].set('API SECRET')
        #self.client=binance.Client()
        

    def login(self):
        self.root=tk.Tk()
        self.root.title("API credentials")
        self.lab1=tk.Label(self.root, text="username").grid(row=0, column=0)
        self.ent1=tk.Entry(self.root, textvariable=self.account['username']).grid(row=0, column=1)
        self.lab2=tk.Label(self.root, text='password').grid(row=1, column=0)
        self.ent2=tk.Entry(self.root, textvariable=self.account['password']).grid(row=1, column=1)
        self.root.mainloop()
        self.username=self.account['username'].get()
        self.password=self.account['password'].get()        
        return "logged in \n{}\n{}".format(self.username, self.password)

    def buy():
        return "bought"

    def sell():
        return "sold"

    def get_orders():
        return "order list"

