from time import strftime
from tkinter import Label, Tk

# Create the main window
window = Tk()
window.title("Digital Clock")  # Set a title for the window
window.geometry("200x80")       # Corrected the window size format
window.configure(bg="black")    # Set the background color to black
window.resizable(False, False) # Disable resizing

# Create and configure the label
clock_label = Label(window, bg="black", fg="white", font=("Times", 30, 'bold'), relief='flat')
clock_label.place(x=20, y=20)

# Function to update the label with the current time
def updating_label():
    current_time = strftime('%H:%M:%S')  # Format the current time
    clock_label.configure(text=current_time)  # Update the label text
    clock_label.after(1000, updating_label)  # Schedule the function to be called after 1 second

# Start updating the label
updating_label()

# Run the application
window.mainloop()
