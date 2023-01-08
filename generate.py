import qrcode
img = qrcode.make("https://aniketshaw.me/")
img.save('QRCode.jpg')

#pip install qrcode
#pip install image