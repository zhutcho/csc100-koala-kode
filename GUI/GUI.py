import tkinter as tk
import keyring as kr
import ReportPage as rp
import Register as reg
import AdminPage as ap
import StaffPage as sp
#TODO CHECK TO CHANGE THE kr IMPORT AND MOVE IT TO THE REGISTER PAGE
service_id = 'Wildlife Hospital'
username = ""

class MainApp(tk.Tk):
    """is the Controller of the application...
    to access this class from the children classes, use controller.function,
    useful functions in this class are controller.show_frame & controller.get_page"""
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        container = tk.Frame(self)

        #Set Full-Screen
        self.state("zoomed")
        container.pack(side="top", fill="both", expand=True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        #Create Empty list for windows
        self.frames = {}
        #Cycle through windows and set them all to frames
        # !!! UPON CREATING A NEW GUI ENTER THE CHILD CLASS NAME HERE !!!
        for F in (LoginWindow,RegisterWindow, ap.AdminPage,sp.StaffPage,rp.ReportPage):
            frame = F(container, self)

            self.frames[F] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        #Set Page on Startup:
        self.show_frame(LoginWindow)

    def show_frame(self, cont):
        """This function is used to bring the window to the front, for viewing.
        Takes one argument show_frame(WindowClass)"""
        frame = self.frames[cont]
        frame.tkraise()
    def get_page(self,page_class):
        """This function is used to pull a windows data without needing to view the page
        Takes one argument get_page(WindowClass)"""
        return self.frames[page_class]

class RegisterWindow(tk.Frame):
    """is the GUI Class for the Register Window...
    this class takes in one argument for a tkinter Frame function(tk.Frame)"""
    def __init__(self, parent, controller):

        #Set self to initiate on request
        tk.Frame.__init__(self, parent)
        #Set controller to MainApp()
        self.controller = controller

        # --- Change Anything to the GUI bellow here ---
        """==============================================================="""

        #Set Background Colour
        self.config(bg="#b7bbc3")

        #Create new frame and
        register_frame = tk.Frame(self, width=500, height=250, bg='#7f8694')
        register_frame.place(x=10, y=10, relx=0.01, rely=0.01)

        #USERNAME GUI
        register_label = tk.Label(register_frame,
                                  text="New Username: ", bg='#7f8694', fg='#1b1811', font="Helvetica 10")
        register_label.place(relx=0.045,rely=0.18,anchor=tk.W)
            #Entry Box
        self.new_username = tk.Entry(register_frame, width=35)
        self.new_username.place(relx=0.05, rely=0.25, anchor=tk.W)

        # PASSWORD GUI
        password_label = tk.Label(register_frame,
                                  text="New Password: ", bg='#7f8694', fg='#1b1811', font="Helvetica 10")
        password_label.place(relx=0.045,rely=0.38,anchor=tk.W)
            #Entry Box
        self.new_password = tk.Entry(register_frame, width=35)
        self.new_password.place(relx=0.05, rely=0.45, anchor=tk.W)
        self.new_password.config(show='*')
        #Create Button GUI
        create_button = tk.Button(register_frame, text="Create",font="Helvetica 10", command=lambda:
                                  reg.Registry.register_entry(self))

        create_button.place(relx=0.05, rely=0.57, anchor=tk.W)
        #Cancel Button GUI
        cancel_button = tk.Button(register_frame,
                                  text="Cancel",font="Helvetica 10", command=lambda: controller.show_frame(LoginWindow))
        cancel_button.place(relx=0.15, rely=0.57, anchor=tk.W)

        self.register_warning_label = tk.Label(register_frame,
                                  text="", bg='#7f8694', fg='#C03A3A', font="Helvetica 10")
        self.register_warning_label.place(relx=0.045,rely=0.7,anchor=tk.W)

class LoginWindow(tk.Frame):
    """is the GUI Class for the Login Window...
     this class takes in one argument for a tkinter Frame function(tk.Frame)"""
    def __init__(self, parent,controller):
        tk.Frame.__init__(self, parent)
        #Set MainApp to controller
        self.controller = controller

        # --- Change Anything to the GUI bellow here ---
        """==============================================================="""

        #Background for Login Window
        self.config(bg="#b7bbc3")
#b7bbc3
        #Frame_One
        login_frame = tk.Frame(self, width=500, height=250, bg='#7f8694')
        login_frame.place(x=10,y=10,relx=0.01, rely=0.01)
        #USERNAME GUI
        username_label = tk.Label(login_frame, text="Username: ", bg='#7f8694', fg='#1b1811', font="Helvetica 10")
        username_label.place(relx=0.045,rely=0.18,anchor=tk.W)
            #Entry Box
        self.user_name = tk.Entry(login_frame, width=35)
        self.user_name.place(relx=0.05, rely=0.25, anchor=tk.W)

        #PASSWORD
        password_label = tk.Label(login_frame, text="Password: ", bg='#7f8694', fg='#1b1811', font="Helvetica 10")
        password_label.place(relx=0.045,rely=0.38,anchor=tk.W)
            #Entry Box
        self.pass_word = tk.Entry(login_frame, width=35)
        self.pass_word.place(relx=0.05, rely=0.45, anchor=tk.W)
        self.pass_word.config(show='*')
        #Login Button
        login_button = tk.Button(login_frame, text="Login", command=lambda: reg.Registry.login_entry(self))
        login_button.place(relx=0.05, rely=0.57, anchor=tk.W)

        #Register Text
        request_registry_label = tk.Label(login_frame,
                                          text="Need an account? ", bg='#7f8694', fg='#1b1811', font="Helvetica 10")
        request_registry_label.place(relx=0.05,rely=0.70,anchor=tk.W)
        #Register Button
        register_button = tk.Button(login_frame, text="Register", relief=tk.FLAT,
                                         bg="#7f8694", fg="#023e8a", activebackground='#303A52',
                                         command=lambda: controller.show_frame(RegisterWindow), borderwidth=0,
                                        activeforeground="#C5C8CF",
                                        font="Helvetica 10")
        register_button.place(relx=0.28, rely=0.70, anchor=tk.W)

        self.login_warning_label = tk.Label(login_frame,
                                  text="", bg='#7f8694', fg='#C03A3A', font="Helvetica 10")
        self.login_warning_label.place(relx=0.045,rely=0.8,anchor=tk.W)

#Function for debugging purposes (Prints "Clicked")
def clicked():
    '''if button is clicked, display message'''
    print("Clicked.")

#Example Text
"""
        Example of displaying basic text:
        text2 = tk.Text(self,width=20, height=10)
        text2.insert(tk.INSERT,"Helloooooooo")
        text2.place(relx=0.05, rely=0.25, anchor=tk.W)
        text2.config(state="disabled")
"""


#Run Application
app = MainApp()
app.mainloop()

