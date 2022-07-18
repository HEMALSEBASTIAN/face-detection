import tkinter as tk   
from tkinter import messagebox
def write_text():
    print("The call can be connected!!")

parent = tk.Tk()
parent.geometry('300x100')

frame = tk.Frame(parent)
frame.pack()

#T=tk.Text(frame,height=5,width=52)

#l =tk.Label(frame, text = "Fact of the Day")
#l.config(font =("Courier", 14))
#t='Do you want to call?'

"""text_box= tk.Text(
    frame,
    height=5,
    width=10)"""
text_lab=tk.Label(parent, text='Do You want to call?').place(x=40,y=10)

#text_box.pack(side=tk.TOP)
#text_box.insert('end',t)

text_disp= tk.Button(frame, 
                   text="Yes", 
                   command=write_text
                   )

#l.pack(side=tk.CENTER)
#T.pack()
text_disp.pack(side=tk.LEFT,padx=25, pady=40)

exit_button = tk.Button(frame,
                   text="No",
                   fg="black",
                   command=quit)
exit_button.pack(side=tk.RIGHT,padx=35,pady=40)
def on_closing():
    flag=0
    #if messagebox.askokcancel("Quit", "Do you want to quit?"):
    parent.destroy()

parent.protocol("WM_DELETE_WINDOW", on_closing)
parent.mainloop()