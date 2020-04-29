import tkinter as tk
from tkinter import filedialog,ttk
import os



def add_file(fileroot):
    filename_img_title_full = filedialog.askopenfilename(initialdir=fileroot,title='Select Image')
    filename_img_title = os.path.basename(filename_img_title_full)
    print(filename_img_title)
    return filename_img_title_full, filename_img_title