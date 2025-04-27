# -*- coding: utf-8 -*-
"""
Created on Thu Apr 24 13:31:38 2025

@author: TadLocal
"""
import tkinter as tk
from tkinter import filedialog
import cv2
import numpy as np
from PIL import Image, ImageTk

#------------------------------ FUNCTIONS ------------------------------
#function for the button to select an image
def select_image():
    #open file explorer to select an image file
    global file_path
    file_path = filedialog.askopenfilename( filetypes=[("Image files", "*.jpg *.jpeg *.png *.bmp")] )
    if file_path:
        #load and resize image
        image = Image.open(file_path)
        image = image.resize((450, 300))
        #convert to PhotoImage so tkinter can use it
        photo = ImageTk.PhotoImage(image)
        #update label
        input_image_label.config(image=photo)
        input_image_label.image = photo

#function for edge detection
def edgeDetection():
    #global variable to hold the transformed image and file name so it can be saved later
    global transformed_image, fileName
    #convert PIL image to cv2 image
    input_image = Image.open(file_path)
    input_image = input_image.resize((450, 300))
    image_np = np.array(input_image)
    #transform image
    edges = cv2.Canny(image_np, 75, 155)
    #hold in global variable so that it can be saved later
    transformed_image = edges
    fileName = "EdgeDetectionOutput.jpg"
    #convert to PhotoImage so tkinter can use it
    edges_pil = Image.fromarray(edges)
    photo_edges = ImageTk.PhotoImage(edges_pil)
    #update label
    transformed_image_label.config(image=photo_edges)
    transformed_image_label.image = photo_edges
    
#function for gaussian blur
def gaussianBlur():
    #global variable to hold the transformed image and file name so it can be saved later
    global transformed_image, fileName
    #convert PIL image to cv2 image
    input_image = Image.open(file_path)
    input_image = input_image.resize((450, 300))
    image_np = np.array(input_image)
    #transform image
    blurred = cv2.GaussianBlur(image_np, (25,25), 0)
    #hold in global variable so that it can be saved later
    transformed_image = blurred
    fileName = "GaussianBlurOutput.jpg"
    #convert to PhotoImage so tkinter can use it
    blurred_pil = Image.fromarray(blurred)
    photo_blurred = ImageTk.PhotoImage(blurred_pil)
    #update label
    transformed_image_label.config(image=photo_blurred)
    transformed_image_label.image = photo_blurred
    
#function for median filtering
def medianFilter():
    #global variable to hold the transformed image and file name so it can be saved later
    global transformed_image, fileName
    #convert PIL image to cv2 image
    input_image = Image.open(file_path)
    input_image = input_image.resize((450, 300))
    image_np = np.array(input_image)
    #transform image
    median = cv2.medianBlur(image_np, 5)
    #hold in global variable so that it can be saved later
    transformed_image = median
    fileName = "MedianFilterOutput.jpg"
    #convert to PhotoImage so tkinter can use it
    median_pil = Image.fromarray(median)
    photo_median = ImageTk.PhotoImage(median_pil)
    #update label
    transformed_image_label.config(image=photo_median)
    transformed_image_label.image = photo_median
    
#function to save the transformed image
def saveImage():
    cv2.imwrite(fileName, transformed_image)
    #update the confirmation label
    saved_image__confirmation_label.configure(text="Image Saved!")
    

#------------------------------ GUI LAYOUT ------------------------------
root = tk.Tk()
root.title("Image Transformation GUI")
tk.Label(root, text="Image Transformation GUI")
root.geometry("1000x600")

# Buttons
#select image and display it
select_image_button = tk.Button(root, text="Select Image", command=select_image, 
                              width=20, height=2, font=("Arial", 14, "bold"), bg="lightpink", fg="red")
select_image_button.place(x=370, y=10)

#transform image to edge detection 
edge_detection_button = tk.Button(root, text="Edge Detection", command=edgeDetection, 
                              width=15, height=1, font=("Arial", 14, "bold"), bg="lightblue", fg="darkblue")
edge_detection_button.place(x=100, y=100)

#transform image to blurred 
blurred_button = tk.Button(root, text="Blurred", command=gaussianBlur, 
                              width=15, height=1, font=("Arial", 14, "bold"), bg="lightblue", fg="darkblue")
blurred_button.place(x=400, y=100)

#transform image to median filtered 
blurred_button = tk.Button(root, text="Median Filtering", command=medianFilter, 
                              width=15, height=1, font=("Arial", 14, "bold"), bg="lightblue", fg="darkblue")
blurred_button.place(x=700, y=100)

#save the transformed image
save_image_button = tk.Button(root, text="Save Image", command=saveImage, 
                              width=15, height=2, font=("Arial", 14, "bold"), bg="lightgreen", fg="darkgreen")
save_image_button.place(x=400, y=470)


# Labels
#input image label
input_image_label = tk.Label(root)
input_image_label.place(x=10, y=150)

#transformed image label
transformed_image_label = tk.Label(root)
transformed_image_label.place(x=500, y=150)

#label to confirm the image has been saved
saved_image__confirmation_label = tk.Label(root, font=("Arial", 14, "bold"), fg="darkgreen")
saved_image__confirmation_label.place(x=430, y=550)


#------------------------------ RUN GUI ------------------------------
root.mainloop()
