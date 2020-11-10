import tkinter as tk
import keyring as kr
import re

service_id = 'Wildlife Hospital'
username = ""

class RegisterPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        self.controller = controller

        # Create new frame and
        register_frame = tk.Frame(self, width=480, height=250)
        register_frame.place(x=register_frame.winfo_screenwidth()/2, y=register_frame.winfo_screenheight()/2 - 100, anchor="c")

        # USERNAME GUI
        register_label = tk.Label(register_frame,
                                  text="New Username: ")
        register_label.place(relx=0.37, rely=0.18, anchor=tk.CENTER)
        # Entry Box
        self.new_username = tk.Entry(register_frame, width=35)
        self.new_username.place(relx=0.5, rely=0.25, anchor=tk.CENTER)
        self.new_username.insert(0,"admin")
        self.new_username.config(state="readonly")
        # PASSWORD GUI
        password_label = tk.Label(register_frame,
                                  text="New Password: ")
        password_label.place(relx=0.37, rely=0.38, anchor=tk.CENTER)
        # Entry Box
        self.new_password = tk.Entry(register_frame, width=35)
        self.new_password.place(relx=0.5, rely=0.45, anchor=tk.CENTER)
        self.new_password.config(show='*')
        # Create Button GUI
        create_button = tk.Button(register_frame, text="Create", command=lambda:
                                  register_entry(self))

        create_button.place(relx=0.32, rely=0.57, anchor=tk.CENTER)
        # Cancel Button GUI
        """
        cancel_button = tk.Button(register_frame,
                                  text="Login", command=lambda: controller.show_frame("LoginPage"))
        cancel_button.place(relx=0.42, rely=0.57, anchor=tk.CENTER)
        """
        self.register_warning_label = tk.Label(register_frame,
                                               text="", fg='#C03A3A')
        self.register_warning_label.place(relx=0.27, rely=0.7, anchor=tk.W)


def register_entry(self):

    register_page = self.controller.get_page("RegisterPage")
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
        # TODO THINK OF MORE CHECKS/TESTS FOR USER CREDENTIALS

        # For Developers **ONLY** DELETE UPON SUBMISSION:
        print(register_page.new_password.get())
        print(register_page.new_username.get())
        # End of Dev Only
