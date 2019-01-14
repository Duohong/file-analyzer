from tkinter import Tk, Menu, Text, BOTH, W, N, E, S, BooleanVar, Checkbutton, END
from tkinter import filedialog
from tkinter import scrolledtext
from tkinter.ttk import Frame, Button, Label, Style


class FileAnalyzer(Frame):
    def __init__(self):
        super().__init__()   
        self.initUI()
        
    def initUI(self):
        self.master.title("Duohong File Analyzer")
        self.pack(fill=BOTH, expand=True)

        menu = Menu(self)
        new_item = Menu(menu)
        new_item.add_command(label='Open')
        menu.add_cascade(label='File', menu=new_item)
        self.master.config(menu=menu)

        self.columnconfigure(1, weight=1)
        self.columnconfigure(3, pad=7)
        self.rowconfigure(3, weight=1)
        self.rowconfigure(5, pad=7)
        
        area = Text(self)
        area.grid(row=0, column=0, columnspan=2, rowspan=1, 
            padx=5, sticky=E+W+S+N)

        self.textPad = scrolledtext.ScrolledText(self, width=50, height=40)
        self.textPad.grid(row=0, column=2, columnspan=1, rowspan=2, padx=5, sticky=E+W+S+N)
        
        chk_state = BooleanVar()
        chk_state.set(True)
        chk = Checkbutton(self, text='Remove', var=chk_state) # may be radio later
        chk.grid(column=0, row=1)

        obtn = Button(self, text="Refresh", command=self.clicked)
        obtn.grid(row=1, column=1)  

        self.openFile()      
    
    def clicked(self):
        res = "Refresh ScrolledText.\n"
        self.textPad.insert(END, res)

    def openFile(self):
        filePath = filedialog.askopenfilename(filetypes=(('text files', 'txt'),))
        file = open(filePath, "r") #filePath
        self.textPad.insert(END, file.read())


def main():
    root = Tk()
    root.geometry("700x500+300+300")
    app = FileAnalyzer()
    root.mainloop()  

if __name__ == '__main__':
    main()  

"""
# --- main --- 
txt = scrolledtext.ScrolledText(window,width=20,height=20)
txt.grid(column=5,row=0)
txt.insert(INSERT,'Content here')
"""