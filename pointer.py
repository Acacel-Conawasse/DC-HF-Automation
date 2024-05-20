import tkinter as tk
import pyautogui

def update_position():
    x, y = pyautogui.position()  # Get the current mouse position
    position_label.config(text=f"Mouse Position: x={x}, y={y}")
    root.after(100, update_position)  # Update the position every 100 milliseconds

# Create the main window
root = tk.Tk()
root.title("Mouse Pointer Coordinates")

# Label to display the mouse coordinates
position_label = tk.Label(root, text="", font=("Helvetica", 16))
position_label.pack(pady=20)

# Start updating the mouse position
update_position()

# Start the GUI
root.mainloop()
