import qrcode as qr
img = qr.make("https://www.youtube.com/watch?v=FOGRHBp6lvM&t=4s&ab_channel=WsCubeTech")
img.save("wscube-.png") 
print(img)