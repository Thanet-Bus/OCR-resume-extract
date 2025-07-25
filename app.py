import tkinter as tk
import window_setting

(width, height) = 500,200
size = 20
    
app = tk.Tk()
window_setting.center_window(app, width, height)
app.title("Resume Data Extraction Prototype App")

window_setting.setup(app)
label = tk.Label(app, text="Upload resume files")
label.pack(pady=size)

upload_button = tk.Button(app, text="Upload file", command=window_setting.upload_files)
upload_button.pack(pady=size)

# TODO: create different page to show :
# - name (both english and thai)
# - email
# - phone number'
# of each resumes

app.mainloop()



