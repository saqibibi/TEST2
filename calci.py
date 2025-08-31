import tkinter as tk

def click(event):
    text = event.widget.cget("text")
    if text == "=":
        try:
            result = str(eval(screen.get()))
            screen.delete(0, tk.END)
            screen.insert(0, result)
        except Exception as e:
            screen.delete(0, tk.END)
            screen.insert(0, "Error")
    elif text == "C":
        screen.delete(0, tk.END)
    else:
        screen.insert(tk.END, text)

root = tk.Tk()
root.title("Simple Calculator")

screen = tk.Entry(root, font="Arial 20", borderwidth=3, relief=tk.RIDGE)
screen.pack(padx=10, pady=10, fill=tk.BOTH)

button_frame = tk.Frame(root)
button_frame.pack()

buttons = [
    ["7", "8", "9", "/"],
    ["4", "5", "6", "*"],
    ["1", "2", "3", "-"],
    ["C", "0", "=", "+"]
]

for row_values in buttons:
    row = tk.Frame(button_frame)
    row.pack(expand=True, fill="both")
    for value in row_values:
        btn = tk.Button(row, text=value, font="Arial 18", width=4, height=2)
        btn.pack(side=tk.LEFT, expand=True, fill="both")
        btn.bind("<Button-1>", click)

root.mainloop()
