from Pages.LoginPage import LoginPage
from Pages.RegisterPage import RegisterPage
from Pages.ReportPage import ReportPage
import tkinter as tk
import keyring as kr

service_id = 'Wildlife Hospital'
username = ""


# TODO CHECK TO CHANGE THE kr IMPORT AND MOVE IT TO THE REGISTER PAGE


class MainApp(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        
        #Container is the Parent frame 
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        #Empty Dict to store each class foreach frame_names as key.
        self.frames = {}
        self.frame_names = ["LoginPage", "RegisterPage", "ReportPage"]
        
        #Cycle through a tuple of windows and set them all to frames which is packed by the container from above.
        index = 0
        for F in (LoginPage, RegisterPage, ReportPage):
            frame = F(container, self)
            print(self.frame_names[index])
            print(frame)
            self.frames[self.frame_names[index]] = frame

            frame.grid(row=0, column=0, sticky="nsew")
            index += 1

        print(self.frames["LoginPage"])

        #Set which page is to be displayed on startup based on/
        #whether there exists a user in the keyring named 'admin'
        if kr.get_password(service_id, "admin") != None:
            self.show_frame("LoginPage")
        else:
            self.show_frame("RegisterPage")

    def show_frame(self, cont):
        """This function is used to bring the window to the front, for viewing.
        Takes one argument show_frame(WindowClass)"""
        frame = self.frames[cont]
        print(frame)
        frame.tkraise()

    def get_page(self, page_class):
        """This function is used to pull a windows data without needing to view the page
        Takes one argument get_page(WindowClass)"""
        return self.frames[page_class]


def RunApp():
    """Function that starts the app & sets window restrictions"""
    app = MainApp()
    app.geometry("{}x{}".format(app.winfo_screenwidth(), app.winfo_screenheight()))
    app.minsize(500,250)
    app.mainloop()

RunApp()

