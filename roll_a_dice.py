import tkinter as tk
import random
from PIL import ImageTk,Image


window = tk.Tk()
window.title('Virtual Dice')
window.geometry('500x500')


#-----Fucntions---------


def dis():

	a = random.randint(1,6)

	b = random.randint(1,6)	

	v_dis1 = tk.Text(master = window,height=1,width=10,font = ("Helvetica",20))

	v_dis1.grid(column = 1, row = 3)

	v_dis1.insert(tk.END, a)

	v_dis2 = tk.Text(master = window,height=1,width=10,font = ("Helvetica",20))

	v_dis2.grid(column = 1, row = 4)

	v_dis2.insert(tk.END, b)
	
#-----image------

my_image = ImageTk.PhotoImage(Image.open('rolling_dice.jpg'))

#-----Labels------

# pading 1

label1 = tk.Label(text = '                         ')
label1.grid(column = 0,row = 0)

# pading 2

label2 = tk.Label(text = '            ')
label2.grid(column = 0,row = 1)

img_label = tk.Label(image = my_image)
img_label.grid(column = 1,row = 1)

# pading 3
label4 = tk.Label(text = '      ')
label4.grid(column = 0,row =2)

# pading 4

label3 = tk.Label(text = '      ')
label3.grid(column = 0,row =4)

#-----Buttons-----

button1 = tk.Button(text = 'Roll A dice',command = dis)
button1.grid(column = 1,row = 5,sticky=tk.W)

button_quit = tk.Button(text = 'Exit',command = window.quit)
button_quit.grid(column = 1,row = 5,sticky=tk.E)



window.mainloop()