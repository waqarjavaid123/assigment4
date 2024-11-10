import os
from tkinter import Tk, Label, Button, filedialog
from PIL import Image, ImageTk


class ImageGallery:
    def __init__(self, root):
        self.root = root
        self.root.title("Image Gallery")

        # Folder select karne ka button
        self.select_folder_button = Button(root, text="Select Image Folder", command=self.load_images)
        self.select_folder_button.pack()

        # Label to display image
        self.image_label = Label(root)
        self.image_label.pack()

        # Navigation buttons
        self.prev_button = Button(root, text="Previous", command=self.show_prev_image, state="disabled")
        self.prev_button.pack(side="left")
        
        self.next_button = Button(root, text="Next", command=self.show_next_image, state="disabled")
        self.next_button.pack(side="right")

        # Image index aur images list
        self.image_index = 0
        self.images = []

    def load_images(self):
        # Folder select karna
        folder_path = filedialog.askdirectory()
        if not folder_path:
            return

        # Folder mein sirf images ko load karna
        self.images = [os.path.join(folder_path, f) for f in os.listdir(folder_path) if f.endswith(('jpg', 'jpeg', 'png', 'gif'))]

        # Agar images hain toh pehli image dikhaye
        if self.images:
            self.image_index = 0
            self.show_image()
            self.update_buttons()

    def show_image(self):
        image_path = self.images[self.image_index]
        img = Image.open(image_path)
        img = img.resize((800, 600), Image.LANCZOS)  # Resize for better display
        photo = ImageTk.PhotoImage(img)
        
        self.image_label.config(image=photo)
        self.image_label.image = photo  # Store reference

    def show_next_image(self):
        if self.image_index < len(self.images) - 1:
            self.image_index += 1
            self.show_image()
        self.update_buttons()

    def show_prev_image(self):
        if self.image_index > 0:
            self.image_index -= 1
            self.show_image()
        self.update_buttons()

    def update_buttons(self):
        # Next/Previous buttons ko enable/disable karna
        if self.image_index == 0:
            self.prev_button.config(state="disabled")
        else:
            self.prev_button.config(state="normal")

        if self.image_index == len(self.images) - 1:
            self.next_button.config(state="disabled")
        else:
            self.next_button.config(state="normal")

# Main code
if __name__ == "__main__":
    root = Tk()
    gallery = ImageGallery(root)
    root.mainloop()
