from tkinter import *
from tkinter import ttk

root = Tk()
root.title("PDF Merge")

#Configurations side
configFrame = Frame(root, padx=20, pady=20)
configFrame.grid(row=0, column=0)

#Inner Configurations LabelFrame
configLabelFrame = LabelFrame(configFrame, padx=10, pady=5, text = 'Configuration')
configLabelFrame.grid(row=0, column=0)

#Add/Remove Buttons
addFileButton = Button(configLabelFrame, text="Add File")
addFileButton.grid(row=0, column=0, pady=5)

removeButton = Button(configLabelFrame, text="Remove")
removeButton.grid(row=0, column=1, pady=5)

#Output Items
outputLabel = Label(configLabelFrame, text="Save Output As..")
outputLabel.grid(row=1, column=0, columnspan=2)

outputEntry = Entry(configLabelFrame)
outputEntry.insert(END, 'Output.pdf')
outputEntry.grid(row=2, column=0, columnspan=2)

mergeButton = Button(configLabelFrame, text="Merge PDFs")
mergeButton.grid(row=3, column=0, columnspan=2, pady=10)

progressBar = ttk.Progressbar(configLabelFrame, length=180)
progressBar.grid(row=4, column=0, columnspan=2, pady=10)

#TreeView side
treeFrame = Frame(root, padx=20 , pady=20)
treeFrame.grid(row=0, column=1)

treeView = ttk.Treeview(treeFrame)
treeView.grid(row=0, column=0)

treeView.column('#0', width=180)
treeView.heading('#0', text='File Name', anchor='w')

treeScrollBar = ttk.Scrollbar(treeView)
treeScrollBar.configure(command=treeView.yview)
treeView.configure(yscrollcommand=treeScrollBar.set)

#Give row and column weight to be "responsive"
root.grid_rowconfigure(0, weight=1)
root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(1, weight=1)

root.mainloop()