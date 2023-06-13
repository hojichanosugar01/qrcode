#pip install qrcode[pil]
#pip install opencv-python

import qrcode
import cv2

# Function to generate a QR code from text
def generate_qr_code(text, filename):
    qr = qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_L, box_size=10, border=4)
    qr.add_data(text)
    qr.make(fit=True)

    image = qr.make_image(fill_color="black", back_color="white")
    image.save(filename)
    print(f"QR code saved as {filename}")

# Function to decode a QR code from an image file
def decode_qr_code(filename):
    image = cv2.imread(filename)
    detector = cv2.QRCodeDetector()
    data, points, _ = detector.detectAndDecode(image)

    if data:
        print(f"Decoded QR code: {data}")
    else:
        print("QR code not found or could not be decoded")

# Main program
def main():
    choice = input("Enter 'E' to encode a QR code or 'D' to decode a QR code: ").upper()

    if choice == 'E':
        text = input("Enter the text to encode: ")
        filename = input("Enter the filename to save the QR code (e.g., qr_code.png): ")
        generate_qr_code(text, filename)
    elif choice == 'D':
        filename = input("Enter the filename of the QR code image to decode: ")
        decode_qr_code(filename)
    else:
        print("Invalid choice. Please enter 'E' or 'D'.")

# Start the program
main()
