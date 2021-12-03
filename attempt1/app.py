from coincode import Manage, Account, Trade
import tkinter as tk
from tkinter import Toplevel, ttk
from time import sleep

class mainwindow(tk.Tk):
    def __init__(self):
        super().__init__()
        super().geometry("480x360")
        super().title("Coin Code")
        self.btn_login=tk.Button(self, text="log in", command=lambda:self.verify())
        self.btn_login.grid(row=0, column=0, columnspan=4)
    
    def verify(self):
        popup=tk.Toplevel()
        popup.title("API credentials")
        self.account={'username':tk.StringVar(), 'password':tk.StringVar()}
        self.account['username'].set('API KEY')
        self.account['password'].set('API SECRET')
        self.lab1=tk.Label(popup, text="username: ")
        self.lab1.grid(row=0, column=0)
        self.ent1=tk.Entry(popup, textvariable=self.account['username'])
        self.ent1.grid(row=0, column=1)
        self.lab2=tk.Label(popup, text='password: ')
        self.lab2.grid(row=1, column=0)
        self.ent2=tk.Entry(popup, textvariable=self.account['password'])
        self.ent2.grid(row=1, column=1)
        self.btn1=tk.Button(popup, text="Commit", command=lambda:[self.return_client(), popup.destroy(), self.initialize()])
        self.btn1.grid(row=2, column=3)

    def return_client(self):
        self.username=self.account['username'].get()
        self.password=self.account['password'].get()
        self.binance_client=Account.login(self.username, self.password)        
        return self.binance_client
    
    def initialize(self):
        ## function buttons
        i=5
        btn_grapher=tk.Button(self, text="Grapher", command=lambda:Grapher())
        btn_grapher.grid(row=i, column=0, columnspan=4, sticky='nsew')
        ## analysis buttons
        i=6
        btn_grapher=tk.Button(self, text="Analysis", command=lambda:Analysis())
        btn_grapher.grid(row=i, column=0, columnspan=4, sticky='nsew')
        ## wallet title
        i=10
        lab_wallet=tk.Label(self, text="Wallet", font=('Helvetica', '20', 'bold'))
        lab_wallet.grid(row=i, column=0, columnspan=4, sticky='w')
        i+=1
        ## header labels
        lab_asset=tk.Label(self, text="asset")
        lab_asset.grid(row=i, column=0)
        lab_free=tk.Label(self, text="free")
        lab_free.grid(row=i, column=1)
        lab_locked=tk.Label(self, text="locked")
        lab_locked.grid(row=i, column=2)
        lab_locked=tk.Label(self, text="worth")
        lab_locked.grid(row=i, column=3)            ## update wallet
        wallet=Account.wallet(self.binance_client)
        i+=1
            
        while True:
            i=12
            for coin in wallet:
                j=0
                for item in ['asset', 'free', 'locked']:
                    ## place value labels
                    lab=tk.Label(self, text=coin[item])
                    lab.grid(row=i, column=j)
                    j+=1
                for item in ['eur worth']:
                    lab=tk.Label(self, text="ticker")
                    lab.grid(row=i, column=j)
                    j+=1                    
                i+=1
            self.update()
            sleep(1)


class Grapher(tk.Toplevel):
    def __init__(self):
        tk.Toplevel.__init__(self)
        super().title('Grapher')

class Analysis(tk.Toplevel):
    def __init__(self):
        Toplevel.__init__(self)
        super().title('Technical Analysis')
        super().geometry('480x360')
        self.markets = Manage.get_all_markets(root.binance_client)
        self.market = tk.StringVar(value='')
        #self.market.set()
        self.choicelist = ttk.Combobox(self, textvariable=self.market, values=self.markets)
        self.choicelist.grid(row=0, column=0, sticky='nsew')
        self.choicelist.bind("<<ComboboxSelected>>", self.load_data())
        
    def load_data(self):
        self.trades = Account.get_orders(root.binance_client, self.market.get())
        for order in self.trades:
            print(order)



if __name__=="__main__":
    ## main application
    root=mainwindow()
    root.mainloop()