import requests

url = "http://127.0.0.1:8000/get-lab-tests"
file_path = "test_images/lab1.png"  # Replace with your image file path

with open(file_path, "rb") as f:
    files = {"file": ("image.jpg", f, "image/jpeg")}
    response = requests.post(url, files=files)

print("Response status:", response.status_code)
print("Response JSON:", response.json())
