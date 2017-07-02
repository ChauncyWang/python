import wechat
from wechat.services import login
import pyqrcode

login.getQR(login.getQRuuid())
f = open("QR.png","rb")
e = pyqrcode.QRCode().png("QR.png")
print(e)