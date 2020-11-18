import tkinter as tk
import keyring as kr
import re
# the the id in which keyring assosciates the passwords/usernames.
service_id = 'Wildlife Hospital'
username = ""


class RegisterPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        # Controller references the parent class(App.App())
        self.controller = controller

        # Register_Frame
        register_frame = tk.Frame(self, width=480, height=250)
        register_frame.pack()

        # New Username Entry Box
        self.new_username = tk.Entry(register_frame, width=35)
        self.new_username.place(
            in_=register_frame, relx=0.5, rely=0.25, anchor=tk.CENTER)
        self.new_username.insert(0, "admin")
        self.new_username.config(state="readonly")
        # New Username Label
        register_label = tk.Label(register_frame,
                                  text="New Username: ")
        register_label.place(in_=self.new_username, relx=.2,
                             rely=-0.75, anchor=tk.CENTER)

        # New Password Entry Box
        self.new_password = tk.Entry(register_frame, width=35)
        self.new_password.place(
            in_=register_frame, relx=0.5, rely=0.45, anchor=tk.CENTER)
        self.new_password.config(show='*')
        # New Password Label
        password_label = tk.Label(register_frame,
                                  text="New Password: ")
        password_label.place(in_=self.new_password,
                             relx=0.19, rely=-0.75, anchor=tk.CENTER)

        # Create Button
        create_button = tk.Button(register_frame, text="Create", command=lambda:
                                  self.register_entry())

        create_button.place(in_=self.new_password, relx=0.1,
                            rely=2, anchor=tk.CENTER)
        # Warning Display Label
        self.register_warning_label = tk.Label(register_frame,
                                               text="", fg='#C03A3A')
        self.register_warning_label.place(
            in_=register_frame, relx=0.28, rely=0.7, anchor=tk.W)

    def register_entry(self):
        """Register Requirement Checks
                Parameters:
                    self: the class instance
                Returns:
                    boolean: True as successful Register, False as unsuccessful
            """
        register_page = self.controller.get_page("RegisterPage")

        # Requirements to be met to create user
        if kr.get_password(service_id, register_page.new_username.get()) != None:
            register_page.register_warning_label["text"] = "User Already Exists"

        elif len(register_page.new_username.get()) <= 7 and register_page.new_username.get() != "admin":
            register_page.register_warning_label["text"] = "Username must be greater than 7 digits long"

        elif bool(re.search(r"\s", register_page.new_username.get())) == True:
            register_page.register_warning_label["text"] = "Username must not contain spaces"

        elif bool(re.search(r"\d", register_page.new_password.get())) == False\
                or bool(re.search(r"[!@#$%^&*()<>,./\{}?]", register_page.new_password.get())) == False:
            register_page.register_warning_label["text"] = "Password must contain a digit and a special character"

        else:
            kr.set_password(service_id, register_page.new_username.get(
            ), register_page.new_password.get())
            register_page.register_warning_label["text"] = "Successfully Created User"
            self.controller.show_frame("LoginPage")
