import sys
import subprocess

try:
    import qrcode
except ImportError:
    subprocess.check_call([sys.executable, "-m", "pip", "install", "qrcode", "pillow"])
    import qrcode

qr = qrcode.QRCode()
a="Semiyaaa"
qr.add_data(a)
qr.make(fit=True)
res= qr.make_image(fill_color="black", back_color="white")
res.save("semiya.png")
print("QR code generated and saved as semiya.png")