import os
from PIL import ImageTk, Image
import tkinter as tk
from tkinter import CENTER, Tk, BOTH, Text, Toplevel
from tkinter.ttk import Frame, Button, Label, Style
from tkinter import messagebox as mbox

script_dir = os.path.dirname(__file__)
image1_path = os.path.join(script_dir, "..", "images", "image.png")
image2_path = os.path.join(script_dir, "..", "images", "office_login_2.png")

root = Tk()

class Window(Frame):
    def __init__(self, on_login_callback):
        super().__init__()
        self.initUI()
        self.on_login_callback = on_login_callback 
    
    def initUI(self):
        self.master.title("ASMC Board of Directors: Office Login")
        self.pack(fill=BOTH, expand=1)

        self.centerWindow()
        
        Style().configure("TFrame", background="#333")
        
        ASMC_logo = Image.open(image1_path)
        ASMC_logojov = ImageTk.PhotoImage(ASMC_logo)
        label1 = Label(self, image=ASMC_logojov)
        label1.image = ASMC_logojov
        label1.place(relx=0.5, rely=0.25, anchor=CENTER)
        
        Office_logo = Image.open(image2_path)
        Office_logojov = ImageTk.PhotoImage(Office_logo)
        label2 = Label(self, image=Office_logojov)
        label2.image = Office_logojov
        label2.place(relx=0.48, rely=0.52, anchor=CENTER)
        
        self.text_widget = tk.Text(self, height=1, width=30)
        self.text_widget.place(relx=0.48, rely=0.59, anchor=CENTER)
        self.text_widget.insert("1.0", "INPUT ID TO LOGIN")
        
        self.login_button = Button(self, text="Login", command=self.handle_login)
        self.login_button.place(relx=0.48, rely=0.65, anchor=CENTER)
        self.text_widget.bind("<Return>", lambda event=None: self.handle_login())
        
        def temp_text(e):
            self.text_widget.delete("1.0", "end")
            
        self.text_widget.bind("<FocusIn>", temp_text)
        
        
        # clam, default, alt, classic themes
        self.style = Style()
        self.style.theme_use("clam")
        
    def text_widget_value(self):
        inputValue = self.text_widget.get("1.0", 'end-1c')
        return inputValue
    
    def handle_login(self):
        input_value = self.text_widget_value()
        self.on_login_callback(input_value)
        
    def centerWindow(self):
        w = 640
        h = 480
        
        # height and width values of application window
        sw = self.master.winfo_screenwidth()
        sh = self.master.winfo_screenheight()
        
        # height and width of screen
        x = (sw - w)/2
        y = (sh - h)/2
        # calculate the required x and y coordinates
        self.master.geometry('%dx%d+%d+%d' % (w, h, x, y))
        
def clockWindow(user, name, role, ID, status, date):
    pop = Toplevel(root)
    pop.title("CLOCKED IN")
    pop.geometry("320x240")