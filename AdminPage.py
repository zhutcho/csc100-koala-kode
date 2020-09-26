import GUI as gui

class AdminPage(gui.tk.Frame):

    def __init__(self, parent, controller):
        # self = this frame specific.
        gui.tk.Frame.__init__(self, parent)
        #set controller to MainApp()
        self.controller = controller

        # --- Change Anything to the GUI bellow here ---
        """==============================================================="""
        # Create 'Logged in as:' text
        admin_text = gui.tk.Text(self, width=50, height=2, bg='#b7bbc3', relief=gui.tk.FLAT,font="Helvetica 10")
        admin_text.insert(gui.tk.INSERT, "Signed in as Administrator")
        admin_text.place(relx=0.83, rely=0.0195, anchor=gui.tk.W)
        admin_text.config(state="disabled")
        sign_out_button = gui.tk.Button(self, text="Sign Out", relief=gui.tk.FLAT,
                                        bg="#b7bbc3", fg="#1b1811", activebackground='#b7bbc3',
                                        command=lambda: controller.show_frame(gui.LoginWindow), borderwidth=0,
                                        activeforeground="#527b99",
                                        font="Helvetica 10 underline"
                                        )
        sign_out_button.place(relx=0.94, rely=0.01, anchor=gui.tk.W)


        #Background colour
        self.config(bg="#b7bbc3")
        #Create new frame
        admin_page_frame_right = gui.tk.Frame(self, width=1505, height=805, bg='#7f8694',)
        admin_page_frame_right.place(x=0,y=10,relx=0.01, rely=0.01)


        #Brief Report Button
        brief_report_button = gui.tk.Button(admin_page_frame_right, text="REPORT", relief=gui.tk.FLAT,
                                         bg="#7f8694", fg="#1b1811", activebackground='#7f8694',
                                         command=lambda: controller.show_frame(gui.rp.ReportPage), borderwidth=0,
                                        activeforeground="#C5C8CF",
                                        font="Helvetica 20 underline"
                                         )
        brief_report_button.place(relx=0.9, rely=0.95, anchor=gui.tk.W)



        #TODO Complete GUI & Plan Layout.