from coincode import Manage, Account, Trade
import tkinter as tk

class mainwindow(tk.Tk):
    def __init__(self):
        super().__init__()
        super().title("Coin Code")
        self.btn_login=tk.Button(self, text="log in", command=lambda:self.verify())
        self.btn_login.grid(row=0, column=1)
    
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
        self.btn1=tk.Button(popup, text="Commit", command=lambda:[self.return_client(), popup.destroy()])
        self.btn1.grid(row=2, column=3)

    def return_client(self):
        self.username=self.account['username'].get()
        self.password=self.account['password'].get()
        self.client=Account.login(self.username, self.password)        
        return self.client

if __name__=="__main__":
    ## main application
    root=mainwindow()
    root.mainloop()