
# importing required libraries for Siva Password Generator Project
from msilib.schema import CheckBox
import random
from tkinter import *
import string
import tkinter



# creating a GUI window

window = Tk()
window.title('Password Generator')
window.geometry('500x500')

Label(window, font = ('bold', 10), text = 'PASSWORD GENERATOR').pack()

# function to generate password
def password_generate(leng):
    '''
    generates random password of given length
    leng - length
    '''
    alphabets = 'abcdefghijklmnopqrstuvwxyz'
    numbers = '0123456789'
    special_char = '@_'

    valid_char = alphabets + alphabets.upper() + numbers + special_char

    empty = '                 '
    l = Label(window, text = empty, font = ('bold', 15))
    l.place(x = 190, y = 50)
    password = ''.join(random.sample(valid_char, leng))
    # l = Label(window, text = password, font = ('bold', 15))
    l = Label(window, text = password, font = ('bold', 15))
    l.place(x = 190, y = 50)

# converting string to int value
len1 = tkinter.IntVar()
len2 = tkinter.IntVar()
len3 = tkinter.IntVar()

# creating checkboxes for user input
Checkbutton(text = '4 character', onvalue = 4,
            offvalue= 0, variable = len1).place(x = 200, y = 150)
Checkbutton(text = '6 character', onvalue = 6,
            offvalue= 0, variable = len2).place(x = 200, y = 170)
Checkbutton(text = '8 character', onvalue = 8,
            offvalue= 0, variable = len3).place(x = 200, y = 190)



# function to check the check box
def get_len():
    if len1.get() == 4:
        password_generate(4)
    elif len2.get() == 6:
        password_generate(6)
    elif len3.get() == 8:
        password_generate(8)
    else:
        password_generate(8)

Button(window, text = 'Generate', font = ('normal', 10),
      bg = 'green', command = get_len).place(x = 200, y = 100)


# run the mail loop
window.mainloop()
