# 📋 Clipboard Logger

A lightweight Python tool that logs everything you copy to your clipboard — perfect for catching those lost snippets, links, or notes.

---

## ✨ Features

- Logs clipboard text in real-time
- Saves content with timestamps to a local database (`.db` file)
- View all previously copied entries
- Runs quietly in the background
- Ignores empty or whitespace-only copies

---

## 🛠️ Technologies Used

- **Python 3.x**
- [`pyperclip`](https://pypi.org/project/pyperclip/) – for clipboard access
- `shelve` – for lightweight local storage
- `time` & `sys` – for timestamping and control

---

## 🚀 How It Works

1. Run the script
2. Choose:
   - **`n`** to start clipboard logging
   - **`y`** to view previously logged items
   - **`exit`** to quit
3. Copied text gets saved with a timestamp (e.g., `2025-08-26 15-30`)
4. Press `Ctrl+C` to stop logging anytime

---

## 📦 Installation

1. Clone the repo:
   ```
   git clone https://github.com/TheGhostAnalyst/clipboard-logger.git
   cd clipboard-logger
  

2. Install dependencies:
```
   pip install pyperclip
```

3. Run it:
```
   python3 clipboard-logger.py
   ```

---

## 📁 Output

Logs are stored in a file named `Clipboard.db` using Python's built-in `shelve` module.
You can view all saved clips using the menu prompt.

---

## ✅ To-Do / Improvements

* [ ] Add support for duplicate entries (optional)
* [ ] Export logs to a `.txt` or `.csv` file
* [ ] Add GUI (Tkinter or PyQt)
* [ ] Detect non-text clipboard types (images, rich text)
* [ ] Add search/filter feature for past entries

---

## ⚠️ Disclaimer

This tool only captures **text-based** clipboard data. It doesn't access or log clipboard contents unless you explicitly run it.

---

## 🧑‍💻 Author

Made with 🧠 and ☕ by [The Ghost Analyst](https://github.com/TheGhostAnalyst)

---

## 📄 License

MIT License

