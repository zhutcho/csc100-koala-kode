import tkinter as tk
from database.CSC100DB import CSC100DB
from PIL import Image,ImageTk
from tkdocviewer import *


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

        # Create a DocViewer widget
        v = DocViewer(self)
        v.pack(side="top", expand=1, fill="both")

        # Display some document
        v.display_file("Put the path of the pdf here")

        # TODO Add Visual Graphs & Plan Layout
