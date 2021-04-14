import qrcode
qr = qrcode.QRCode(version=1, border=5, box_size=15,)

data = 'Hello this is testing qr code'
qr.add_data(data)
qr.make(fit=True)
img=qr.make_image(fill='white', back_color='white',)
img.save('qr.png')