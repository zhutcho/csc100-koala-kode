import tkinter as tk
from database.CSC100DB import CSC100DB
from PIL import Image,ImageTk
from pdf2image import convert_from_path


db = CSC100DB()


class ReportPage(tk.Frame):

    def __init__(self, parent, controller):
        # self = this frame specific.
        tk.Frame.__init__(self, parent)
        # set controller to MainApp()
        self.controller = controller

        """report_frame = tk.Frame(self, width=480, height=240)
        report_frame.pack()"""

        # Generates monthly report

        button1 = tk.Button(self, text="Generate monthly report",
                               relief=tk.FLAT, command=lambda: self.buttonClick()).pack()
        
        # Adding Scrollbar to the PDF frame
        scrol_y = tk.Scrollbar(self, orient=tk.VERTICAL)
        # Adding text widget for inserting images
        pdf = tk.Text(self, yscrollcommand=scrol_y.set,bg="grey")
        # Setting the scrollbar to the right side
        scrol_y.pack(side=tk.RIGHT,fill=tk.Y)
        scrol_y.config(command=pdf.yview)
        # Finally packing the text widget
        pdf.pack()
        # Here the PDF is converted to list of images
        pages = convert_from_path('D:\Downloads\combinepdf.pdf',size=(800,900))
        # Empty list for storing images
        photos = []
        # Storing the converted images into list
        for i in range(len(pages)):
          photos.append(ImageTk.PhotoImage(pages[i]))
          
        # Adding all the images to the text widget
        for photo in photos:
          pdf.image_create(tk.END,image=photo)
        # For Seperating the pages
          pdf.insert(tk.END,'\n\n')

        # TODO Add Visual Graphs & Plan Layout


# Function used to generate monthly report

    def buttonClick(self):
        """print(db.getMonthlyDataForTaxons('01', 2018))
        print(db.getMonthlyDataForLGA('01', 2018))
        print(db.previousMonths('', '', ''))"""

 
"""# Adding Scrollbar to the PDF frame
scrol_y = tk.Scrollbar(orient=tk.VERTICAL)
# Adding text widget for inserting images
pdf = tk.Text(yscrollcommand=scrol_y.set,bg="grey")
# Setting the scrollbar to the right side
scrol_y.pack(side=tk.RIGHT,fill=tk.Y)
scrol_y.config(command=pdf.yview)
# Finally packing the text widget
pdf.pack(fill=tk.BOTH,expand=1)
# Here the PDF is converted to list of images
pages = convert_from_path('D:\Downloads\combinepdf.pdf',size=(800,900))
# Empty list for storing images
photos = []
# Storing the converted images into list
for i in range(len(pages)):
  photos.append(ImageTk.PhotoImage(pages[i]))
# Adding all the images to the text widget
for photo in photos:
  pdf.image_create(tk.END,image=photo)
# For Seperating the pages
pdf.insert(tk.END,'\n\n')"""
