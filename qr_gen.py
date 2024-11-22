import qrcode
img = qrcode.make('Sushant Gaha Magar')
type(img) # qrcode.image.pil.PilImage
img.save("sushantgahamagar.png")
