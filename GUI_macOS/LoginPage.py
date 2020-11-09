import tkinter as tk
import keyring as kr


service_id = 'Wildlife Hospital'
username = ""


# sub-root to contain the LoginPage frame and a controller function to switch the tabs within the LoginPage
class LoginPage(tk.Frame):

    name = "LoginPage"

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
            login_frame, text="Login", command=lambda: self.login_entry())
        login_button.place(relx=0.05, rely=0.57, anchor=tk.W)
        """
        # Register Text
        request_registry_label = tk.Label(login_frame,
                                          text="Need an account? ")
        request_registry_label.place(relx=0.05, rely=0.70, anchor=tk.W)
        # Register Button
        register_button = tk.Button(login_frame, text="Register", relief=tk.FLAT,
                                    bg="#7f8694", fg="#023e8a", activebackground='#303A52',
                                    command=lambda: controller.show_frame("RegisterPage"), borderwidth=0,
                                    activeforeground="#C5C8CF",
                                    font="Helvetica 10")
        register_button.place(relx=0.28, rely=0.70, anchor=tk.W)
        """
        self.login_warning_label = tk.Label(login_frame,
                                            text="", fg='#C03A3A')
        self.login_warning_label.place(relx=0.045, rely=0.8, anchor=tk.W)

    def get_name(self):
        return "LoginPage"

    def login_entry(self):

        login_page = self.controller.get_page("LoginPage")
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
                self.controller.show_frame("ReportPage")
            elif login_page.user_name.get() != "admin":
                print("Logged in As Staff Member")
                self.controller.show_frame("ReportPage")
        elif check_pass_word != None and check_pass_word != login_page.pass_word.get():
            login_page.login_warning_label["text"] = "Username or Password does not exist.."
