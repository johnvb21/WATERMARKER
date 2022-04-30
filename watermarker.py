import PyPDF2
import sys
import os
input = sysargv[1]
water_file = sysargv[2]

template = PyPDF2.PdfFileReader(open(input, 'rb'))
watermark = PyPDF2.PdfFileReader(open(water_file, 'rb'))
output = PyPDF2.PdfFileWriter()

for i in range(template.getNumPages()):
    page = template.getPage(i)
    page.mergePage(watermark.getPage(0))

    with open('watermarked_pdf', 'wb') as file:
        output.write(file)