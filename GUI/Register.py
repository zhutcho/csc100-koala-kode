import GUI as gui
import re


class Registry:
    """Registry Class sets passwords and usernames,
    it sets restrictions on what characters can be used as a username and password"""

    def register_entry(self):

        register_page = gui.app.get_page(gui.RegisterWindow)

        if len(register_page.new_username.get()) <= 7 and register_page.new_username.get() != "admin":
            register_page.register_warning_label["text"] = "Username must be greater than 7 digits long"
        elif bool(re.search(r"\s", register_page.new_username.get())) == True:
            register_page.register_warning_label["text"] = "Username must not contain spaces"
        elif bool(re.search(r"\d", register_page.new_password.get())) == False\
                or bool(re.search(r"[!@#$%^&*()<>,./\{}?]", register_page.new_password.get())) == False:
            register_page.register_warning_label["text"] = "Password must contain at least one digit and at least one special character"
        else:
            gui.kr.set_password(gui.service_id, register_page.new_username.get(
            ), register_page.new_password.get())
            register_page.register_warning_label["text"] = ""
            # TODO THINK OF MORE CHECKS/TESTS FOR USER CREDENTIALS

            # For Developers **ONLY** DELETE UPON SUBMISSION:
            print(register_page.new_password.get())
            print(register_page.new_username.get())
            # End of Dev Only

    def login_entry(self):

        login_page = gui.app.get_page(gui.LoginWindow)
        check_pass_word = gui.kr.get_password(
            gui.service_id, login_page.user_name.get())
        print(check_pass_word)
        login_page.login_warning_label["text"] = ""
        if check_pass_word == None:
            login_page.login_warning_label["text"] = "Username or Password does not exist.."
        elif check_pass_word != None and check_pass_word == login_page.pass_word.get():
            print("Successfully logged in as: " +
                  str(login_page.user_name.get()))
            if login_page.user_name.get() == "admin":
                print("Logged in As Administrator")
                gui.app.show_frame(gui.ap.AdminPage)
            elif login_page.user_name.get() != "admin":
                print("Logged in As Staff Member")
                gui.app.show_frame(gui.sp.StaffPage)
        elif check_pass_word != None and check_pass_word != login_page.pass_word.get():
            login_page.login_warning_label["text"] = "Username or Password does not exist.."
