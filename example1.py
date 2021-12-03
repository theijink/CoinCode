import tkinter as tk

class App(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        tk.Tk.wm_title(self, "title")
        ## frame container
        container=tk.Frame(self)
        container.grid(row=0, column=0, sticky='nsew')
        ## menubar
        self.menubar=tk.Menu(container)
        self.add_file_menu()
        ## add menubar to app
        tk.Tk.config(self, menu=self.menubar)
        ## frame handler
        self.frames={}
        for F in (HomePage, LoginPage, TradePage):
            frame = F(container, self)
            self.frames[F]=frame
            frame.grid(row=0, column=0, sticky='nsew')
        ## initial page
        self.show_frame(LoginPage)
        ## app icon
        #tk.Tk.iconbitmap(self, default="")
    
    def show_frame(self, cont):
        frame=self.frames[cont]
        frame.tkraise()

    def add_file_menu(self):
        ## filemenu
        filemenu=tk.Menu(self.menubar, tearoff=0)
        #filemenu.add_command(label="Open", command=lambda:print("Nothing to open"))
        #filemenu.add_command(label="Save", command=lambda:print("Nothing to save"))
        filemenu.add_separator()
        filemenu.add_command(label="Exit", command=lambda:quit())
        self.menubar.add_cascade(label="File", menu=filemenu)

    def add_navigate_menu(self):
        ## navigatemenu
        navigatemenu=tk.Menu(self.menubar, tearoff=1)
        navigatemenu.add_command(label="Login", command=lambda:self.show_frame(LoginPage))
        navigatemenu.add_separator()
        navigatemenu.add_command(label="Home", command=lambda:self.show_frame(HomePage))
        navigatemenu.add_command(label="Trade", command=lambda:self.show_frame(TradePage))
        self.menubar.add_cascade(label="Navigate", menu=navigatemenu)




class LoginPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.lab01=tk.Label(text="Login")
        self.lab01.grid(row=0, column=0)
        ## login button
        btn01=tk.Button(text="log in", command=lambda:self.arrange())
        btn01.grid(row=1, column=0, sticky='nsew')
    
    def arrange(self):
        app.add_navigate_menu()


class HomePage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.lab01=tk.Label(text="Home")
        self.lab01.grid(row=0, column=0)


class TradePage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.lab01=tk.Label(text="Trade")
        self.lab01.grid(row=0, column=0)

if __name__=="__main__":
    app=App()
    app.geometry("1280x720")
    app.mainloop()

