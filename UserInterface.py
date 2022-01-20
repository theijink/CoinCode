from CoinCode.key import pkey, skey
from CoinCode.CoinCode import client
import tkinter as tk

class window(tk.Tk):
    def __init__(self):
        super().__init__()
        ## create api connection
        self.client=self.login()
        ## settings for data aquisition
        self.base='EUR'
        self.ignore=['', '', '', '', '', '']
        self.interval='5m'
        self.period='1 day ago UTC'
        ## 
        self.markets=self.client.get_markets(self.base)
        self.datalist=self.create_datalist()
        #self.market_list()
        print(self.markets)
    
    def login(self):
        return client(api_key=pkey, api_secret=skey)
    
    def market_list(self):
        popup=tk.Toplevel(self)
        popup.title("market list")
        grid={'row':0, 'col':0}
        for sym in self.markets:
            tk.Label(text=sym).grid(row=grid['row'], column=0)
            grid['row']+=1
    
    def create_datalist(self):
        datalist={}
        for sym in self.markets:
            datalist[sym]={'otime':[], 'open':[], 'close':[], 'ctime':[]}
        return datalist

    def data_aquisition():
        pass



if __name__=="__main__":
    app=window()
    app.mainloop()