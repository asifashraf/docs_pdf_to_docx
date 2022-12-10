# https://github.com/scraperwiki/pdfminer/blob/scraperwiki/tools/pdf2html.cgi
import pdfminer
from pdfminer.pdfinterp import PDFResourceManager, process_pdf
from pdfminer.converter import HTMLConverter, TextConverter
from pdfminer.layout import LAParams
import os 

dir_path = os.path.dirname(os.path.realpath(__file__))
pdf_file = os.path.join(dir_path, 'source.pdf')
docx_file = os.path.join(dir_path, 'target.html')

rsrcmgr = PDFResourceManager()
laparams = LAParams()
converter = HTMLConverter if format == 'html' else TextConverter
device = converter(rsrcmgr, out_file, codec='utf-8', laparams=laparams)
process_pdf(rsrcmgr, device, in_file, pagenos=[1,3,5], maxpages=9)

# https://github.com/scraperwiki/scraperwiki-python/blob/master/scraperwiki/utils.py
with contextlib.closing(tempfile.NamedTemporaryFile(mode='r', suffix='.xml')) as xmlin:
    cmd = 'pdftohtml -xml -nodrm -zoom 1.5 -enc UTF-8 -noframes "%s" "%s"' % (
            pdf_file, xmlin.name.rpartition('.')[0])
    os.system(cmd + " >/dev/null 2>&1")
    result = xmlin.read().decode('utf-8')