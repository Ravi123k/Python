import qrcode

img = qrcode.make(
    '6396297848'
)
img.save('myQRcode.png')
img.show()
