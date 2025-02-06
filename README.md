# Windows Search Tool

This project is a **Windows-based search tool** that allows users to input a file or folder path and open it directly in **Windows Explorer**. The script provides a quick way to navigate files and folders using a GUI-based search box.

---

## ✅ Features

- **Open File Location**: If you enter a file path, it opens the folder containing the file.
- **Open Folder Directly**: If you enter a folder path, it opens the folder directly.
- **Press ********`Enter`******** to Search**: Works the same as clicking the button.
- **Standalone EXE Version**: Can be converted into an `.exe` file for easy execution.

---

## 📌 Requirements

To run this script, you need:

- **Python 3.x** installed
- The following built-in Python libraries:
  - `os`
  - `subprocess`
  - `tkinter`
  - `messagebox`

---

## 💡 Problem Statement

**Windows Explorer lacks a simple, dedicated tool for quickly opening files and folders from a custom search box.** This tool provides an easy way to navigate directly to a file or folder.

---

## 🛠️ Solution

This script creates a simple GUI using `Tkinter` where users can:

- **Enter a file/folder path**
- **Press ********`Enter`******** or Click the Button** to open the location
- **Invalid paths show an error message**

---

## 🚀 How to Run the Script

### **Step 1: Install Python**

Ensure you have Python installed. Check using:

```sh
python --version
```

### **Step 2: Run the Script**

1. Save the Python script as `search_tool.py`
2. Open **Command Prompt (cmd)** and navigate to the script location:
   ```sh
   cd path\to\script
   ```
3. Run the script:
   ```sh
   python search_tool.py
   ```

---

## 🔥 How to Convert to EXE

### **Step 1: Install PyInstaller**

```sh
pip install pyinstaller
```

### **Step 2: Create EXE File**

```sh
pyinstaller --onefile --noconsole search_tool.py
```

- `--onefile`: Generates a single `.exe` file
- `--noconsole`: Hides the command prompt window

### **Step 3: Find and Use the EXE**

- The `.exe` file will be inside the `dist` folder.
- Move it to a convenient location and run it like any other application.

---

## 📌 Future Enhancements

- Add a **Browse Button** for file selection.
- Implement **Auto-Suggestions** while typing paths.
- Store frequently used paths for quick access.

---

## 📂 Repository Structure

```
|-- search_tool.py  # Main script
|-- README.md       # Documentation
|-- dist/           # EXE output (after PyInstaller)
```

---

### 📝 Notes

This project is a simple utility for **Windows users** who frequently search for files and folders. It's designed for **quick access and usability**.

