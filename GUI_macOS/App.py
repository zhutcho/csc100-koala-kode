import tkinter as tk
import keyring as kr
import re


# TODO CHECK TO CHANGE THE kr IMPORT AND MOVE IT TO THE REGISTER PAGE


service_id = 'Wildlife Hospital'
username = ""


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

    def show_frame(self, cont):
        """This function is used to bring the window to the front, for viewing.
        Takes one argument show_frame(WindowClass)"""
        frame = self.frames[cont]
        frame.tkraise()

    def get_page(self, page_class):
        """This function is used to pull a windows data without needing to view the page
        Takes one argument get_page(WindowClass)"""
        return self.frames[page_class]


class Register:
    """Registry Class sets passwords and usernames,
    it sets restrictions on what characters can be used as a username and password"""

    def register_entry(self):

        register_page = app.get_page(RegisterPage)

        if len(register_page.new_username.get()) <= 7 and register_page.new_username.get() != "admin":
            register_page.register_warning_label["text"] = "Username must be greater than 7 digits long"
        elif bool(re.search(r"\s", register_page.new_username.get())) == True:
            register_page.register_warning_label["text"] = "Username must not contain spaces"
        elif bool(re.search(r"\d", register_page.new_password.get())) == False\
                or bool(re.search(r"[!@#$%^&*()<>,./\{}?]", register_page.new_password.get())) == False:
            register_page.register_warning_label["text"] = "Password must contain at least one digit and at least one special character"
        else:
            kr.set_password(service_id, register_page.new_username.get(
            ), register_page.new_password.get())
            register_page.register_warning_label["text"] = ""
            # TODO THINK OF MORE CHECKS/TESTS FOR USER CREDENTIALS

            # For Developers **ONLY** DELETE UPON SUBMISSION:
            print(register_page.new_password.get())
            print(register_page.new_username.get())
            # End of Dev Only

    def login_entry(self):

        login_page = app.get_page(LoginPage)
        check_pass_word = kr.get_password(
            service_id, login_page.user_name.get())
        print(check_pass_word)
        login_page.login_warning_label["text"] = ""
        if check_pass_word == None:
            login_page.login_warning_label["text"] = "Username or Password does not exist.."
        elif check_pass_word != None and check_pass_word == login_page.pass_word.get():
            print("Successfully logged in as: " +
                  str(login_page.user_name.get()))
            if login_page.user_name.get() == "admin":
                print("Logged in As Administrator")
                app.show_frame(ReportPage)
            elif login_page.user_name.get() != "admin":
                print("Logged in As Staff Member")
                app.show_frame(ReportPage)
        elif check_pass_word != None and check_pass_word != login_page.pass_word.get():
            login_page.login_warning_label["text"] = "Username or Password does not exist.."


# sub-root to contain the LoginPage frame and a controller function to switch the tabs within the LoginPage
class LoginPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        self.controller = controller

        # Frame_One
        login_frame = tk.Frame(self, width=500, height=250)
        login_frame.place(x=10, y=10, relx=0.01, rely=0.01)
        # USERNAME GUI
        username_label = tk.Label(login_frame, text="Username: ")
        username_label.place(relx=0.045, rely=0.18, anchor=tk.W)
        # Entry Box
        self.user_name = tk.Entry(login_frame, width=35)
        self.user_name.place(relx=0.05, rely=0.25, anchor=tk.W)

        # PASSWORD
        password_label = tk.Label(
            login_frame, text="Password: ")
        password_label.place(relx=0.045, rely=0.38, anchor=tk.W)
        # Entry Box
        self.pass_word = tk.Entry(login_frame, width=35)
        self.pass_word.place(relx=0.05, rely=0.45, anchor=tk.W)
        self.pass_word.config(show='*')
        # Login Button
        login_button = tk.Button(
            login_frame, text="Login", command=lambda: Register.login_entry(self))
        login_button.place(relx=0.05, rely=0.57, anchor=tk.W)

        # Register Text
        request_registry_label = tk.Label(login_frame,
                                          text="Need an account? ")
        request_registry_label.place(relx=0.05, rely=0.70, anchor=tk.W)
        # Register Button
        register_button = tk.Button(login_frame, text="Register", relief=tk.FLAT,
                                    bg="#7f8694", fg="#023e8a", activebackground='#303A52',
                                    command=lambda: controller.show_frame(RegisterPage), borderwidth=0,
                                    activeforeground="#C5C8CF",
                                    font="Helvetica 10")
        register_button.place(relx=0.28, rely=0.70, anchor=tk.W)

        self.login_warning_label = tk.Label(login_frame,
                                            text="", fg='#C03A3A')
        self.login_warning_label.place(relx=0.045, rely=0.8, anchor=tk.W)


class RegisterPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        self.controller = controller

        # Create new frame and
        register_frame = tk.Frame(self, width=500, height=250)
        register_frame.place(x=10, y=10, relx=0.01, rely=0.01)

        # USERNAME GUI
        register_label = tk.Label(register_frame,
                                  text="New Username: ")
        register_label.place(relx=0.045, rely=0.18, anchor=tk.W)
        # Entry Box
        self.new_username = tk.Entry(register_frame, width=35)
        self.new_username.place(relx=0.05, rely=0.25, anchor=tk.W)

        # PASSWORD GUI
        password_label = tk.Label(register_frame,
                                  text="New Password: ")
        password_label.place(relx=0.045, rely=0.38, anchor=tk.W)
        # Entry Box
        self.new_password = tk.Entry(register_frame, width=35)
        self.new_password.place(relx=0.05, rely=0.45, anchor=tk.W)
        self.new_password.config(show='*')
        # Create Button GUI
        create_button = tk.Button(register_frame, text="Create", command=lambda:
                                  Register.register_entry(self))

        create_button.place(relx=0.05, rely=0.57, anchor=tk.W)
        # Cancel Button GUI
        cancel_button = tk.Button(register_frame,
                                  text="Cancel", command=lambda: controller.show_frame(LoginPage))
        cancel_button.place(relx=0.15, rely=0.57, anchor=tk.W)

        self.register_warning_label = tk.Label(register_frame,
                                               text="", fg='#C03A3A')
        self.register_warning_label.place(relx=0.045, rely=0.7, anchor=tk.W)


class ReportPage(tk.Frame):

    def __init__(self, parent, controller):
        # self = this frame specific.
        tk.Frame.__init__(self, parent)
        # set controller to MainApp()
        self.controller = controller

        # --- Change Anything to the GUI bellow here ---
        """==============================================================="""

        # Set Background Colour
        self.config(bg="#7f8694")

        # Return To Admin Page Button
        return_button = tk.Button(self, text="Return To Profile", relief=tk.FLAT,
                                  bg="#7f8694", fg="#023e8a", activebackground='#7f8694',
                                  command=lambda: controller.show_frame(AdminPage), borderwidth=0,
                                  activeforeground="#C5C8CF",
                                  font="Helvetica 10"
                                  )
        return_button.place(relx=0.4, rely=0.70, anchor=tk.W)

        # print to PDF Button
        pdf_button = tk.Button(self, text="Print to PDF", relief=tk.FLAT,
                               bg="#7f8694", fg="#023e8a", activebackground='#7f8694',
                               command=lambda: clicked(), borderwidth=0,
                               activeforeground="#C5C8CF",
                               font="Helvetica 10"
                               )
        pdf_button.place(relx=0.6, rely=0.70, anchor=tk.W)

        # TODO Add Visual Graphs & Plan Layout

# Function used for debugging purposes.


def clicked():
    print("Button Clicked!")


app = MainApp()
app.geometry("1920x1080")
app.mainloop()
