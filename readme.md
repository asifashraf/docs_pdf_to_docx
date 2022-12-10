# PDF to docx and then html

$ pdf2docx convert source.pdf target.docx
$ Upload to MS Office online, Make slight change then export > Copy as Docx
$ Upload result to Google docs -> Export as HTML(Zipped)

# SETUP

$ python -m venv venv
$ source venv/bin/activate
$ pip install -r requirements.txt

# PDF to DOCX

- put file in the folder 'source.pdf'
- run $ python pdf2docx.py
- CLI: pdf2docx convert source.pdf target.docx
- wait for file 'target.docx'
