import pyqrcode
from base64 import b64decode

li = {"Name" : "Dushyant"}
encoded_li = str(li).encode('base64','strict')

print encoded_li

qr = pyqrcode.create(encoded_li)
qr.png('qr1.png', scale=5)
