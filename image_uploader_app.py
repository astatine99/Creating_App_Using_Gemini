import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
from PIL import Image, ImageTk

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
        image_label.configure(image=photo_img)
        image_label.image = photo_img  # Keep a reference

# Create the main window
root = tk.Tk()
root.title("Image Uploader")

root.geometry("500x400")  # Set a specific window size

#Add some overall padding
root.configure(padx=20, pady=20)

# Style for the button
style = ttk.Style(root)
style.configure("Tbutton", font=("Helvetica", 12, "bold"), padding=10)

# Create a button to trigger image upload
upload_button = ttk.Button(root, text="Upload Image", command=upload_image)
upload_button.pack(pady=10)  # Add some padding

# Create a label to display the image
image_label = tk.Label(root)
image_label.pack()

# Start the GUI
root.mainloop()
