import tkinter as tk
from CreatePDF import CreatePDF
import datetime


class ReportPage(tk.Frame):

    def __init__(self, parent, controller):
        # self = this frame specific.
        tk.Frame.__init__(self, parent)
        # set controller to MainApp()
        self.controller = controller

        # Generates monthly report

        button1 = tk.Button(self, text="Generate monthly report",
                               relief=tk.FLAT, command=lambda: pdf.getMonthlyReport(month, year)).pack()

        # TODO Add Visual Graphs & Plan Layout


