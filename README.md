```md
# 📸 Auto Screenshot Utility  
A simple **Tkinter-based Desktop Screenshot App** that automatically captures full-screen screenshots every **10 minutes** and saves them to a folder selected by the user.

This tool is useful for:  
✔️ Monitoring work progress  
✔️ Passive activity tracking  
✔️ Classroom/workplace documentation  
✔️ Background screen recording (as images)

---

## 🚀 Features

- 🖼️ **Full-screen auto screenshot** using `PIL.ImageGrab`
- ⏱️ **Captures every 10 minutes** (600 seconds)
- 📁 **Choose destination folder** using a file dialog
- ▶️ **Start capturing** anytime
- ⛔ **Stop capturing** safely
- 🧵 **Runs in background** using threads (app stays responsive)
- 📌 Clean and simple Tkinter UI
- 💾 Saves files in format:
  ```
  screenshot_YYYYMMDD_HHMMSS.png
  ```

---

## 🛠️ Requirements

Install the required packages:

```bash
pip install pillow
```

Tkinter comes built-in with Python on Windows & Linux.  
If missing on macOS:

```bash
brew install python-tk
```

---

## 📦 How to Run

1. Save the script as:

```
auto_screenshot.py
```

2. Run it:

```bash
python auto_screenshot.py
```

---

## 📁 Screenshot Saving Format

Each screenshot is saved with a timestamp:

Example:

```
screenshot_20250214_103045.png
```

---

## 🧩 How It Works

### **1. Folder Selection**
User selects a destination folder using:

```python
filedialog.askdirectory()
```

The path is stored in a `StringVar()`.

---

### **2. Start Capture**
When **Start Capture** is clicked:

- Checks if folder exists  
- Disables buttons  
- Starts a background thread:
  ```python
  threading.Thread(target=capture_worker, daemon=True).start()
  ```

---

### **3. Background Screenshot Worker**
The `capture_worker()` function:

- Captures full screen:
  ```python
  ImageGrab.grab(all_screens=True)
  ```
- Saves as PNG  
- Waits 10 minutes  
- Repeats until user stops capturing  

---

### **4. Stop Capture**
Clicking stop:

- Sets `is_capturing = False`  
- Restores button states  
- Updates status text  

---

## 🖼️ User Interface Overview

### Buttons:
- **Start Capture** → Begin auto screenshots  
- **Stop Capture** → Stop background thread  
- **Select Folder** → Choose screenshot save path  

### Status Text:
Shows live updates like:

```
Status: Captured screenshot_20250214_103045.png. Waiting 10 minutes...
```

---

## 🔒 Notes & Limitations

- macOS may require screen recording permissions  
- Linux systems may need X11 and screenshot support  
- The app must stay running for captures to continue  

---

## 📄 Full Code

(Paste the main Python file contents here if sharing publicly.)

---

## 📬 Support

If you want extra features such as:

- Modern rounded UI  
- Minimize to system tray  
- Custom time intervals  
- Select area for screenshot  
- Watermarks/time overlay  

Ask and I can upgrade the project!
```
