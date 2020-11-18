from CreatePDF import CreatePDF
import tkinter as tk
from PIL import Image, ImageTk
from pdf2image import convert_from_path
from tkdocviewer import *


class ReportPage(tk.Frame):

    def __init__(self, parent, controller):
        # self = this frame specific.
        tk.Frame.__init__(self, parent)
        # set controller to App.App()
        self.controller = controller

        """report_frame = tk.Frame(self, width=480, height=240)
        report_frame.pack()"""

        # Generates monthly report

        button1 = tk.Button(self, text="Generate monthly report",
                            relief=tk.FLAT, command=lambda: self.exportMonthlyReport('01', 2018)).pack()

        # Create a DocViewer widget
        self.v = DocViewer(self)
        self.v.pack(side="top", expand=1, fill="both")

    def exportMonthlyReport(self, month, year):
        """Exports Monthly Report to designated file path with dating
            Parameters:
                self: the class instance
                month: the required month
                year: the required year
        """

        pdf = CreatePDF()
        pdf.exportMonthlyReport("app/docs/monthlyreport.pdf", month, year)

        # Display monthly report
        self.v.display_file("app/docs/monthlyreport.pdf")
