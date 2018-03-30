import tkinter
# create:
a = tkinter.Tk()
for i in range(10):
    label = tkinter.Label(a, text=str(i))
    label.grid(column=0, row=i)
# remove from screen:
for label in a.grid_slaves():
    if int(label.grid_info()["row"]) > 10:
        label.grid_forget()
