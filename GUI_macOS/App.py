from LoginPage import LoginPage
from RegisterPage import RegisterPage
from ReportPage import ReportPage
import tkinter as tk


service_id = 'Wildlife Hospital'
username = ""


# TODO CHECK TO CHANGE THE kr IMPORT AND MOVE IT TO THE REGISTER PAGE


class MainApp(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        container = tk.Frame(self)

        # Set Full-Screen
        self.state("zoomed")
        container.pack(side="top", fill="both", expand=True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {
            "LoginPage": LoginPage,
            "RegisterPage": RegisterPage,
            "ReportPage": ReportPage
        }

        for F in self.frames.values():
            frame = F(container, self)
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("LoginPage")

    def show_frame(self, cont):
        """This function is used to bring the window to the front, for viewing.
        Takes one argument show_frame(WindowClass)"""
        frame = self.frames[cont]
        frame.lift(self)

    def get_page(self, page_class):
        """This function is used to pull a windows data without needing to view the page
        Takes one argument get_page(WindowClass)"""
        return self.frames[page_class]


app = MainApp()
app.geometry("1920x1080")
app.mainloop()
