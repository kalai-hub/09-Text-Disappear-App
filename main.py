from tkinter import *

BACKGROUND_COLOR = "#B1DDC6"

user_text = ""
timer = None


# After user starts typing timer start if user stops typing
def start_calculating(event):
    global timer, user_text

    if timer is not None:
        window.after_cancel(timer)

    if event.keysym == "BackSpace":
        user_text = user_text[0: len(user_text) - 1]
        timer = window.after(5000, reset_app)

    elif event.char:
        user_text += event.char
        timer = window.after(5000, reset_app)

    return


# Deleting Text
def reset_app():
    global timer, user_text
    input_text.delete('1.0', 'end')
    user_text = ""
    timer = None
    return


# Save the text
def save_text():
    global user_text
    if user_text == "":
        return
    try:
        f = open('my_work.txt', 'r')
    except FileNotFoundError:
        f = open('my_work.txt', 'w')
        f.write(user_text)
        user_text = ""
        return
    else:
        cont = f.read()
        if cont == "":
            text_to_write = user_text
        else:
            text_to_write = f'\n{user_text}'

        with open('my_work.txt', 'a') as f:
            f.write(text_to_write)
            user_text = ""
    finally:
        return


window = Tk()
window.title("Typing speed calculator")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

# Label
l = Label(window, text='Do not stop typing or your work will be lost', padx=10, pady=10)
l.config(font=("Courier", 14))

# Input Text
input_text = Text(window, height=7,
                  width=75,
                  bg="light yellow",
                 )

input_text.bind('<KeyPress>', start_calculating)

# Save Button
save = Button(text='Save',
              highlightthickness=0, border=3,
              command=save_text, width=50)

l.grid(row=2, column=0, columnspan=3, padx=10, pady=10)
input_text.grid(row=3, column=0, columnspan=3)
input_text.focus_set()
save.grid(row=4, column=2, padx=10, pady=10)

window.mainloop()
