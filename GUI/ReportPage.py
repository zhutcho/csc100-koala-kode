import tkinter as tk
from Database.CSC100DB import CSC100DB


class ReportPage(tk.Frame):

    def __init__(self, parent, controller):
        # self = this frame specific.
        tk.Frame.__init__(self, parent)
        # set controller to MainApp()
        self.controller = controller

        # print to PDF Button
        pdf_button = tk.Button(self, text="Create PDF",
                               relief=tk.FLAT, command=lambda: createPDF())

        # TODO Add Visual Graphs & Plan Layout


# Function used for debugging purposes.


def createPDF():
    print(CSC100DB.callMonthlyProc())
