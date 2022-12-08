##############################################################################
# PYTHON PROJECT ON POKEMON DATA 
##############################################################################

##### PACKAGE IMP0RTATION
import tkinter as tk
import customtkinter as ctk
import os
from PIL import Image

##### SOME DEFINITION

##### IMAGES
image_path = os.path.join(os.getcwd(), "images")
pokeball_image = ctk.CTkImage(Image.open(os.path.join(image_path, "pokeball.png")), size = (26,26))
pokedex_image = ctk.CTkImage(Image.open(os.path.join(image_path, "pokedex.png")), size = (20,20))

##### DEFAULT THEME
ctk.set_appearance_mode("dark")  
ctk.set_default_color_theme("dark-blue")

##### APP
class App(ctk.CTk):
    ### Constructor
    def __init__(self):
        super().__init__()

        ## Window
        self.title("Pokemon")
        self.geometry("700x450")

        ## Grid layout
        self.grid_rowconfigure(0, weight = 1)
        self.grid_columnconfigure(1, weight = 1)

        ## Navigation Frame
        # Structure
        self.navigation_frame = ctk.CTkFrame(self, corner_radius = 0)
        self.navigation_frame.grid(row = 0, column = 0, sticky = "nsew")
        self.navigation_frame.grid_rowconfigure(4, weight = 1)
        # Label
        self.navigation_frame_label = ctk.CTkLabel(self.navigation_frame, text = " Pokemon project", image = pokeball_image, compound = "left", font = ctk.CTkFont(size = 15, weight = "bold"))
        self.navigation_frame_label.grid(row = 0, column = 0, padx = 20, pady = 20)
        # Pokedex button
        self.pokedex_button = ctk.CTkButton(self.navigation_frame, corner_radius = 0, height = 40, border_spacing = 10, text = "Pokedex", fg_color = "transparent", text_color = ("red", "white"), image = pokedex_image, anchor = "w", command = self.pokedex_button_event)
        self.pokedex_button.grid(row = 1, column = 0, sticky = "ew")
    
        ## Pokedex Frame
        self.pokedex_frame = ctk.CTkFrame(self, corner_radius = 0, fg_color = "transparent")
        self.pokedex_frame.grid_columnconfigure(0, weight = 1)

    ### Change Frame
    def select_frame(self, name):
        ## Color for selected button
        self.pokedex_button.configure(fg_color = ("red", "red") if name == "pokedex" else "transparent")

        ## Show selected frame
        if name == "pokedex":
            self.pokedex_frame.grid(row = 0, column = 1, sticky = "nsew")
        else:
            self.pokedex_frame.grid_forget()

    ### Go to pokedex page
    def pokedex_button_event(self):
        self.select_frame("pokedex")




##### MAIN
if __name__ == "__main__":
    app = App()
    app.mainloop()       
        
        

