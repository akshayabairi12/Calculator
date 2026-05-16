import tkinter as tk

# Function to click buttons
def button_click(value):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current + str(value))

# Function to clear screen
def clear():
    entry.delete(0, tk.END)

# Function to calculate result
def calculate():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(0, result)
    except:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

# Main window
root = tk.Tk()
root.title("Calculator")
root.geometry("350x450")
root.config(bg="lightblue")

# Entry box
entry = tk.Entry(
    root,
    font=("Arial", 20),
    bd=10,
    relief=tk.RIDGE,
    justify="right"
)
entry.pack(fill="both", ipadx=8, pady=10, padx=10)

# Button frame
frame = tk.Frame(root, bg="lightblue")
frame.pack()

# Buttons layout
buttons = [
    ['7', '8', '9', '/'],
    ['4', '5', '6', '*'],
    ['1', '2', '3', '-'],
    ['0', '.', '=', '+']
]

# Create buttons
for row in buttons:
    row_frame = tk.Frame(frame, bg="lightblue")
    row_frame.pack(expand=True, fill="both")

    for btn in row:
        if btn == "=":
            button = tk.Button(
                row_frame,
                text=btn,
                font=("Arial", 18),
                command=calculate,
                height=2,
                width=5,
                bg="green",
                fg="white"
            )
        else:
            button = tk.Button(
                row_frame,
                text=btn,
                font=("Arial", 18),
                command=lambda b=btn: button_click(b),
                height=2,
                width=5
            )

        button.pack(side="left", expand=True, fill="both", padx=5, pady=5)

# Clear button
clear_button = tk.Button(
    root,
    text="Clear",
    font=("Arial", 18),
    command=clear,
    bg="red",
    fg="white"
)

clear_button.pack(fill="both", padx=10, pady=10)

# Run app
root.mainloop()