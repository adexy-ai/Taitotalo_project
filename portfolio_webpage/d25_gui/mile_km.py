from tkinter import *
# Window gui
window = Tk()
window.title('Miles to Kilometer Converter')
window.minsize(width=500, height=400)
window.config(padx=50, pady=50)

# Mile label
my_label = Label(text='Miles', font=('Arial', 24, 'bold'))
my_label.grid(column=4, row=0)

# Km label
my_label = Label(text='Km', font=('Arial', 24, 'bold'))
my_label.grid(column=4, row=2)

# is equal label
my_label = Label(text='is equal to', font=('Arial', 24, 'bold'))
my_label.grid(column=0, row=2)

# label for conversion result
my_label = Label(text= 0, font=('Arial', 24, 'bold'))
my_label.grid(column=2, row=2)
     
# Function for changing label
def clicked__():
    my_label['text'] = cacl()
    #my_label.grid(column=0, row=0)


def cacl():
    mile = int(my_input.get())
    km = mile * 1.60934
    return round(km, 2)
    
    
    #my_label.pack()


# Calculate button
button = Button(text='Calculate', command=clicked__)
button.grid(column=2, row=4)


# input entry for taking the number 
my_input = Entry(text='Enter distance: Miles', width=10)
my_input.grid(column=2, row=0, padx=20, pady=20)



# The second button which we may not need for the final project
# button2 = Button(text='This is a new button')
# button2.grid(column=0, row=3)






window.mainloop()