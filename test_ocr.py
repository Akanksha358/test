import pytesseract
from PIL import Image

# Set the path to the Tesseract executable explicitly
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"  # Make sure this path is correct

# Open an image (replace with your own image path)
img = Image.open("test_images/lab1.png")

# Extract text from the image
text = pytesseract.image_to_string(img)
print(text)
