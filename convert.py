import base64

# Baca file gambar sebagai bytes
with open("GAMBAR_ASLI.png", "rb") as image_file:
    image_bytes = image_file.read()

# Konversi bytes menjadi data base64
image_data = base64.b64encode(image_bytes).decode("utf-8")

print(image_data)