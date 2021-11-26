import tkinter as tk
from tkinter.font import Font
from recognition_pannel import RecognitionPannel
from PIL import Image, ImageTk

class Home:

    # * method to navigate to new window
    def navigate(self):
        self.root.destroy()
        RecognitionPannel()

    def __init__(self):

        self.root = tk.Tk()  # * root widget
        self.root.title('Covid Vaccine Tracker')
        self.root.geometry('900x600')
        self.root.iconbitmap('images/tracker.ico')
        self.root.minsize(1100, 800)
        self.root.maxsize(1100, 800)

        # * about dialog frame
        self.aboutDailog = tk.PanedWindow(self.root, bg='#afeaed', width=self.root.winfo_screenwidth(
        ), height=self.root.winfo_screenheight() * .1)
        self.aboutDailog.pack(fill='x')

        # * add widgets to header frame
        tk.Label(self.aboutDailog, text='ABOUT TRACKER :)', bg='#afeaed', font=Font(
            family='Arial', size=24, weight='bold')).pack(side=tk.TOP)

        tk.Message(self.aboutDailog, justify='center', text='The worldwide endeavor to create a safe and effective COVID-19 vaccine is bearing fruit. Almost two dozen vaccines now have been authorized around the globe; many more remain in development.',
                   bg='#afeaed', foreground='black', font=Font(family='Arial', size=13, weight='normal')).pack(side=tk.TOP, pady=12.0)

        # * image frame
        self.imageFrame = tk.PanedWindow(self.root).pack(side=tk.BOTTOM)

        # * creating image and then adding to image frame
        image = ImageTk.PhotoImage(Image.open(
            'images/vaccine.png').resize((400, 400)))

        tk.Button(self.imageFrame, command=self.navigate, text='Continue', background='#afeaed', font=Font(
            size=16, weight='bold'), borderwidth=.7).pack(side='right', padx=40, pady=70)

        tk.Label(self.imageFrame, image=image).pack()

        self.root.mainloop()


Home()
