from tkinter import *
import random
import string


def generate_random_password():
    length = len_password.get()
    characters = string.ascii_letters + string.digits + string.punctuation
    cur_password = ''.join(random.choice(characters) for _ in range(length))
    final_password.set(cur_password)


window = Tk()
window.geometry("400x300")
window.title("Random Password Generator")

final_password = StringVar()
len_password = IntVar()

len_password.set(0)


Label(window, text="Password Generator Application", font="calibri 20 bold").pack()
Label(window, text="Enter password length").pack(pady=5)
Entry(window, textvariable=len_password).pack(pady=5)
Button(window, text="Click button to generate", command=generate_random_password).pack(pady=10)
Label(window, text="Your Generated password").pack(pady=5)
Entry(window, textvariable=final_password).pack(pady=5)


window.mainloop()
