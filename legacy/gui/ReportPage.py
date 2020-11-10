import GUI as gui


class ReportPage(gui.tk.Frame):

    def __init__(self, parent, controller):
        # self = this frame specific.
        gui.tk.Frame.__init__(self, parent)
        # set controller to MainApp()
        self.controller = controller

        # --- Change Anything to the GUI bellow here ---
        """==============================================================="""

        # Set Background Colour
        self.config(bg="#7f8694")

        # Return To Admin Page Button
        return_button = gui.tk.Button(self, text="Return To Profile", relief=gui.tk.FLAT,
                                      bg="#7f8694", fg="#023e8a", activebackground='#7f8694',
                                      command=lambda: controller.show_frame(gui.ap.AdminPage), borderwidth=0,
                                      activeforeground="#C5C8CF",
                                      font="Helvetica 10"
                                      )
        return_button.place(relx=0.4, rely=0.70, anchor=gui.tk.W)

        # print to PDF Button
        pdf_button = gui.tk.Button(self, text="Print to PDF", relief=gui.tk.FLAT,
                                   bg="#7f8694", fg="#023e8a", activebackground='#7f8694',
                                   command=lambda: gui.clicked(), borderwidth=0,
                                   activeforeground="#C5C8CF",
                                   font="Helvetica 10"
                                   )
        pdf_button.place(relx=0.6, rely=0.70, anchor=gui.tk.W)

        # TODO Add Visual Graphs & Plan Layout
