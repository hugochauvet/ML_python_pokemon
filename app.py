##############################################################################
# PYTHON PROJECT ON POKEMON DATA 
##############################################################################

import tkinter as tk
import customtkinter
import os
from PIL import Image

##### PACKAGE IMP0RTATION
import tkinter as tk
import customtkinter
import os
from PIL import Image

##### SOME DEFINITION


##### DEFAULT THEME
customtkinter.set_appearance_mode("dark")  
customtkinter.set_default_color_theme("red")

##### APP

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.title("Pokemon")
        self.geometry("700x450")
        
     
##### MAIN

if __name__ == "__main__":
    app = App()
    app.mainloop()       
        
        

