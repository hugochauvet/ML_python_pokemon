##############################################################################
# PYTHON PROJECT ON POKEMON DATA 
##############################################################################

##### PACKAGE IMP0RTATION
import tkinter as tk
from tkinter.filedialog import askopenfile, askopenfilename
import customtkinter as ctk
import os
from PIL import Image, ImageTk
import cv2
import numpy as np
from keras.models import load_model, Model
import subprocess
import tensorflow as tf

##### SOME DEFINITION
global model
model_path = os.path.join(os.getcwd(), "model.h5")
model = tf.keras.models.load_model(model_path)

##### IMAGES
image_path = os.path.join(os.getcwd(), "images")
pokeball_image = ctk.CTkImage(Image.open(os.path.join(image_path, "pokeball.png")), size = (26,26))
pokedex_image = ctk.CTkImage(Image.open(os.path.join(image_path, "pokedex.png")), size = (20,20))
pokeball_open_image = ctk.CTkImage(Image.open(os.path.join(image_path, "pokeball_open.png")), size = (200,200))

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
        self.geometry("1000x700")

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
    
    ### Pokedex Frame
        ## Pokemon image selection
        self.pokedex_frame = ctk.CTkFrame(self, corner_radius = 0, fg_color = "transparent")
        self.pokedex_frame.grid_columnconfigure(0, weight = 1)
        # Label
        self.pokedex_label = ctk.CTkLabel(self.pokedex_frame, text = "POKEDEX", text_color = 'white')
        self.pokedex_label.grid(row = 0, column = 0, padx = 20, pady = 20)
        # Button to select an image
        self.pokedex_button_select_image = ctk.CTkButton(self.pokedex_frame, text = "Select a pokemon image", command = self.select_image, fg_color = 'red')
        self.pokedex_button_select_image.grid(row = 1, column = 0, padx = 25, pady = 10)
        ## Show the pokemon selected
        self.pokemon_selected_image = ctk.CTkLabel(self.pokedex_frame, text = "", image = pokeball_open_image, padx = 10, pady = 20)
        self.pokemon_selected_image.grid(row = 2, column = 0, padx = 10, pady = 10)

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

    ### Selection of the image to test
    def select_image(self):
        ## Images input
        # Select the path
        initialdir = os.getcwd()
        image_path = askopenfilename(initialdir = initialdir, filetypes = [ ('Image File', '*.*') ], title = "Select a pokemon image")
        # Read the image
        photo = ctk.CTkImage(Image.open(image_path), size = (160,160))
        # Show the image
        self.pokemon_selected_image.configure(image = photo)
        ## CNN Model
        # definiations
        img_height = 256
        img_width = 256
        class_names = ['Bulbasaur', 'Charmander', 'Mew', 'Pikachu', 'Squirtle']
        # predictions
        image_to_predict = tf.keras.utils.load_img(image_path, target_size = (img_height, img_width))
        img_array = tf.keras.utils.img_to_array(image_to_predict)
        img_array = tf.expand_dims(img_array, 0)
        predictions = model.predict(img_array)
        score = tf.nn.softmax(predictions[0])
        pokemon_predicted = class_names[np.argmax(score)]
        ## Prediction
        self.pokemon_predict_label = ctk.CTkLabel(self.pokedex_frame, text = "The pokedex prediction ({:.2f}%) is :".format(100*np.max(score)), padx = 10, pady = 20)
        self.pokemon_predict_label.grid(row = 3, column = 0, padx = 15, pady = 10)
        ## Pokemon predicted
        # Load the image
        pokemon_predicted_img = ctk.CTkImage(Image.open(os.path.join(os.getcwd(),"images_prediction", pokemon_predicted + ".png")), size = (200,200))
        # Show pokemon predicted
        self.pokemon_predicted_image = ctk.CTkLabel(self.pokedex_frame, text = "", image = pokemon_predicted_img, padx = 10, pady = 20)
        self.pokemon_predicted_image.grid(row = 4, column = 0, padx = 5, pady = 10)


        
        

        
        

        




##### MAIN
if __name__ == "__main__":
    app = App()
    app.mainloop()       
        
        

