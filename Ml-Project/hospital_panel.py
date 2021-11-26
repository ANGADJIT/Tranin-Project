from datetime import date
import tkinter.messagebox as mb
from database import Database
import tkinter as tk
from tkcalendar import DateEntry
from tkinter.ttk import Combobox
from tkinter.font import Font
from tkinter.ttk import Treeview

class HospitalPanel:

    def getDetails(self):
        if self.option.get() == 1 or self.option.get() == 3:
            if self.search.get().isdigit() == False:
                mb.showerror('Hospital Pannel','INVALID')
                return

        self.results = self.db.citizenDetails(self.option.get(),self.search.get())

        if len(self.results) == 0:
            mb.showinfo('Hospital Pannel','RESULT NOT FOUND')
            return

        self.table.delete(*self.table.get_children())
        
        #* filter results
        self.filteredResults = []

        for result in self.results:
            self.filteredResults.append(
                (result[0],result[1],str(result[4]),result[5],str(result[6]),result[7],result[10])
            )

        for result in self.filteredResults:
            self.table.insert("",'end',values=result)

        
    def __init__(self):

        #* database instance
        self.db = Database()

        self.root = tk.Tk() #* root widget
        self.root.iconbitmap('images/hospital.ico')
        self.root.title('Hospital Pannel')
        self.root.minsize(900,600)
        self.root.maxsize(900,600)

        #* frame 1
        self.frame1 = tk.PanedWindow(self.root,height=50,bg='#afeaed')
        self.frame1.pack(side='top',fill='x')

        #* adding widgets to frame1
        self.search = tk.Entry(self.frame1,font=Font(size=14),foreground='black',
        width=30,
        background='white') 
        self.search.grid(row=0,column=0,padx=10,pady=10)

        self.option = tk.IntVar()
        self.option.set(1)
        self.nameR = tk.Radiobutton(self.frame1,bg='#afeaed',text='name',variable=self.option,value=2)
        self.mobR = tk.Radiobutton(self.frame1,bg='#afeaed',text='mobile',variable=self.option,value=3)
        self.idR = tk.Radiobutton(self.frame1,bg='#afeaed',text='id',variable=self.option,value=1)

        self.mobR.grid(row=0,column=3,padx=20,pady=10)
        self.nameR.grid(row=0,column=2,padx=20,pady=10)
        self.idR.grid(row=0,column=1,padx=20,pady=10)

        tk.Button(self.frame1,text='Submit',command=self.getDetails,font=Font(size=12,weight='bold'),
        width=22,background='#afeaed',foreground='black',borderwidth=.7).grid(row=0,column=4,padx=15,pady=10)
        
        #* frame 2
        self.frame2 = tk.PanedWindow(self.root)
        self.frame2.pack(side='top',fill='both')

        #* adding table to frame 2
        self.table = Treeview(self.frame2,selectmode='browse')
        self.table.pack(side='top',fill='both',padx=10,pady=20)

        #* adding columns and heading to it
        # self.selectHospital['values'] = self.db.returnHospitalsName()
        self.table['columns'] = ('1','2','3','4','5','6','7')
        self.table['show'] = 'headings'

        self.table.column('1',width=50,anchor='c')
        self.table.column('2',width=50,anchor='c')
        self.table.column('3',width=50,anchor='c')
        self.table.column('4',width=50,anchor='c')
        self.table.column('5',width=50,anchor='c')
        self.table.column('6',width=50,anchor='c')
        self.table.column('7',width=50,anchor='c')

        self.table.heading('1',text='Id')
        self.table.heading('2',text='Name')
        self.table.heading('3',text='Date of first doze')
        self.table.heading('4',text='Center of first doze')
        self.table.heading('5',text='Date of second doze')
        self.table.heading('6',text='Center of second doze')
        self.table.heading('7',text='Mobile number')

        self.root.mainloop()


