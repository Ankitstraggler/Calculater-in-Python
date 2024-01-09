import tkinter as tk

def on_click(button_text):
    current_text = result_var.get()
    if button_text == "=":
        try:
            result_var.set(eval(current_text))
        except Exception as e:
            result_var.set("Error")
    elif button_text == "C":
        result_var.set("")
    else:
        result_var.set(current_text + button_text)

# Create the main window
window = tk.Tk()
window.title("Simple Calculator")

# Entry widget for displaying the result
result_var = tk.StringVar()
result_entry = tk.Entry(window, textvariable=result_var, justify='right', font=('Arial', 14))
result_entry.grid(row=0, column=0, columnspan=4)

# Buttons
buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', 'C', '=', '+'
]

row_val = 1
col_val = 0

for button_text in buttons:
    tk.Button(window, text=button_text, padx=20, pady=20, font=('Arial', 14),
              command=lambda bt=button_text: on_click(bt)).grid(row=row_val, column=col_val)
    col_val += 1
    if col_val > 3:
        col_val = 0
        row_val += 1

# Run the application
window.mainloop()