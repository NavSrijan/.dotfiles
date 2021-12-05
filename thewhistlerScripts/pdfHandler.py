#!/bin/python3
import PyPDF2


def PDFsplit(pdf):
    # creating input pdf file object
    pdfFileObj = open(pdf, 'rb')
     
    # creating pdf reader object
    pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
     
    # starting index of first slice

    pdfWriter = PyPDF2.PdfFileWriter()

    outputpdfO = pdf.split('.pdf')[0] + 'O.pdf'
    
    end = pdfReader.getNumPages()

    # adding pages to pdf writer object
    for page in range(0, end, 2):
        pdfWriter.addPage(pdfReader.getPage(page))
         
    # writing split pdf pages to pdf file
    with open(outputpdfO, "wb") as f:
            pdfWriter.write(f)

    pdfWriter = PyPDF2.PdfFileWriter()

    outputpdfE = pdf.split('.pdf')[0] + 'E.pdf'

    for page in range(1, end, 2):
        pdfWriter.addPage(pdfReader.getPage(page))

    with open(outputpdfE, "wb") as f:
        pdfWriter.write(f)
