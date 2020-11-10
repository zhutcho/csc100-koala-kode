import tkinter as tk
from database.CSC100DB import CSC100DB


db = CSC100DB()


class ReportPage(tk.Frame):

    def __init__(self, parent, controller):
        # self = this frame specific.
        tk.Frame.__init__(self, parent)
        # set controller to MainApp()
        self.controller = controller

        # print to PDF Button
        pdf_button = tk.Button(self, text="Create PDF",
                               relief=tk.FLAT, command=lambda: self.buttonClick())
        pdf_button.pack()

        # TODO Add Visual Graphs & Plan Layout


# Function used for debugging purposes.

    def buttonClick(self):
        print(db.getMonthlyDataForTaxons('01', 2018))
        print(db.getMonthlyDataForLGA('01', 2018))
