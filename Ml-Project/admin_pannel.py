from datetime import date
import tkinter.messagebox as mb
from database import Database
import tkinter as tk
from tkcalendar import DateEntry
from tkinter.ttk import Combobox
from tkinter.font import Font
from tkinter.ttk import Treeview

class AdminPanel:

    def search(self):

        if self.hospital.get() == 'Select center':
            mb.showerror('AdminPanel','Requirement unsatisfied')
            return

        self.table.delete(*self.table.get_children())
        result = list(self.db.getHospitalDetails(self.hospital.get(),str(self.date.get_date())))
        data = list(result[0]) + [result[1]]

        self.table.insert("",'end',values=tuple(data))
    
    def __init__(self):

        #* database instance
        self.db = Database()

        self.root = tk.Tk() #* root widget
        self.root.title('Admin Pannel')
        self.root.iconbitmap('images/admin.ico')
        self.root.minsize(900,600)
        self.root.maxsize(900,600)

        #* frame 1
        self.frame1 = tk.PanedWindow(self.root,height=50,bg='#afeaed')
        self.frame1.pack(side='top',fill='x')

        #* adding widgets to frame1
        self.hospital = tk.StringVar()
        self.hospital.set('Select center')
        self.selectHospital = Combobox(self.frame1,state='readonly',textvariable=self.hospital,width=35)
        self.selectHospital.grid(row=0,column=0,padx=10,pady=10)

        self.date = DateEntry(self.frame1,state='readonly',width=35,bg="darkblue",fg="white",year=2021)
        self.date._set_text('Select date')
        self.date.grid(row=0,column=1,padx=10,pady=10)

        tk.Button(self.frame1,text='Submit',font=Font(size=10,weight='bold'),
        command=self.search,
        width=35,
        background='#afeaed',foreground='black',borderwidth=.7).grid(row=0,column=2,padx=10,pady=10)

        #* frame 2
        self.frame2 = tk.PanedWindow(self.root)
        self.frame2.pack(side='top',fill='both')

        #* adding table to frame 2
        self.table = Treeview(self.frame2,selectmode='browse')
        self.table.pack(side='top',fill='both',padx=10,pady=20)

        #* adding columns and heading to it
        self.selectHospital['values'] = self.db.returnHospitalsName()
        self.table['columns'] = ('1','2','3','4','5')
        self.table['show'] = 'headings'

        self.table.column('1',width=50,anchor='c')
        self.table.column('2',width=50,anchor='c')
        self.table.column('3',width=50,anchor='c')
        self.table.column('4',width=50,anchor='c')
        self.table.column('5',width=50,anchor='c')

        self.table.heading('1',text='Id')
        self.table.heading('2',text='Name')
        self.table.heading('3',text='Location')
        self.table.heading('4',text='Type')
        self.table.heading('5',text='Total vaccine count')

        self.root.mainloop()

