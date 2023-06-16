import tkinter
FONT = ("Arial", 12, "normal")


def button_clicked():
    answer = round(int(user_input.get()) * 1.609344)
    answer_label.config(text=str(answer))


window = tkinter.Tk()
window.title("Miles to Kilometer Converter")
window.config(padx=20, pady=20)

user_input = tkinter.Entry(width=10)
user_input.grid(column=1, row=0)
user_input.config()
user_input.insert(index=0, string="0")

miles_label = tkinter.Label(text="Miles", font=FONT)
miles_label.grid(column=2, row=0)

equal_label = tkinter.Label(text="is equal to", font=FONT)
equal_label.grid(column=0, row=1)

answer_label = tkinter.Label(text="0", font=FONT)
answer_label.grid(column=1, row=1)

km_label = tkinter.Label(text="Km", font=FONT)
km_label.grid(column=2, row=1)

button = tkinter.Button(text="Calculate", font=FONT, command=button_clicked)
button.grid(column=1, row=2)

window.mainloop()
