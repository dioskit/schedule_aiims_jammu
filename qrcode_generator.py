import qrcode

# Replace with your GitHub Pages URL
github_pages_url = "https://dioskit.github.io/schedule_aiims_jammu/"

# Generate the QR code
qr = qrcode.QRCode(
    version=1,  # Controls the size of the QR code (1 is the smallest, 40 is the largest)
    error_correction=qrcode.constants.ERROR_CORRECT_L,  # Error correction level
    box_size=10,  # Size of each box in the QR code
    border=4,  # Border size around the QR code
)

# Add the data (your GitHub Pages URL) to the QR code
qr.add_data(github_pages_url)
qr.make(fit=True)

# Create an image from the QR code
img = qr.make_image(fill_color="black", back_color="white")

# Save the image
img.save("github_qrcode.png")

print(f"QR code generated successfully for: {github_pages_url}")