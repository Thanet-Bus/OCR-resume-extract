
import tkinter as tk
import resume_content_extract
import threading
from tkinter import filedialog, messagebox, ttk

app = None

def setup(root_window):
    global app
    app = root_window

def center_window(window, width, height):
    # Get the screen width and height
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    # Calculate the x and y coordinates to center the window
    x = (screen_width // 2) - (width // 2)
    y = (screen_height // 2) - (height // 2)
    # Set the geometry of the window
    window.geometry(f"{width}x{height}+{x}+{y}")


# TODO: Create loading screen when process the resume files
def upload_files():
    file_path = filedialog.askopenfilenames(title = 'Select files to upload')
    if file_path:
        messagebox.showinfo("Starting", "Click OK to start extracting data.\nThis may take a while. Please wait till finish show up")
    else:
        messagebox.showwarning("Opps!!", "You didn't choose any files")
        return
    
    def worker():
        try:
            process = resume_content_extract.data_extract(file_path)
            print(process)
            app.after(0, lambda: messagebox.showinfo(
            "Finished", process
        ))
        except Exception as e:
            process = f"Error: {e}"
            app.after(0, lambda: messagebox.showinfo(
            "Error", process
        ))

    threading.Thread(target=worker, daemon=True).start()