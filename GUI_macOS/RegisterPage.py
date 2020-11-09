import tkinter as tk
import keyring as kr
import re


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
                                  register_entry(self))

        create_button.place(relx=0.05, rely=0.57, anchor=tk.W)
        # Cancel Button GUI
        cancel_button = tk.Button(register_frame,
                                  text="Cancel", command=lambda: controller.show_frame("LoginPage"))
        cancel_button.place(relx=0.15, rely=0.57, anchor=tk.W)

        self.register_warning_label = tk.Label(register_frame,
                                               text="", fg='#C03A3A')
        self.register_warning_label.place(relx=0.045, rely=0.7, anchor=tk.W)


def register_entry(self):

    register_page = get_page("RegisterPage")

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
