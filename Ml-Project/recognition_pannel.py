from database import Database
import tkinter as tk
from pyautogui import press
import tkcap
from tkinter.font import Font
import cv2 as cv
import deepface.DeepFace as df
from PIL import Image, ImageTk

# * Recognition Pannel
class RecognitionPannel:

    # * method to take scr of widget
    def saveVaccineDetails(self):

        self.details = tkcap.CAP(self.infoPannel)
        self.details.capture(f'{self.data[0][1]}.png')

    # * method to show details
    def showDetails(self):
        if self.isDetected == False:
            self.isDetected = True

            # * top level window
            self.infoPannel = tk.Tk()
            self.infoPannel.iconbitmap('images/details.ico')
            self.infoPannel.title('Details')
            self.infoPannel.configure(bg='#afeaed')
            self.infoPannel.minsize(400, 600)
            self.infoPannel.maxsize(400, 600)

            # * user data
            self.data = self.db.getCitizenDetailsAfterDetection(
                self.images[self.imageIndex][0])

            # *image of user
            self.userImage = ImageTk.PhotoImage(
                Image.open(self.images[self.imageIndex][2]))

            # * image label
            tk.Label(self.infoPannel, image=self.userImage).grid(
                row=0, column=0, padx=20, pady=20)
            tk.Label(self.infoPannel, bg='#afeaed', font=Font(family='Arial', size=15,
                                                              weight='bold'), text=self.data[0][1]).grid(row=0, column=1, pady=20)

            tk.Label(self.infoPannel, bg='#afeaed', font=Font(family='Arial', size=12, weight='normal'),
                     text='Fully Vaccinated : ').grid(row=1, column=0, padx=10, pady=15)

            if str(self.data[0][4]) != '' and str(self.data[0][4]) != '':
                tk.Label(self.infoPannel, bg='#afeaed', fg='green', font=Font(family='Arial', size=12,
                                                                              weight='bold'), text='Yes').grid(row=1, column=1, padx=5, pady=15)
            else:
                tk.Label(self.infoPannel, bg='#afeaed', fg='red', font=Font(family='Arial', size=12,
                                                                            weight='bold'), text='No').grid(row=1, column=1, padx=5, pady=15)

            tk.Label(self.infoPannel, bg='#afeaed', font=Font(family='Arial', size=12, weight='normal'),
                     text='Father\'s name : ').grid(row=2, column=0, padx=10, pady=15)
            tk.Label(self.infoPannel, bg='#afeaed', font=Font(family='Arial', size=12,
                                                              weight='normal'), text=self.data[0][2]).grid(row=2, column=1,  pady=15)

            tk.Label(self.infoPannel, bg='#afeaed', font=Font(family='Arial', size=12, weight='normal'),
                     text='First Doze : ').grid(row=3, column=0, padx=10, pady=15)
            tk.Label(self.infoPannel, bg='#afeaed', font=Font(family='Arial', size=12, weight='normal'), text=str(
                self.data[0][4])).grid(row=3, column=1,  pady=15)

            tk.Label(self.infoPannel, bg='#afeaed', font=Font(family='Arial', size=12, weight='normal'),
                     text='Second Doze : ').grid(row=4, column=0, padx=10, pady=15)
            tk.Label(self.infoPannel, bg='#afeaed', font=Font(family='Arial', size=12, weight='normal'), text=str(
                self.data[0][6])).grid(row=4, column=1,  pady=15)

            tk.Label(self.infoPannel, bg='#afeaed', font=Font(family='Arial', size=12, weight='normal'),
                     text='Contact : ').grid(row=5, column=0, padx=10, pady=15)
            tk.Label(self.infoPannel, bg='#afeaed', font=Font(family='Arial', size=12, weight='normal'),
                     text=self.data[0][10]).grid(row=5, column=1,  pady=15)

            tk.Button(self.infoPannel, bg='#afeaed', text='Save Details', command=self.saveVaccineDetails, font=Font(size=13, weight='normal',
                                                                                                                     slant='italic'), background='#afeaed', foreground='black', borderwidth=.7).grid(row=6, column=1,  pady=25, columnspan=2)

            self.infoPannel.mainloop()

            self.isDetected = False

    def __init__(self):

        # * database instance
        self.db = Database()

        web = cv.VideoCapture(0, cv.CAP_DSHOW)
        web.set(cv.CAP_PROP_FRAME_WIDTH, 1280)
        web.set(cv.CAP_PROP_FRAME_HEIGHT, 720)

        self.images = self.db.getImages()

        self.isDetected = False
        self.imageIndex = -1

        while True:

            frame = web.read()[1]

            for index, image in enumerate(self.images):
                try:
                    result = df.verify(
                        img1_path=frame, img2_path=image[1])

                    if result['verified']:
                        self.imageIndex = index

                    if result['verified']:
                        cv.putText(frame, text='DETECTED', org=(20, 20), fontScale=.7, color=(
                            0, 255, 0), thickness=2, fontFace=cv.LINE_AA)

                        press('q')

                    else:
                        cv.putText(frame, text='NOT DETECTED', org=(20, 20), fontScale=.7, color=(
                            0, 0, 255), thickness=2, fontFace=cv.LINE_AA)

                except:
                    cv.putText(frame, text='FRAME HAS NO FACE', org=(
                        20, 20), fontScale=.7, color=(0, 0, 255), thickness=2, fontFace=cv.LINE_AA)

            cv.imshow('Camera', frame)

            if cv.waitKey(1) & 0xFF == ord('q'):
                break

        web.release()
        cv.destroyAllWindows()

        self.showDetails()

