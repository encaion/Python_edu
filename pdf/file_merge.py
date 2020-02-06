# !pip install pyPdf2
from PyPDF2 import PdfFileWriter, PdfFileReader
import sys
import os

folder_name = "pdfs"
file_list = os.listdir(folder_name)
file_list.sort()

output = PdfFileWriter()

for file_name in file_list :
    input = PdfFileReader(open(folder_name + "/" + file_name, "rb"))
    for n in range(input.getNumPages()):
        output.addPage(input.getPage(n))

outputStream = open("final.pdf", "wb")
output.write(outputStream)
outputStream.close()
