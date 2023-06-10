import tkinter as tk
from PIL import Image, ImageTk
from tkinter import font
import base64
import os
import sys

def on_button1_click():
    selected_option = radio_var.get()
    if selected_option == "Option 1":
        label.config(image=resized_image1)
    elif selected_option == "Option 2":
        label.config(image=resized_image4)
    elif selected_option == "Option 3":
        label.config(image=resized_image7)
    elif selected_option == "Option 4":
        label.config(image=resized_image10)
    elif selected_option == "Option 5":
        label.config(image=resized_image13)
    elif selected_option == "Option 6":
        label.config(image=resized_image16)
    else:
        label.config(image=placeholder_image)

def on_button2_click():
    selected_option = radio_var.get()
    if selected_option == "Option 1":
        label.config(image=resized_image2)
    elif selected_option == "Option 2":
        label.config(image=resized_image5)
    elif selected_option == "Option 3":
        label.config(image=resized_image8)
    elif selected_option == "Option 4":
        label.config(image=resized_image11)
    elif selected_option == "Option 5":
        label.config(image=resized_image14)
    elif selected_option == "Option 6":
        label.config(image=resized_image17)
    else:
        label.config(image=placeholder_image)

def on_button3_click():
    selected_option = radio_var.get()
    if selected_option == "Option 1":
        label.config(image=resized_image3)
    elif selected_option == "Option 2":
        label.config(image=resized_image6)
    elif selected_option == "Option 3":
        label.config(image=resized_image9)
    elif selected_option == "Option 4":
        label.config(image=resized_image12)
    elif selected_option == "Option 5":
        label.config(image=resized_image15)
    elif selected_option == "Option 6":
        label.config(image=resized_image18)
    else:
        label.config(image=placeholder_image)

# Membuat jendela utama
window = tk.Tk()

font_style = font.Font(weight="bold")

# Variabel terkait radio button
radio_var = tk.StringVar()

#Membuat Frame
frame = tk.Frame(window, bg="yellow")
frame.pack(side="top")

# Mengubah ukuran gambar
new_size = (530, 530)  # Ukuran baru gambar (lebar, tinggi)

# Mendapatkan path direktori gambar yang disematkan oleh PyInstaller
image_dir = os.path.join(getattr(sys, "_MEIPASS", os.path.abspath(".")), "images")

# Memuat gambar
image1_path = os.path.join(image_dir, "GAMBAR_ASLI.png")
image2_path = os.path.join(image_dir, "KONTUR.png")
image3_path = os.path.join(image_dir, "3D.png")
image4_path = os.path.join(image_dir, "gunungsumbing.png")
image5_path = os.path.join(image_dir, "kontursumbing.png")
image6_path = os.path.join(image_dir, "plotsumbing.png")
image7_path = os.path.join(image_dir, "gunungcikurai.png")
image8_path = os.path.join(image_dir, "konturcikuray.png")
image9_path = os.path.join(image_dir, "plotcikuray.png")
image10_path = os.path.join(image_dir, "gambarsuket.png")
image11_path = os.path.join(image_dir, "kontursuket.png")
image12_path = os.path.join(image_dir, "plotsuket.png")
image13_path = os.path.join(image_dir, "gambarlawu.png")
image14_path = os.path.join(image_dir, "gambarlawu.png")
image15_path = os.path.join(image_dir, "plotlawu.png")
image16_path = os.path.join(image_dir, "gambarsindoro.png")
image17_path = os.path.join(image_dir, "gambarsindoro.png")
image18_path = os.path.join(image_dir, "plotsindoro.png")

# Membaca dan mengkonversi gambar menjadi data base64
with open(image1_path, "rb") as image_file:
    image1_data = base64.b64encode(image_file.read()).decode("utf-8")
with open(image2_path, "rb") as image_file:
    image2_data = base64.b64encode(image_file.read()).decode("utf-8")
with open(image3_path, "rb") as image_file:
    image3_data = base64.b64encode(image_file.read()).decode("utf-8")
with open(image4_path, "rb") as image_file:
    image4_data = base64.b64encode(image_file.read()).decode("utf-8")
with open(image5_path, "rb") as image_file:
    image5_data = base64.b64encode(image_file.read()).decode("utf-8")
with open(image6_path, "rb") as image_file:
    image6_data = base64.b64encode(image_file.read()).decode("utf-8")
with open(image7_path, "rb") as image_file:
    image7_data = base64.b64encode(image_file.read()).decode("utf-8")
with open(image8_path, "rb") as image_file:
    image8_data = base64.b64encode(image_file.read()).decode("utf-8")
with open(image9_path, "rb") as image_file:
    image9_data = base64.b64encode(image_file.read()).decode("utf-8")
with open(image10_path, "rb") as image_file:
    image10_data = base64.b64encode(image_file.read()).decode("utf-8")
with open(image11_path, "rb") as image_file:
    image11_data = base64.b64encode(image_file.read()).decode("utf-8")
with open(image12_path, "rb") as image_file:
    image12_data = base64.b64encode(image_file.read()).decode("utf-8")
with open(image13_path, "rb") as image_file:
    image13_data = base64.b64encode(image_file.read()).decode("utf-8")
with open(image14_path, "rb") as image_file:
    image14_data = base64.b64encode(image_file.read()).decode("utf-8")
