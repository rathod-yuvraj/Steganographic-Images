from tkinter import *
from tkinter import filedialog, messagebox, simpledialog
from imageStegHelper import ImageSteg

class StegGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Image Steganography")
        self.root.geometry("500x400")

        self.img_steg = ImageSteg()

        # Labels
        self.label = Label(root, text="Image Steganography Tool", font=("Arial", 18))
        self.label.pack(pady=20)

        # Encode Section
        self.encode_frame = LabelFrame(root, text="Encode Message", padx=10, pady=10)
        self.encode_frame.pack(fill="both", expand="yes", padx=20, pady=10)

        self.select_image_btn = Button(self.encode_frame, text="Select Image", command=self.select_image_for_encode)
        self.select_image_btn.grid(row=0, column=0, padx=10, pady=10)

        self.message_label = Label(self.encode_frame, text="Enter Message:")
        self.message_label.grid(row=1, column=0, padx=10, pady=10)

        self.message_entry = Entry(self.encode_frame, width=50)
        self.message_entry.grid(row=1, column=1, padx=10, pady=10)

        self.encode_btn = Button(self.encode_frame, text="Encode", command=self.encode_message)
        self.encode_btn.grid(row=2, column=0, columnspan=2, pady=10)

        # Decode Section
        self.decode_frame = LabelFrame(root, text="Decode Message", padx=10, pady=10)
        self.decode_frame.pack(fill="both", expand="yes", padx=20, pady=10)

        self.select_image_decode_btn = Button(self.decode_frame, text="Select Image", command=self.select_image_for_decode)
        self.select_image_decode_btn.grid(row=0, column=0, padx=10, pady=10)

        self.decoded_message_label = Label(self.decode_frame, text="Decoded Message:")
        self.decoded_message_label.grid(row=1, column=0, padx=10, pady=10)

        self.decoded_message_text = Text(self.decode_frame, width=50, height=5)
        self.decoded_message_text.grid(row=1, column=1, padx=10, pady=10)

        self.decode_btn = Button(self.decode_frame, text="Decode", command=self.decode_message)
        self.decode_btn.grid(row=2, column=0, columnspan=2, pady=10)

        # Exit Button
        self.exit_button = Button(root, text="Exit", command=root.quit)
        self.exit_button.pack(pady=10)

    def select_image_for_encode(self):
        self.image_path = filedialog.askopenfilename(title="Select Image to Hide Message")
        if not self.image_path:
            messagebox.showerror("Error", "Please select an image file.")

    def encode_message(self):
        if not hasattr(self, 'image_path') or not self.image_path:
            messagebox.showerror("Error", "Please select an image file.")
            return

        message = self.message_entry.get()
        if not message:
            messagebox.showerror("Error", "Please enter a message.")
            return

        try:
            target_path = filedialog.askdirectory(title="Select Directory to Save Encrypted Image")
            if not target_path:
                messagebox.showerror("Error", "Please select a directory to save the encrypted image.")
                return

            save_path = self.img_steg.encrypt_text_in_image(self.image_path, message, target_path)
            messagebox.showinfo("Success", f"Message encrypted and saved at: {save_path}")
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def select_image_for_decode(self):
        self.decode_image_path = filedialog.askopenfilename(title="Select Image to Decode Message")
        if not self.decode_image_path:
            messagebox.showerror("Error", "Please select an image file.")

    def decode_message(self):
        if not hasattr(self, 'decode_image_path') or not self.decode_image_path:
            messagebox.showerror("Error", "Please select an image file.")
            return

        try:
            message = self.img_steg.decrypt_text_in_image(self.decode_image_path)
            self.decoded_message_text.delete(1.0, END)
            self.decoded_message_text.insert(END, message)
        except Exception as e:
            messagebox.showerror("Error", str(e))

if __name__ == "__main__":
    root = Tk()
    gui = StegGUI(root)
    root.mainloop()
