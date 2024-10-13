import qrcode

url = "https://yourusername.github.io/your-repository/"
img = qrcode.make(url)
img.save("car_qr_code.png")
