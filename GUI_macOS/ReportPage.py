import tkinter as tk


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
