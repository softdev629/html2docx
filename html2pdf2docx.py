import pdfkit
from pdf2docx import parse
pdfkit.from_file("temp.html", "temp.pdf")
parse("temp.pdf", "temp.docx")