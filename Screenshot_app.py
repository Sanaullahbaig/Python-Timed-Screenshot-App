import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import ImageGrab
import threading
import time
import os


CAPTURE_INTERVAL = 600 


is_capturing = False 
save_directory = None
status_text = None


def select_folder():
    global save_directory
    folder_selected = filedialog.askdirectory()
    
    if folder_selected:
        save_directory.set(folder_selected)
        status_text.set(f"Status: Folder set. Ready to capture.")
    else:
        status_text.set("Status: Please select a folder.")

def start_capture():
    global is_capturing
    folder_path = save_directory.get()
    
    if not folder_path or not os.path.isdir(folder_path):
        messagebox.showerror("Error", "Please select a valid destination folder.")
        return

    is_capturing = True
    status_text.set(f"Status: Capturing every 10 minutes...")
    
    start_btn.config(state=tk.DISABLED)
    stop_btn.config(state=tk.NORMAL)
    browse_btn.config(state=tk.DISABLED)

    threading.Thread(target=capture_worker, daemon=True).start()

def stop_capture():
    """Stops the capture process and resets the button states."""
    global is_capturing
    is_capturing = False
    
    status_text.set("Status: Capture stopped. Ready.")
    
    start_btn.config(state=tk.NORMAL)
    stop_btn.config(state=tk.DISABLED)
    browse_btn.config(state=tk.NORMAL)

def capture_worker():
    """The function that runs in the background, taking screenshots."""
    global is_capturing
    
    while is_capturing:
        try:
            timestamp = time.strftime("%Y%m%d_%H%M%S")
            filename = f"screenshot_{timestamp}.png"
            full_path = os.path.join(save_directory.get(), filename)

            ImageGrab.grab(all_screens=True).save(full_path, "PNG")
            
            print(f"Captured: {filename}")
            
            root.after(0, status_text.set, f"Status: Captured {filename}. Waiting 10 minutes...")

        except Exception as e:
            print(f"Error during capture: {e}")
            root.after(0, stop_capture) 
            root.after(0, messagebox.showerror, "Error", f"Capture failed: {e}")
            break

        time.sleep(CAPTURE_INTERVAL)



if __name__ == "__main__":
    root = tk.Tk()
    root.title("Simple Auto Screenshot Utility")
    root.resizable(False, False)
    root.config(bg="#F8F8F8")
    
    save_directory = tk.StringVar()
    status_text = tk.StringVar(value="Status: Ready to begin.")

    folder_frame = tk.Frame(root, bg="#F8F8F8")
    folder_frame.pack(padx=20, pady=15, fill='x')

    tk.Label(folder_frame, text="Destination Folder:", bg="#F8F8F8", font=("Arial", 10, "bold")).pack(side=tk.LEFT, padx=(0, 10))
    
    tk.Entry(folder_frame, textvariable=save_directory, width=35, font=("Arial", 9), relief=tk.FLAT).pack(side=tk.LEFT, fill='x', expand=True, ipady=4)
    
    browse_btn = tk.Button(folder_frame, text="Select Folder", command=select_folder, 
                            bg="#007ACC", fg="white", relief=tk.FLAT, font=("Arial", 9, "bold"))
    browse_btn.pack(side=tk.LEFT, padx=10)

    btn_frame = tk.Frame(root, bg="#F8F8F8")
    btn_frame.pack(padx=20, pady=10)

    start_btn = tk.Button(btn_frame, text="Start Capture", command=start_capture, 
                            bg="#4CAF50", fg="white", relief=tk.FLAT, font=("Arial", 11, "bold"), width=15, pady=8)
    start_btn.pack(side=tk.LEFT, padx=10)

    stop_btn = tk.Button(btn_frame, text="Stop Capture", command=stop_capture, 
                            bg="#F44336", fg="white", relief=tk.FLAT, font=("Arial", 11, "bold"), width=15, pady=8, state=tk.DISABLED)
    stop_btn.pack(side=tk.LEFT, padx=10)

    tk.Label(root, textvariable=status_text, bg="#F8F8F8", font=("Arial", 10)).pack(pady=(5, 20))

    root.mainloop()