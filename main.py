from fastapi import FastAPI, UploadFile, File
from app.ocr_utils import extract_text, clean_extracted_text
from app.parser import parse_lab_tests

app = FastAPI()

@app.post("/get-lab-tests")
async def get_lab_tests(file: UploadFile = File(...)):
    try:
        file_location = f"temp_{file.filename}"
        with open(file_location, "wb") as f:
            f.write(await file.read())
        
        # Extract text from the image
        raw_text = extract_text(file_location)
        
        # Clean the extracted text
        cleaned_text = clean_extracted_text(raw_text)
        
        # Parse the cleaned text to extract lab test data
        lab_results = parse_lab_tests(cleaned_text)
        
        return {
            "is_success": True,
            "results": lab_results
        }
    except Exception as e:
        return {
            "is_success": False,
            "error": str(e)
        }
