import qrcode

print("QR Code Generator")
print("Created by @ surabhi")

data = input("Enter input >> ")

qr = qrcode.make(data)

# Make sure the path exists or use a simple filename
qr.save("C:/Users/surab/OneDrive/Desktop/qr_code.png")

print("QR Code generated and saved successfully!")
