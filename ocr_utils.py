import pytesseract
import re
from PIL import Image
import cv2

def clean_extracted_text(text):
    # Remove unwanted characters and extra spaces
    cleaned_text = re.sub(r'\s+', ' ', text)  # Collapse multiple spaces into a single space
    cleaned_text = re.sub(r'[^\w\s.-]', '', cleaned_text)  # Remove special characters (except for dots and hyphens)
    return cleaned_text


def preprocess_image(image_path):
    # Load the image
    img = cv2.imread(image_path)
    
    # Convert to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    # Apply Gaussian Blur to reduce noise
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)
    
    # Apply binary thresholding to make text more visible
    _, thresh = cv2.threshold(blurred, 150, 255, cv2.THRESH_BINARY)
    
    return thresh

# Apply Tesseract OCR with custom configuration
def extract_text(image_path):
    custom_config = r'--oem 3 --psm 6'  # Use OCR Engine Mode 3 and Page Segmentation Mode 6
    preprocessed = preprocess_image(image_path)
    text = pytesseract.image_to_string(preprocessed, config=custom_config)
    return text
