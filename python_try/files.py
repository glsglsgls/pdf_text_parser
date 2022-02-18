from io import StringIO
import os
import pyperclip
from sys import argv

from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfdocument import PDFDocument
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.pdfpage import PDFPage
from pdfminer.pdfparser import PDFParser



def convert_pdf_to_string(file_path):

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

def check_matching(str,condition):
    if str.find(condition)>0:
        return True
    else:
        return False


def readAllFilesInFolder():
	path="test/"
	files=os.listdir(path)
	for i in range(0,files.__len__()):
		if files[i][-4:]=='.pdf':
			cond = files[i].replace(".pdf","")
			cond = cond[:-cond.find('_')+1]
			return check_matching(convert_pdf_to_string(path + files[i]),cond)

