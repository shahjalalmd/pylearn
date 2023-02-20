import qrcode as qr
img = qr.make("https://www.youtube.com/@codewithkiran/playlists")
img.save("qrsqure_youtub.png")