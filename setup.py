import sys
from cx_Freeze import setup, Executable

build_exe_options = {
    "packages": ["tkinter", "PIL"],
    "include_files": [
        ("GAMBAR_ASLI.png", "3D.png"),
         ("cikurayplot.png","gunungcikurai.png"),
         ("gunungsumbing.png","KONTUR.png"),
         ("konturcikuray.png","kontursumbing.png"),
         ("plotsumbing.png"),  # Ganti dengan daftar file gambar yang diperlukan
                      # Tambahkan daftar file gambar lainnya di sini
     ],
 # Hanya perlu diaktifkan jika menggunakan Python versi 3.8 atau lebih baru
}

base = None
if sys.platform == "win32":
    base = "Win32GUI"  # Gunakan ini jika ingin menjalankan aplikasi tanpa konsol pada Windows

executables = [
    Executable("guigunung.py", base=base),  # Ganti dengan nama file skrip Anda
]

setup(
    name="GUI KONTUR 3D",
    version="1.0",
    description="UAS",
    options={"build_exe": build_exe_options},
    executables=executables
)
