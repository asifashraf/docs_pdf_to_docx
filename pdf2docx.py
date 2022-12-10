from pdf2docx import Converter
import os 
dir_path = os.path.dirname(os.path.realpath(__file__))
pdf_file = os.path.join(dir_path, 'source.pdf')
docx_file = os.path.join(dir_path, 'target.docx')

# convert pdf to docx
cv = Converter(pdf_file)
cv.convert(docx_file)      # all pages by default
cv.close()