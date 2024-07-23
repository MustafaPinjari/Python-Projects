from tkinter import *
import random, string
import pyperclip

# Function to create a rounded rectangle
def rounded_rectangle(canvas, x1, y1, x2, y2, radius, **kwargs):
    points = [x1 + radius, y1,
              x1 + radius, y1,
              x2 - radius, y1,
              x2 - radius, y1,
              x2, y1,
              x2, y1 + radius,
              x2, y1 + radius,
              x2, y2 - radius,
              x2, y2 - radius,
              x2, y2,
              x2 - radius, y2,
              x2 - radius, y2,
              x1 + radius, y2,
              x1 + radius, y2,
              x1, y2,
              x1, y2 - radius,
              x1, y2 - radius,
              x1, y1 + radius,
              x1, y1 + radius,
              x1, y1]

    return canvas.create_polygon(points, **kwargs, smooth=True)

###initialize window
root = Tk()
root.geometry("400x200")
root.resizable(0, 0)
root.title("Musuu - The PASSWORD GENERATOR")

# Set the background color to blue
root.configure(bg='blue')

# heading
canvas = Canvas(root, bg='blue', highlightthickness=0)
canvas.pack(fill=BOTH, expand=YES)
rounded_rectangle(canvas, 10, 10, 390, 40, 20, fill='blue', outline='white')
heading = Label(canvas, text='PASSWORD GENERATOR', font='arial 15 bold', bg='blue', fg='white')
heading.pack()

Label(root, text='Musuu', font='arial 15 bold', bg='blue', fg='white').pack(side=BOTTOM)

###select password length
pass_label = Label(root, text='PASSWORD LENGTH', font='arial 10 bold', bg='blue', fg='white')
pass_label.pack()

pass_len = IntVar()
length = Spinbox(root, from_=8, to_=32, textvariable=pass_len, width=15)
length.pack()

#####define function
pass_str = StringVar()

def Generator():
    password = ''
    for x in range(0, 4):
        password = random.choice(string.ascii_uppercase) + random.choice(string.ascii_lowercase) + random.choice(
            string.digits) + random.choice(string.punctuation)
    for y in range(pass_len.get() - 4):
        password = password + random.choice(
            string.ascii_uppercase + string.ascii_lowercase + string.digits + string.punctuation)
    pass_str.set(password)

###button
Button(root, text="GENERATE PASSWORD", command=Generator, bg='red', fg='white').pack(pady=5)

Entry(root, textvariable=pass_str).pack()

########function to copy
def Copy_password():
    pyperclip.copy(pass_str.get())

Button(root, text='COPY TO CLIPBOARD', command=Copy_password, bg='green', fg='white').pack(pady=5)

# loop to run program
root.mainloop()