import qrtools
from base64 import b64decode


qr = qrtools.QR()
qr.decode('qr1.png')

response = str(qr.data).decode('base64', 'strict')

print response

