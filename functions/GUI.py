import os
from PIL import Image, ImageTk
import tkinter as tk
from tkinter import CENTER, Tk, BOTH, Text
from tkinter.ttk import Frame, Button, Label, Style
from tkinter import messagebox as mbox

script_dir = os.path.dirname(__file__)
image1_path = os.path.join(script_dir, "..", "images", "image.png")
image2_path = os.path.join(script_dir, "..", "images", "office_login_2.png")

class Window(Frame):
    def __init__(self):
        super().__init__()
        
        self.initUI()
    
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
        
        #text_label = Label(self, text="ENTER ID TO LOGIN")
        #text_label.place(relx=0.5, rely=0.64, anchor=CENTER)
        
        
        self.text_widget = tk.Text(self, height=1, width=30)
        self.text_widget.place(relx=0.48, rely=0.59, anchor=CENTER)
        self.text_widget.insert("1.0", "INPUT ID TO LOGIN")
        
        def temp_text(e):
            self.text_widget.delete("1.0", "end")
        
        self.text_widget.bind("<FocusIn>", temp_text)
        

        
        # clam, default, alt, classic themes
        self.style = Style()
        self.style.theme_use("clam")
    

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
        
    
        
        
        
    
def main():
    root = Tk()
    root.geometry("250x150+300+300")
    root.resizable(False, False)
    app = Window()
    root.mainloop()
    
if __name__ == '__main__':
    main()