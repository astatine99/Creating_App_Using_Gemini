import tkinter as tk
import customtkinter as ctk
from tkinter import ttk
from tkinter import filedialog
from PIL import Image, ImageTk

current_mode = "dark"

def upload_image():
    """Opens a file dialog, loads the selected image, and displays it"""
    file_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.jpg;*.jpeg;*.png")])
    if file_path:  # Check if a file was chosen
        # Load the image using PIL (Pillow)
        img = Image.open(file_path)

        # Resize the image if you'd like (optional)
        resized_img = img.resize((640, 480), Image.LANCZOS)  # Resize to 250x250

        # Convert to PhotoImage object (compatible with Tkinter)
        photo_img = ImageTk.PhotoImage(resized_img)

        # Update the image label with the new image
        image_label.configure(image=photo_img, text="Uploaded Image")
        image_label.image = photo_img  # Keep a reference

def toggle_theme():
    global current_mode
    if current_mode == "dark":
        ctk.set_appearance_mode("light")
        current_mode = "light"
    else:
        # Configure light mode colors here
        ctk.set_appearance_mode("dark")
        current_mode = "dark"

def update_image_label():
    """Updates the image label with the uploaded image"""
    image_label.configure(text="Image uploaded!")

# Create the main window
root = ctk.CTk()
root.title("Image Uploader")

root.geometry("500x400")  # Set a specific window size

#Add some overall padding
root.configure(padx=20, pady=20)

# Style for the button
style = ttk.Style(root)
style.configure("Tbutton", font=("Helvetica", 12, "bold"), padding=10)

# Customize button style (optional)
button_style = ctk.CTkButton(master=root, corner_radius=8)  
button_style.configure(text="Upload Image", command=upload_image)
button_style.pack(pady=10)

image_label = ctk.CTkLabel(root, text="No image uploaded", font=("Helvetica", 16) )
image_label.pack(pady=15)

# Create a button to toggle the theme
current_mode = "light"  # Initial mode

theme_button = ctk.CTkButton(root, corner_radius=8, text="Toggle Theme", command=toggle_theme)
theme_button.pack(pady=10)

# Start the GUI
root.mainloop()









