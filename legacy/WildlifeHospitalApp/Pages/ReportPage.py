import tkinter as tk
from Pages.DB.CSC100DB import CSC100DB


db = CSC100DB()


class ReportPage(tk.Frame):

    def __init__(self, parent, controller):
        # self = this frame specific.
        tk.Frame.__init__(self, parent)
        # set controller to MainApp()
        self.controller = controller

        # Generates monthly report

        button1 = tk.Button(self, text="Generate monthly report",
                               relief=tk.FLAT, command=lambda: self.buttonClick()).pack()

        # TODO Add Visual Graphs & Plan Layout


# Function used to generate monthly report

    def buttonClick(self):
        print(db.getMonthlyDataForTaxons('01', 2018))
        print(db.getMonthlyDataForLGA('01', 2018))
        print(db.previousMonths('', '', ''))
