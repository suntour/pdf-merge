from PyPDF2 import PdfFileMerger
from tree import get_pdf_array

def generate_merged_pdfs(destination):
    pdf_array = get_pdf_array()
    merger = PdfFileMerger()

    for pdf in pdf_array:
        merger.append(pdf)

    print(destination)
    merger.write(destination)
