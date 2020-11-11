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
        pdf_button.place(relx=1, rely=0.57, anchor=tk.W)
        pdf_button.pack()

        # drop down box

        # Function used for drop down box
        def show():
            myLabel = tk.Label(self, text = clicked.get()).pack()

        options = [
            "Select Month",
            "Janurary",
            "Feburary",
            "March",
            "April",
            "May",
            "June",
            "July",
            "August",
            "September",
            "October",
            "November",
            "December"
        ]

        clicked = tk.StringVar()
        clicked.set(options[0])

        drop = tk.OptionMenu(self, clicked, *options)
        drop.pack()

        dropButton = tk.Button(self, text = "Show Selection", command = show).pack()
        # TODO Add Visual Graphs & Plan Layout


# Function used for debugging purposes.

    def buttonClick(self):
        print(db.getMonthlyDataForTaxons('01', 2018))
        print(db.getMonthlyDataForLGA('01', 2018))
