import pyperclip
from sys import argv

def get_text_from_pdf(path):    
    import fitz  # this is pymupdf
    with fitz.open(path) as doc:
        text = ""
        for page in doc:
            text += page.getText()
        return text

# took 36.5 seconds for 10 files
# Some problems with revision number

filePath = argv
#"C:/mytemp/z.pdf"
#filePath = ["123","C:/Users/sglazkov/Documents/pythonProject/pdfReader/test/079322C-AWP1A-300-CS-KMD-06810-D-0726_01.pdf"]
#print(get_pdf_info(filePath[1]))
pyperclip.copy(get_text_from_pdf(filePath[1]))
