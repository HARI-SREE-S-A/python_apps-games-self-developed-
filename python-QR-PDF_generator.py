import qrcode
from reportlab.lib.pagesizes import letter
from reportlab.lib.units import inch
from reportlab.pdfgen import canvas

# Get information from user
name = input("Enter your name: ")
email = input("Enter your email: ")
phone = input("Enter your phone number: ")

# Combine information into a single string
info = f"Name: {name}\nEmail: {email}\nPhone: {phone}"

# Generate PDF document
pdf = canvas.Canvas("my_info.pdf", pagesize=letter)
pdf.drawString(2*inch, 9*inch, "Name:")
pdf.drawString(2.5*inch, 9*inch, name)
pdf.drawString(2*inch, 8.5*inch, "Email:")
pdf.drawString(2.5*inch, 8.5*inch, email)
pdf.drawString(2*inch, 8*inch, "Phone:")
pdf.drawString(2.5*inch, 8*inch, phone)
pdf.save()

# Generate QR code containing link to PDF document
qr = qrcode.QRCode(version=1, box_size=10, border=5)
qr.add_data("https://www.pixelstalk.net/wp-content/uploads/2016/07/Wallpapers-pexels-photo.jpg")
qr.make(fit=True)

# Save QR code image
img = qr.make_image(fill_color="black", back_color="white")
img.save("my_qr_code.png")

