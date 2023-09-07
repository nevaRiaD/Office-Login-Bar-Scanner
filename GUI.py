import os
from PIL import Image, ImageTk
from tkinter import CENTER, Tk, BOTH
from tkinter.ttk import Frame, Button, Label, Style

file_directory = r"E:\VScode\Python Learning\barScan\Office-Login-Bar-Scanner"
image1 = file_directory + "\\logoASMC_70.png"

class Window(Frame):
    def __init__(self):
        super().__init__()
        
        self.initUI()
        
    def initUI(self):
        self.master.title("ASMC Board of Directors: Office Login")
        self.pack(fill=BOTH, expand=1)

        self.centerWindow()
        
        Style().configure("TFrame", background="#333")
        
        ASMC_logo = Image.open(image1)
        ASMC_logojov = ImageTk.PhotoImage(ASMC_logo)
        label1 = Label(self, image=ASMC_logojov)
        label1.image = ASMC_logojov
        label1.place(relx=0.5, y=115, anchor=CENTER)
        
        
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
    app = Window()
    root.mainloop()
    
if __name__ == '__main__':
    main()