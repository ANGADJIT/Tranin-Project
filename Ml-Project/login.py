import tkinter as tk
from tkinter.font import Font
from  database import Database
from admin_pannel import AdminPanel
import tkinter.messagebox as mb
from PIL import Image,ImageTk

class Login:

    #* login method
    def login(self):

        if self.id.get() == '' or self.password.get() == '':
            mb.showerror('Login',message='User and password are required')
            return

        check,admin_name = self.db.login(self.id.get(),self.password.get())

        if(check == None):
            mb.showerror('Login',message='You\'re not authorized')

        elif(check):
            mb.showinfo('Login',message='Login succesfull')
            self.root.destroy()

            AdminPanel()
           
        
        else:
            mb.showerror(title='Login',message='Something went wrong!')

    def __init__(self):

        self.db = Database()

        self.root = tk.Tk() #* root widget
        self.root.geometry('900x600')
        self.root.minsize(300,200)
        self.root.maxsize(900,600)
        self.root.iconbitmap('images/tracker.ico')
        self.root.title('Covid Vaccine Tracker : ')

        #* creating image obj and adding to window
        image = ImageTk.PhotoImage(Image.open('images/login.png').resize(size=(400,600)))

        #* login box
        self.loginBox = tk.PanedWindow(self.root,background='#afeaed',height=400,width=250)
        self.loginBox.pack(side=tk.LEFT,expand=True,fill='both')

        #* adding widgets to login box
        tk.Label(self.loginBox,font=Font(family='Arial',size=19,weight='normal',slant='italic'),text='Login',foreground='black',background='#afeaed').pack(pady=110)

        tk.Label(self.loginBox,font=Font(family='Arial',size=15,weight='normal',slant='italic'),text='user',foreground='black',background='#afeaed').pack(padx=25,anchor=tk.W)

        self.id = tk.Entry(self.loginBox,font=Font(size=14),foreground='black',
        width=40,
        background='white') 
        self.id.pack(anchor=tk.W,padx=25,pady=10)

        tk.Label(self.loginBox,font=Font(family='Arial',size=15,weight='normal',slant='italic'),text='Password',foreground='black',background='#afeaed').pack(padx=25,anchor=tk.W)

        self.password = tk.Entry(self.loginBox,show='*',font=Font(size=14),foreground='black',
        width=40,
        background='white') 
        self.password.pack(anchor=tk.W,padx=25,pady=10)

        tk.Button(self.loginBox,text='Continue',command=self.login,font=Font(size=16,weight='bold'),background='#afeaed',foreground='black',borderwidth=.7).pack(side='top',pady=35)
        
        tk.Label(image=image).pack(side=tk.RIGHT)
        
        self.root.mainloop() #* event loop

Login()