import pyqrcode
print("welcome to QR Code generator")
msg=input("Type your secret message:")
code=pyqrcode.create(msg)
code.png("qrcode.png",scale=5)
print("QR Code generated successfully.")
