import tkinter as tk

#Creating a new window and configurations
window = tk.Tk()
window.title("Miles to km converter")
# window.minsize(width=500, height=500)
window.config(pady=30,padx=30)

input = tk.Entry(width=10)
input.grid(column=1,row=0)

#labels
font_size = 18
miles_l = tk.Label(text= 'Miles',font=('Arial',font_size,'bold'))
miles_l.grid(column= 2,row=0)
km_l = tk.Label(text= 'km',font=('Arial',font_size,'bold'))
km_l.grid(column= 2,row=1)
label = tk.Label(text= 'is equal to',font=('Arial',font_size,'bold'))
label.grid(column=0, row=1)

#button
def calculate():
    miles = input.get()
    km = float(miles) * 1.609
    answer = tk.Label(text=km,font=('Arial',font_size,'bold'))
    answer.grid(column=1,row=1)

calc_button = tk.Button(text='Calculate' ,command=calculate)
calc_button.grid(column=1,row=2)





window.mainloop()