from io import StringIO
import pyperclip
from sys import argv

from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfdocument import PDFDocument
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.pdfpage import PDFPage
from pdfminer.pdfparser import PDFParser

def convert_pdf_to_string(file_path):
	if file_path=="":
		print("path is empty")
	output_string = StringIO()
	with open(file_path, 'rb') as in_file:
		parser = PDFParser(in_file)
		doc = PDFDocument(parser)
		rsrcmgr = PDFResourceManager()
		device = TextConverter(rsrcmgr, output_string, laparams=LAParams())
		interpreter = PDFPageInterpreter(rsrcmgr, device)
		for page in PDFPage.create_pages(doc):
			interpreter.process_page(page)
	return(output_string.getvalue())

# took 60 seconds for 10 files
# all files are completely correct
#filePath = argv
filePath = ["123","C:/Users/sglazkov/Documents/123/079322C-GWP5B-100-CS-KMD-00560-M-0001_01.pdf"]
pyperclip.copy(convert_pdf_to_string(filePath[1]))
