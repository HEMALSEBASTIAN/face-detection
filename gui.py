import tkinter as tk   

def write_text():
    print("The call can be connected!!")

parent = tk.Tk()
parent.geometry('100x100')

frame = tk.Frame(parent)
frame.pack()

#T=tk.Text(frame,height=5,width=52)

#l =tk.Label(frame, text = "Fact of the Day")
#l.config(font =("Courier", 14))
t='Do you want to call?'

text_box= tk.Text(
    frame,
    height=5,
    width=10)
text_box.pack(side=tk.TOP)
text_box.insert('end',t)

text_disp= tk.Button(frame, 
                   text="Yes", 
                   command=write_text
                   )

#l.pack(side=tk.CENTER)
#T.pack()
text_disp.pack(side=tk.LEFT)

exit_button = tk.Button(frame,
                   text="No",
                   fg="black",
                   command=quit)
exit_button.pack(side=tk.RIGHT)

parent.mainloop()