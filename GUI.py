import tkinter as tk
from tkinter import filedialog, messagebox, Text
import datetime

root = tk.Tk()

canvas = tk.Canvas(root, height = 600, width = 900, bg="#FFFFFF")
canvas.pack()

frame = tk.Frame(root, bg="#05014a")
frame.place(relwidth=0.8, rellheight=0.8)