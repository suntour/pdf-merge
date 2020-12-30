pdf_array = []
pdf_name_array = []

def append_pdf(pdf_file_name, pdf_file):
    global pdf_array

    pdf_array.append(pdf_file)
    pdf_name_array.append(pdf_file_name)

def get_pdf_name_array():
    return pdf_name_array

def get_pdf_array():
    return pdf_array

def clear_tree_data():
    global pdf_name_array
    global pdf_array
    pdf_array = []
    pdf_name_array = []