with open(image15_path, "rb") as image_file:
    image15_data = base64.b64encode(image_file.read()).decode("utf-8")
with open(image16_path, "rb") as image_file:
    image16_data = base64.b64encode(image_file.read()).decode("utf-8")
with open(image17_path, "rb") as image_file:
    image17_data = base64.b64encode(image_file.read()).decode("utf-8")
with open(image18_path, "rb") as image_file:
    image18_data = base64.b64encode(image_file.read()).decode("utf-8")

# Membuat objek ImageTk dari gambar yang sudah diubah ukurannya
resized_image1 = ImageTk.PhotoImage(Image.open(image1_path).resize(new_size))
resized_image2 = ImageTk.PhotoImage(Image.open(image2_path).resize(new_size))
resized_image3 = ImageTk.PhotoImage(Image.open(image3_path).resize(new_size))
resized_image4 = ImageTk.PhotoImage(Image.open(image4_path).resize(new_size))
resized_image5 = ImageTk.PhotoImage(Image.open(image5_path).resize(new_size))
resized_image6 = ImageTk.PhotoImage(Image.open(image6_path).resize(new_size))
resized_image7 = ImageTk.PhotoImage(Image.open(image7_path).resize(new_size))
resized_image8 = ImageTk.PhotoImage(Image.open(image8_path).resize(new_size))
resized_image9 = ImageTk.PhotoImage(Image.open(image9_path).resize(new_size))
resized_image10 = ImageTk.PhotoImage(Image.open(image10_path).resize(new_size))
resized_image11 = ImageTk.PhotoImage(Image.open(image11_path).resize(new_size))
resized_image12 = ImageTk.PhotoImage(Image.open(image12_path).resize(new_size))
resized_image13 = ImageTk.PhotoImage(Image.open(image13_path).resize(new_size))
resized_image14 = ImageTk.PhotoImage(Image.open(image14_path).resize(new_size))
resized_image15 = ImageTk.PhotoImage(Image.open(image15_path).resize(new_size))
resized_image16 = ImageTk.PhotoImage(Image.open(image16_path).resize(new_size))
resized_image17 = ImageTk.PhotoImage(Image.open(image17_path).resize(new_size))
resized_image18 = ImageTk.PhotoImage(Image.open(image18_path).resize(new_size))
placeholder_image = ImageTk.PhotoImage(Image.open("GAMBAR_ASLI.png").resize(new_size))

# Judul
title_label = tk.Label(frame, text="Kontur Gunung 3D", font=("Arial", 16, "bold"), bg="yellow", fg="red")
title_label.config(highlightbackground="yellow", highlightcolor="yellow")
title_label.pack(pady=10)

# Membuat radio button
radio_button1 = tk.Radiobutton(frame, text="Merbabu", variable=radio_var, value="Option 1", bg="yellow", fg="red",font=font_style)
radio_button2 = tk.Radiobutton(frame, text="Sumbing", variable=radio_var, value="Option 2", bg="yellow", fg="red",font=font_style)
radio_button3 = tk.Radiobutton(frame, text="Cikuray", variable=radio_var, value="Option 3", bg="yellow", fg="red",font=font_style)
radio_button4 = tk.Radiobutton(frame, text="Suket", variable=radio_var, value="Option 4", bg="yellow", fg="red",font=font_style)
radio_button5 = tk.Radiobutton(frame, text="Lawu", variable=radio_var, value="Option 5", bg="yellow", fg="red",font=font_style)
radio_button6 = tk.Radiobutton(frame, text="Sindoro", variable=radio_var, value="Option 6", bg="yellow", fg="red",font=font_style)
radio_button7 = tk.Radiobutton(frame, text="Suket", variable=radio_var, value="Option 7", bg="yellow", fg="red",font=font_style)
radio_button8 = tk.Radiobutton(frame, text="Suket", variable=radio_var, value="Option 8", bg="yellow", fg="red",font=font_style)
radio_button9 = tk.Radiobutton(frame, text="Suket", variable=radio_var, value="Option 9", bg="yellow", fg="red",font=font_style)
radio_button10 = tk.Radiobutton(frame, text="Suket", variable=radio_var, value="Option 10", bg="yellow", fg="red",font=font_style)

# Menampilkan radio button
radio_button1.pack(side="left")
radio_button2.pack(side="left")
radio_button3.pack(side="left")
radio_button4.pack(side="left")
radio_button5.pack(side="left")
radio_button6.pack(side="left")
radio_button7.pack(side="left")
radio_button8.pack(side="left")
radio_button9.pack(side="left")
radio_button10.pack(side="left")


# Membuat label untuk menampilkan gambar
label = tk.Label(window, image=placeholder_image)
label.pack(padx=10, pady=10)

# Tombol untuk mengakses pilihan radio button
button1 = tk.Button(window, text="Gambar Gunung", command=on_button1_click)
button1.pack(pady=10)
button2 = tk.Button(window, text="Kontur Gunung", command=on_button2_click)
button2.pack(pady=10)
button3 = tk.Button(window, text="Plot", command=on_button3_click)
button3.pack(pady=10)

#Background dasar
window.configure(bg="yellow")

# Menjalankan jendela utama
window.mainloop()
