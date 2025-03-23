import pyautogui
import tkinter as tk
import keyboard
from tkinter import messagebox

# Define the macro function (automating some actions)
def run_macro():
    print("Macro started...")
    pyautogui.moveTo(500, 300)
    pyautogui.click()
    pyautogui.write('Hello, starting the macro with a button click!')
    pyautogui.press('enter')
    pyautogui.moveTo(700, 500)
    pyautogui.rightClick()
    messagebox.showinfo("Macro Status", "Macro has finished running!")  # Notify the user when the macro is done

# Function to create a simple GUI with a button to start the macro
def create_gui():
    # Create the main window
    root = tk.Tk()
    root.title("Macro Starter")
    root.geometry("300x200")

    # Add a label
    label = tk.Label(root, text="Click the button to start the macro", font=("Arial", 12))
    label.pack(pady=20)

    # Add a button that starts the macro when clicked
    start_button = tk.Button(root, text="Start Macro", font=("Arial", 12), command=run_macro)
    start_button.pack(pady=10)
    
    # Run the tkinter event loop
    root.mainloop()
    if keyboard.is_pressed("]"):
        root.destroy
# Call the function to create the GUI
create_gui()
