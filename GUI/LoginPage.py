import tkinter as tk
import keyring as kr


service_id = 'Wildlife Hospital'
username = ""


# sub-root to contain the LoginPage frame and a controller function to switch the tabs within the LoginPage
class LoginPage(tk.Frame):

    name = "LoginPage"

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        #Controller references the parent class(App.MainApp())
        self.controller = controller

        #Login_Frame
        login_frame = tk.Frame(self, width=480, height=240)
        login_frame.pack()
      
        #Username Entry Box
        self.user_name = tk.Entry(login_frame, width=35)
        self.user_name.place(in_=login_frame,relx=0.5, rely=0.25, anchor=tk.CENTER)
        #Username Label
        username_label = tk.Label(login_frame, text="Username: ")
        username_label.place(in_=self.user_name, relx=.125, rely=-0.75, anchor=tk.CENTER)
        #Password Entry Box
        self.pass_word = tk.Entry(login_frame, width=35)
        self.pass_word.place(in_=login_frame,relx=0.5, rely=0.45, anchor=tk.CENTER)
        self.pass_word.config(show='*')
        #Password Label
        password_label = tk.Label(
            login_frame, text="Password: ")
        password_label.place(in_=self.pass_word,relx=0.125, rely=-0.75, anchor=tk.CENTER)
        #Login Button
        login_button = tk.Button(
            login_frame, text="Login", command=lambda: self.login_entry())
        login_button.place(in_=self.pass_word,relx=0.1, rely=2, anchor=tk.CENTER)
        #Warning Display Label
        self.login_warning_label = tk.Label(login_frame,
                                            text="", fg='#C03A3A')
        self.login_warning_label.place(in_=login_frame,relx=0.28, rely=0.7, anchor=tk.W)


    def get_name(self):
        """Returns Class Identity for Dict key"""
        return "LoginPage"

    def login_entry(self):
        """Login Requirement Checks"""
        login_page = self.controller.get_page("LoginPage")

        #Check password
        check_pass_word = kr.get_password(
            service_id, login_page.user_name.get())

        #Warning Label
        login_page.login_warning_label["text"] = ""

        #Password Requirement Checks
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
                #REMOVED CODE FOR STAFF MEMBER PAGE
        elif check_pass_word != None and check_pass_word != login_page.pass_word.get():
            login_page.login_warning_label["text"] = "Username or Password does not exist.."
