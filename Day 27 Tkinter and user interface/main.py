import tkinter as tk

def button_clicked():
    new_text = input.get()
    my_label.config(text=new_text)


window = tk.Tk()# Needs to be at the beginning of program
window.title('First GUI program')
window.minsize(width=500, height=300)
window.config(padx=20, pady=20)

#Label
my_label = tk.Label(text= 'I am a label',font=('Arial',24,'bold'))
my_label.config(text='New Text')
# my_label['text'] = 'New Text'
# my_label.config(text='New text option 2')
# my_label.pack()#place into the screen and center it
my_label.grid(column=0,row=0) #This is relative to others, so it wont change if only this on grid
my_label.config(padx=50,pady=50)

#Button
button = tk.Button(text='Click me',command=button_clicked)
# button.pack()
button.grid(column=2,row=2)

new_button = tk.Button(text= 'New Button')
new_button.grid(column= 3, row=0)

#Entry component
input = tk.Entry(width=10)
input.grid(column=4,row=3)
input.get()
# input.pack()



window.mainloop() #Needs to be at the end of the program