from tkinter import *
from tkinter import Menu
from tkinter import filedialog
from tkinter import scrolledtext

# --- functions ---
def clicked():
    res = "Refresh ScrolledText."
    txt.insert(INSERT,res)

# --- main --- 
window = Tk()
window.title("Duohong File Analyzer")
window.geometry('700x500')

menu = Menu(window)
new_item = Menu(menu)
new_item.add_command(label='Open')
menu.add_cascade(label='File', menu=new_item)
window.config(menu=menu)
 
lbl = Label(window, text="Remove") 
lbl.grid(column=0, row=0)

chk_state = BooleanVar()
chk_state.set(True)
chk = Checkbutton(window, text='Remove', var=chk_state) # may be radio later
chk.grid(column=200, row=0)

btn = Button(window, text="Refresh", command=clicked)
btn.grid(column=200, row=400)

txt = scrolledtext.ScrolledText(window,width=20,height=20)
txt.grid(column=5,row=0)
txt.insert(INSERT,'Content here')
 
file = filedialog.askopenfilename(filetypes=(('text files', 'txt'),))

window.mainloop()