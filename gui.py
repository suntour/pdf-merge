from tkinter import Button, Entry, END, Frame, LabelFrame, Tk, ttk
from tkinter import filedialog
from PyPDF2 import PdfFileReader
from tree import append_pdf, get_pdf_name_array, clear_tree_data
from writer import generate_merged_pdfs

root = Tk()
root.title("PDF Merge")

#Configurations side
configFrame = Frame(root, padx=20, pady=20)
configFrame.grid(row=0, column=0)

#Inner Configurations LabelFrame
configLabelFrame = LabelFrame(configFrame, padx=10, pady=5, text = 'Configuration')
configLabelFrame.grid(row=0, column=0)

#Add Button
addFileButton = Button(configLabelFrame, text="Add File", command = lambda:add_file())
addFileButton.grid(row=0, column=0, pady=5)

def select_pdf():
    file_path = filedialog.askopenfilename(initialdir = "/",title = "Select file",filetypes = (("PDF","*.pdf"),("All files","*.*")))
    return file_path

def add_file():
    file_path = select_pdf()
    file_name = file_path.rsplit('/',1)[-1]
    new_file = open(file_path, 'rb')
    
    if new_file is not None:
        new_pdf = PdfFileReader(new_file)
        append_pdf(file_name, new_pdf)
        refresh_tree_view()

#Clear Button
clear_button = Button(configLabelFrame, text="Clear All", command = lambda:clear_all())
clear_button.grid(row=0, column=1, pady=5)

def clear_all():
    clear_tree_data()
    refresh_tree_view()

#Output Items
destination_button = Button(configLabelFrame, text="Save To..", command = lambda:select_destination())
destination_button.grid(row=1, column=0, columnspan=2)

def select_destination():
    destination = filedialog.asksaveasfilename(filetypes=(("PDF","*.pdf"),("All files","*.*")))
    update_destination_entry(destination + '.pdf')

def get_destination():
    return outputEntry.get()

def update_destination_entry(destination):
        outputEntry.configure(state='normal')
        outputEntry.delete(0, END)
        outputEntry.insert(END, destination)
        outputEntry.configure(state='readonly')

outputEntry = Entry(configLabelFrame)
outputEntry.configure(state='readonly')
outputEntry.insert(END, '')
outputEntry.grid(row=2, column=0, columnspan=2, pady=5)

mergeButton = Button(configLabelFrame, text="Merge PDFs", command = lambda:merge_pdfs())
mergeButton.grid(row=3, column=0, columnspan=2, pady=5)

def merge_pdfs():
    destination = get_destination()
    if destination is not None:
        generate_merged_pdfs(destination)
    #need destination

#TreeView side
treeFrame = Frame(root, padx=20 , pady=20)
treeFrame.grid(row=0, column=1)

treeView = ttk.Treeview(treeFrame)
treeView.grid(row=0, column=0)

treeView['columns'] = ('file_name')
treeView.column('#0', width=0, stretch='NO')
treeView.heading('#0', text='')
treeView.column('file_name', width=180)
treeView.heading('file_name', text='File Name', anchor='w')

treeScrollBar = ttk.Scrollbar(treeView)
treeScrollBar.configure(command=treeView.yview)
treeView.configure(yscrollcommand=treeScrollBar.set)

def refresh_tree_view():
    clear_tree_view()
    pdf_name_array = get_pdf_name_array()
    counter = 1
    for pdf_file_name in pdf_name_array:
        treeView.insert(parent='', index='end', iid=counter, text='', values=(pdf_file_name))
        counter += 1

def clear_tree_view():
    print(treeView.get_children)
    for record in treeView.get_children():
        treeView.delete(record)

#Give row and column weight to be "responsive"
root.grid_rowconfigure(0, weight=1)
root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(1, weight=1)

root.mainloop()