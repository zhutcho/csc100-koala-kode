import tkinter as tk
import LoginPage
import RegisterPage
import ReportPage


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
    # Create Empty list for windows
        self.frames = {}
        # Cycle through windows and set them all to frames
        # !!! UPON CREATING A NEW GUI ENTER THE CHILD CLASS NAME HERE !!!
        for F in (LoginPage, RegisterPage, ReportPage):
            frame = F(container, self)

            self.frames[F] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        # Set Page on Startup:
        self.show_frame(LoginPage)

    def show_frame(self, container):
        """This function is used to bring the window to the front, for viewing.
        Takes one argument show_frame(WindowClass)"""
        frame = self.frames[container]
        frame.tkraise()

    def get_page(self, page_class):
        """This function is used to pull a windows data without needing to view the page
        Takes one argument get_page(WindowClass)"""
        return self.frames[page_class]


app = MainApp()
app.geometry("1920x1080")
app.mainloop()
